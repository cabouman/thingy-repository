---
title: Thingy Template (Lite)
emoji: 🧪
colorFrom: yellow
colorTo: green
sdk: static
pinned: false
license: bsd-3-clause
short_description: Duplicate me to start a Python thingy - runs free in the browser
---

The starting point for a Python thingy on a free Hugging Face account.
The Python runs in the visitor's browser; there is no server and no
cost.

To use it: duplicate this Space (the "..." menu, then "Duplicate this
Space"), then have your AI assistant replace the sample app inside
`index.html` with yours and swap `icon.png` for your own. The full
rules are in the builder's guide:
https://cabouman-thingy-repository.static.hf.space/claude-instructions.md

`app.py` holds the readable copy of the sample app, and `build.py`
shows how `index.html` is assembled from it. The page pins Gradio-Lite
5.45.0 and carries a shim that keeps it working; do not remove either.

Part of The Thingy Repository:
https://huggingface.co/spaces/cabouman/thingy-repository
