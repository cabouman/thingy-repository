---
title: Thingy Template (Server)
emoji: 🏭
colorFrom: yellow
colorTo: pink
sdk: gradio
sdk_version: 5.45.0
app_file: app.py
pinned: false
license: bsd-3-clause
thingy_author: Your Name Here
short_description: Real Gradio on a server; the author stays credited
---

The pattern for a hosted thingy: ordinary Gradio running on a Hugging
Face server, used when a thingy is debugged and ready for a home under
Charlie's account.

Credit for the true author appears in two places, and both must be
set when a thingy is promoted:

1. `thingy_author` in this file's metadata - the repository's front
   page shows the tile as "by" this name instead of the account that
   hosts it.
2. The `AUTHOR` line at the top of `app.py` - the app itself opens
   with "By **author**".

The Gradio release is pinned to 5.45.0 so an app developed on the
free Lite template behaves identically here.

Part of The Thingy Repository:
https://huggingface.co/spaces/cabouman/thingy-repository
