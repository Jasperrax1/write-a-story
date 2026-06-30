#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


EXPECTED_FILES = [
    "SKILL.md",
    "cheatsheet.md",
    "patterns.md",
    "glossary.md",
    "three-book-synthesis.md",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        fail(f"{path} is not UTF-8 text")


def frontmatter_value(frontmatter: str, key: str) -> str | None:
    pattern = re.compile(rf"^{re.escape(key)}:\s*(.+?)\s*$", re.MULTILINE)
    match = pattern.search(frontmatter)
    if not match:
        return None
    value = match.group(1).strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        value = value[1:-1]
    return value


def main() -> None:
    skill_dir = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else Path.cwd()

    if not skill_dir.exists():
        fail(f"skill directory not found: {skill_dir}")

    for relative in EXPECTED_FILES:
        if not (skill_dir / relative).is_file():
            fail(f"missing required file: {relative}")

    skill_md = read(skill_dir / "SKILL.md")
    match = re.match(r"^---\n(.*?)\n---", skill_md, re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")

    frontmatter = match.group(1)
    name = frontmatter_value(frontmatter, "name")
    description = frontmatter_value(frontmatter, "description")

    if name != "write-a-story":
        fail("SKILL.md frontmatter name must be write-a-story")
    if not description:
        fail("SKILL.md frontmatter description is required")
    if not re.fullmatch(r"[a-z0-9-]+", name):
        fail("skill name must be lowercase hyphen-case")

    chapters_dir = skill_dir / "chapters"
    chapters = sorted(chapters_dir.glob("*.md"))
    if len(chapters) != 44:
        fail(f"expected 44 chapter files, found {len(chapters)}")

    missing_links = []
    for md_path in [skill_dir / "SKILL.md", skill_dir / "cheatsheet.md", skill_dir / "patterns.md", skill_dir / "glossary.md", skill_dir / "three-book-synthesis.md"]:
        text = read(md_path)
        for link in re.findall(r"\[[^\]]+\]\(([^)#][^)]+)\)", text):
            if "://" in link or link.startswith("mailto:"):
                continue
            target = (md_path.parent / link).resolve()
            if not target.exists():
                missing_links.append(f"{md_path.relative_to(skill_dir)} -> {link}")

    if missing_links:
        fail("broken relative links:\n" + "\n".join(missing_links))

    print("OK: write-a-story skill verified.")


if __name__ == "__main__":
    main()
