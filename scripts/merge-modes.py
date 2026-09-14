#!/usr/bin/env python3
"""Зводить експорти режимів Figma в одну таблицю.

Плагін вивантажує один режим за раз, але сам підписує його в
$extensions."com.figma.modeName" — тож імена файлів не мають значення.

Розкладка:
    tokens-modes/semantic/*.json
    tokens-modes/component/*.json
    tokens-modes/primitives/*.json

Запуск:
    python3 scripts/merge-modes.py              всі колекції
    python3 scripts/merge-modes.py component    одна колекція

На виході: tokens-modes/<колекція>.md — таблиця тих токенів,
значення яких залежать від розміру екрана.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "tokens-modes"
ORDER = ["desktop", "tab-large", "tab", "mob"]


def flatten(path):
    """Листки файлу як {шлях: значення}. Колір повертаємо як hex."""
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    mode = raw.get("$extensions", {}).get("com.figma.modeName")
    flat = {}

    def walk(node, prefix=""):
        if not isinstance(node, dict):
            return
        if "$value" in node:
            val = node["$value"]
            if isinstance(val, dict):
                val = val.get("hex", json.dumps(val, sort_keys=True))
            flat[prefix] = val
            return
        for key, child in node.items():
            if key.startswith("$"):
                continue
            walk(child, f"{prefix}/{key}" if prefix else key)

    walk(raw)
    return mode, flat


def collection(name):
    files = sorted((BASE / name).glob("*.json"))
    if not files:
        return None

    data = {}
    for path in files:
        mode, flat = flatten(path)
        if not mode:
            sys.exit(f"{path.name}: немає $extensions.com.figma.modeName — "
                     "експортуйте плагіном Figma, а не вручну")
        data[mode] = flat

    modes = [m for m in ORDER if m in data] + [m for m in data if m not in ORDER]
    all_keys = sorted(set().union(*(set(d) for d in data.values())))

    differing, missing = [], []
    for key in all_keys:
        values = [data[m].get(key) for m in modes]
        if any(v is None for v in values):
            missing.append(key)
        elif len(set(map(str, values))) > 1:
            differing.append((key, values))

    lines = [
        f"# {name} — залежність від розміру екрана",
        "",
        f"Режимів у експорті: {len(modes)} ({', '.join(modes)}).",
        f"Токенів усього: {len(all_keys)}. Залежать від режиму: **{len(differing)}**.",
        "",
        "| Токен | " + " | ".join(modes) + " |",
        "|---" * (len(modes) + 1) + "|",
    ]
    for key, values in differing:
        lines.append(f"| `{key.replace('/', '.')}` | "
                     + " | ".join(str(v) for v in values) + " |")

    if missing:
        lines += ["", "## Є не в усіх режимах", ""]
        lines += [f"- `{k.replace('/', '.')}`" for k in missing]

    out = BASE / f"{name}.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{name:12} режимів {len(modes)}, токенів {len(all_keys)}, "
          f"залежать від режиму {len(differing)} → {out.relative_to(ROOT)}")
    return out


def main():
    names = sys.argv[1:] or ["semantic", "component", "primitives"]
    done = [n for n in names if collection(n)]
    if not done:
        print("Порожньо. Покладіть файли в tokens-modes/<колекція>/ і запустіть знову.")


if __name__ == "__main__":
    main()
