#!/usr/bin/env python3
"""Збирає system-brief.md — компактний опис системи для генерації дизайну.

Джерела:
  tokens.json                   кольори, типографіка, шкала відступів
  style.css                     реальні розміри компонентів
  docs.json                     які сторінки в навігації
  scripts/brief-sections.md     рукописні розділи з плейсхолдерами
  scripts/brief-inventory.json  англійські описи компонентів

Пише два однакові файли:
  system-brief.md                     для читання в репозиторії
  assets/lazarev-design-system.txt    для завантаження зі сторінки Claude Design

Запуск:  python3 scripts/build-brief.py
"""
import json, re, sys, collections
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_specs

ROOT = Path(__file__).resolve().parent.parent


def load_tokens():
    raw = json.loads((ROOT / "tokens.json").read_text(encoding="utf-8"))
    flat = {}

    def walk(node, path=""):
        if not isinstance(node, dict):
            return
        if "value" in node and not isinstance(node["value"], dict):
            flat[path] = node["value"]
            return
        for key, val in node.items():
            walk(val, f"{path}/{key}" if path else key)

    walk(raw)
    return flat


def resolve(flat, value, depth=0):
    """Розгортає посилання {a.b.c} до справжнього значення."""
    if depth > 6 or not isinstance(value, str):
        return value
    match = re.fullmatch(r"\{(.+)\}", value.strip())
    if not match:
        return value
    return resolve(flat, flat.get(match.group(1).replace(".", "/"), value), depth + 1)


def spacing_scale(flat):
    sizes = sorted({int(v) for k, v in flat.items() if k.startswith("primitives/spacing")})
    return ", ".join(str(s) for s in sizes)


def colour_table(flat):
    rows = sorted(
        (k.replace("semantic/color/", ""), resolve(flat, v))
        for k, v in flat.items()
        if k.startswith("semantic/color/")
    )
    return "\n".join(f"| `color/{name}` | {val} |" for name, val in rows)


def text_styles(flat):
    """Групує typography.* назад у складені стилі."""
    styles = collections.defaultdict(dict)
    for key, val in flat.items():
        if not key.startswith("typography/"):
            continue
        parts = key[len("typography/"):].split("/")
        if len(parts) >= 2:
            styles["/".join(parts[:-1])][parts[-1]] = val
    return styles


def type_tables(flat):
    styles = text_styles(flat)
    site, article = [], []
    for name, attrs in sorted(styles.items()):
        if "fontSize" not in attrs:
            continue
        if name.startswith("article/"):
            article.append(
                f'| `{name.replace("/", ".")}` | {attrs.get("fontFamily")} | '
                f'{attrs.get("fontSize")} / {attrs.get("lineHeight")} | {attrs.get("fontWeight")} |'
            )
        else:
            site.append(
                f'| `font.{name.replace("/", ".")}` | {attrs.get("fontFamily")} | '
                f'{attrs.get("fontSize")} / {attrs.get("lineHeight")} | {attrs.get("fontWeight")} | '
                f'{attrs.get("letterSpacing")} | {attrs.get("textCase")} |'
            )
    return "\n".join(site), "\n".join(article)


def css_size(css, cls):
    """Дістає ширину й висоту з правила класу."""
    if not cls:
        return "—"
    rule = re.search(r"\n\." + re.escape(cls) + r"\s*\{([^}]*)\}", css, re.S)
    if not rule:
        return "—"
    body = rule.group(1)
    parts = []
    width = re.search(r"(?<!max-)(?<!min-)width:\s*([^;]+);", body)
    min_width = re.search(r"min-width:\s*([^;]+);", body)
    height = re.search(r"(?<!line-)height:\s*([^;]+);", body)
    if width and width.group(1).strip() not in ("100%", "auto"):
        parts.append(width.group(1).strip())
    elif min_width:
        parts.append("min " + min_width.group(1).strip())
    if height and height.group(1).strip() != "auto":
        parts.append("h " + height.group(1).strip())
    # змінні в брифі нічого не означають — підставляємо значення
    out = " · ".join(parts) if parts else "fluid"
    for var, val in re.findall(r"^\s*(--[a-z0-9-]+):\s*([^;]+);", css, re.M):
        out = out.replace(f"var({var})", val.strip())
    return out


def nav_pages():
    raw = json.loads((ROOT / "docs.json").read_text(encoding="utf-8"))
    found = []

    def walk(node):
        if isinstance(node, dict):
            for key, val in node.items():
                if key == "pages":
                    for page in val:
                        if isinstance(page, str):
                            found.append(page)
                        else:
                            walk(page)
                else:
                    walk(val)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(raw)
    return found


def inventory(css):
    spec = json.loads((ROOT / "scripts" / "brief-inventory.json").read_text(encoding="utf-8"))
    listed = set()
    out = []
    for group in spec["groups"]:
        out.append(f"\n### {group['name']}\n")
        out.append("| Component | CSS class | Size | Purpose |")
        out.append("|---|---|---|---|")
        for item in group["items"]:
            listed.add(item["page"])
            cls = item["class"]
            label = f"`.{cls}`" if cls else "—"
            out.append(f"| {item['title']} | {label} | {css_size(css, cls)} | {item['purpose']} |")
    return "\n".join(out), listed


def main():
    flat = load_tokens()
    css = (ROOT / "style.css").read_text(encoding="utf-8")
    template = (ROOT / "scripts" / "brief-sections.md").read_text(encoding="utf-8")
    site_type, article_type = type_tables(flat)
    inv, listed = inventory(css)

    brief = (
        template.replace("{{SPACING}}", spacing_scale(flat))
        .replace("{{COLORS}}", colour_table(flat))
        .replace("{{TYPE}}", site_type)
        .replace("{{ARTICLE_TYPE}}", article_type)
        .replace("{{INVENTORY}}", inv)
        .replace("{{SPECS}}", build_specs.build())
    )
    left = re.findall(r"\{\{[A-Z_]+\}\}", brief)
    if left:
        sys.exit(f"незаповнені плейсхолдери: {left}")

    (ROOT / "system-brief.md").write_text(brief, encoding="utf-8")

    # Копія для завантаження з сайту. Саме .txt, а не .md: Mintlify віддає
    # markdown як сторінку і на статичний файл відповідає 404.
    download = ROOT / "assets" / "lazarev-design-system.txt"
    download.parent.mkdir(exist_ok=True)
    download.write_text(brief, encoding="utf-8")

    # Нічого не має загубитись: кожна сторінка навігації має бути в інвентарі
    # Сторінки, які не описують компонент: у брифі їм нема чого робити
    skip = {"index", "claude-design", "foundations/colors", "foundations/typography",
            "foundations/spacing", "foundations/icons", "foundations/logo"}
    missing = [p for p in nav_pages() if p not in listed and p not in skip]
    print(f"system-brief.md — {len(brief.splitlines())} рядків, {len(brief)} символів")
    print(f"assets/lazarev-design-system.txt — копія для завантаження з сайту")
    print(f"компонентів в інвентарі: {len(listed)}")
    if missing:
        print("\nУВАГА: сторінки в навігації, яких немає в scripts/brief-inventory.json:")
        for page in missing:
            print("  ", page)
        print("Додайте їх туди, інакше генератор дизайну про них не дізнається.")
    else:
        print("усі сторінки навігації присутні в інвентарі")


if __name__ == "__main__":
    main()
