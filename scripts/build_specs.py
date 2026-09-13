"""Збирає повну специфікацію компонентів: розмітка плюс усі стилі.

Імпортується з build-brief.py. Окремий файл, щоб генератор лишався читабельним.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Класи, які обслуговують саму документацію, а не дизайн-систему.
CHROME = (
    "ds-preview", "ds-btn-row", "ds-btn-item", "ds-btn-caption", "ds-btn-flag",
    "ds-table", "ds-sw", "ds-bp", "ds-page", "ds-icon-grid", "ds-download",
    "ds-art-type", "ds-type",
)


def css_variables(css):
    """Мапа --змінна → значення з :root."""
    return {m.group(1): m.group(2).strip()
            for m in re.finditer(r"^\s*(--[a-z0-9-]+):\s*([^;]+);", css, re.M)}


def expand(value, variables):
    """Підставляє значення змінної, повертаючи (значення, використані імена)."""
    used = []

    def swap(m):
        var = m.group(1)
        if var not in variables:
            return m.group(0)
        used.append(var)
        return variables[var]

    out = value
    for _ in range(5):
        nxt = re.sub(r"var\((--[a-z0-9-]+)\)", swap, out)
        if nxt == out:
            break
        out = nxt
    return out, list(dict.fromkeys(used))


AT_RULE = re.compile(r"\n(@(?:keyframes|media|supports)[^{]*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\})", re.S)


def at_rules(css):
    """@keyframes і @media — віддаємо як є, вкладені правила не розбираємо."""
    return [m.group(1) for m in AT_RULE.finditer(css)]


def parse_rules(css):
    """Правила верхнього рівня як (селектор, тіло). At-правила вирізані."""
    plain = AT_RULE.sub("\n", css)
    out = []
    for m in re.finditer(r"\n([^{}@][^{}]*?)\s*\{([^{}]*)\}", plain):
        selector = m.group(1)
        # коментар перед селектором у той самий фрагмент не тягнемо
        selector = re.sub(r"/\*.*?\*/", "", selector, flags=re.S).strip()
        if not selector:
            continue
        out.append((selector, m.group(2)))
    return out


def classes_in(selector):
    return re.findall(r"\.([a-zA-Z0-9_-]+)", selector)


def assign(rules, components):
    """Розкладає правила по компонентах за найдовшим збігом класу."""
    buckets = {c: [] for c in components}
    shared = []
    for selector, body in rules:
        if any(c in selector for c in CHROME) or selector.strip() == ":root":
            continue
        best, best_len = None, 0
        for cls in classes_in(selector):
            for comp in components:
                if cls.startswith(comp) and len(comp) > best_len:
                    best, best_len = comp, len(comp)
        (buckets[best] if best else shared).append((selector, body))
    return buckets, shared


def format_rule(selector, body, variables):
    lines = [f"{selector} {{"]
    for raw in body.strip().splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("/*"):
            lines.append(f"  {line}")
            continue
        prop = re.match(r"([a-z-]+):\s*(.+?);\s*(/\*.*\*/)?$", line)
        if prop:
            value, used = expand(prop.group(2), variables)
            tail = prop.group(3) or ("/* " + ", ".join(used) + " */" if used else "")
            lines.append(f"  {prop.group(1)}: {value};" + (f" {tail}" if tail else ""))
        else:
            lines.append(f"  {line}")
    lines.append("}")
    return "\n".join(lines)


def structure(page):
    """Розмітка компонента: спершу «Збірка», інакше прев'ю."""
    path = ROOT / f"{page}.mdx"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    # Найбільший демо-блок — це майже завжди повна збірка компонента
    demos = re.findall(r"<div className=\"ds-btn-row[^\"]*\">\n(.*?)\n</div>", text, re.S)
    if demos:
        markup = max(demos, key=len)
    else:
        preview = re.search(r"<span className=\"ds-preview__stage[^\"]*\">(.*?)</span>\n</div>", text, re.S)
        if not preview:
            return None
        markup = preview.group(1)
    markup = re.sub(r"^ {2}", "", markup, flags=re.M)
    markup = markup.replace("className=", "class=")
    return markup.strip()


def icon_sources():
    """SVG-код іконок із foundations/icons.mdx.

    У CSS іконки — це mask із data-URI, і такі правила переживають не кожен
    інструмент. Тому в специфікацію кладемо ще й вихідний SVG, щоб генератор
    міг вставити його інлайном.
    """
    path = ROOT / "foundations" / "icons.mdx"
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```html (\S+\.svg)\n(.*?)\n```", text, re.S)
    if not blocks:
        return ""
    out = ["\n### Icons — SVG source\n"]
    out.append(
        "In CSS these are drawn as `mask` with a data URI so they inherit `currentColor`.\n"
        "If masks do not survive your tool, inline the SVG below instead and set `fill`\n"
        "to the icon colour. Default size is 16px; breadcrumbs draw arrow-side at 12px.\n"
    )
    out.append("```html")
    for name, svg in blocks:
        out.append(f"<!-- {name} -->")
        out.append(svg.strip())
    out.append("```\n")
    return "\n".join(out)


def build():
    css = (ROOT / "style.css").read_text(encoding="utf-8")
    spec = json.loads((ROOT / "scripts" / "brief-inventory.json").read_text(encoding="utf-8"))
    variables = css_variables(css)
    rules = parse_rules(css)

    items = [i for g in spec["groups"] for i in g["items"] if i["class"]]
    components = [i["class"].split("--")[0] for i in items]
    buckets, shared = assign(rules, components)

    out = []
    root = next((b for s, b in rules if s.strip() == ":root"), None)
    if root:
        out.append("\n### Design tokens as CSS variables\n")
        out.append("Every value below is resolved inline in the rules that follow. "
                   "This block is the map from Figma token to value.\n")
        out.append("```css\n:root {" + root + "}\n```\n")

    for group in spec["groups"]:
        for item in group["items"]:
            if not item["class"]:
                continue
            key = item["class"].split("--")[0]
            body = buckets.get(key) or []
            if not body:
                continue
            out.append(f"\n### {group['name']} — {item['title']}\n")
            out.append(item["purpose"] + "\n")
            markup = structure(item["page"])
            if markup:
                out.append("Markup:\n\n```html\n" + markup + "\n```\n")
            out.append("Styles:\n\n```css")
            for selector, rule_body in body:
                out.append(format_rule(selector, rule_body, variables))
            out.append("```\n")
            buckets[key] = []

    out.append(icon_sources())

    at = at_rules(css)
    if at:
        out.append("\n### Motion\n")
        out.append("The only animation in the system: the loading spinner inside a button.\n")
        out.append("```css")
        out.extend(at)
        out.append("```\n")

    if shared:
        out.append("\n### Shared\n")
        out.append("Rules used by more than one component.\n")
        out.append("```css")
        for selector, rule_body in shared:
            out.append(format_rule(selector, rule_body, variables))
        out.append("```\n")

    return "\n".join(out)
