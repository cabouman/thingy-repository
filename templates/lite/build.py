#!/usr/bin/env python3
"""Build the Lite template's index.html.

Reads ../app.py and the shim from ../../python-thingy-guide.md, so the
app and the shim each live in exactly one place. Run from this
directory:

    python3 build.py
"""

import html
import pathlib
import re

HERE = pathlib.Path(__file__).parent
APP = (HERE / ".." / "app.py").resolve()
GUIDE = (HERE / ".." / ".." / "python-thingy-guide.md").resolve()


def shim():
    text = GUIDE.read_text(encoding="utf-8")
    section = text.split("## The shim", 1)[1]
    match = re.search(r"```html\n(.*?)```", section, re.S)
    if not match:
        raise SystemExit("The shim block was not found in the guide.")
    return match.group(1).rstrip()


def main():
    app = html.escape(APP.read_text(encoding="utf-8"), quote=False)
    page = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>The Wiggler</title>
    {shim()}
    <script type="module" crossorigin src="https://cdn.jsdelivr.net/npm/@gradio/lite@5.45.0/dist/lite.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gradio/lite@5.45.0/dist/lite.css" />
  </head>
  <body>
    <gradio-lite>
<gradio-requirements>matplotlib</gradio-requirements>
<gradio-file name="app.py" entrypoint>
{app}
</gradio-file>
</gradio-lite>
  </body>
</html>
"""
    out = HERE / "index.html"
    out.write_text(page, encoding="utf-8")
    print(f"Wrote {out} ({len(page)} bytes)")


if __name__ == "__main__":
    main()
