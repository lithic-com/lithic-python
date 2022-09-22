from __future__ import annotations

import re
import ast
from pathlib import Path

# Taken from https://github.com/asottile/blacken-docs/blob/main/blacken_docs.py
MARKDOWN_CODE_BLOCK_RE = re.compile(
    r"(?P<before>^(?P<indent> *)```\s*python\n)" r"(?P<code>.*?)" r"(?P<after>^(?P=indent)```\s*$)",
    re.DOTALL | re.MULTILINE,
)


def check_file(path: Path) -> None:
    contents = path.read_text()
    for match in MARKDOWN_CODE_BLOCK_RE.finditer(contents):
        code = match.group("code")
        try:
            ast.parse(code)
        except Exception:
            print(f"---- The {path} file contains invalid Python code ---")
            print(code)
            print("---- See above output ----")
            raise


def main() -> int:
    # NOTE: this may catch files that we don't want to check but it's fine for now
    for file in Path.cwd().glob("**/*.md"):
        check_file(file)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
