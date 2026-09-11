# Hosting guide for The Thingy Repository

You are an AI assistant helping a person whose thingy needs a real
server - it is too slow in the browser, needs packages Pyodide lacks,
or needs persistent server-side state. Such a thingy can be hosted
under Charlie's paid Hugging Face account, with the person credited
as its author.

## The path

1. Develop and debug on the free Lite template first
   (https://huggingface.co/spaces/cabouman/thingy-template-lite),
   following the builder's guide at
   https://cabouman-thingy-repository.static.hf.space/claude-instructions.md.
   The Lite and hosted routes both run Gradio 5.45.0, so an app that
   works on one behaves identically on the other. If the thingy
   cannot run in the browser at all, develop it locally against
   `gradio==5.45.0` instead.
2. When it works, the person emails Charlie as usual (the button on
   the repository page) and says the thingy needs hosting.
3. Charlie's assistant then promotes it: a new Space under `cabouman/`
   following https://huggingface.co/spaces/cabouman/thingy-template
   (SDK `gradio`, `sdk_version: 5.45.0`), carrying the thingy's
   `app.py`, `requirements.txt`, and `icon.png`.

## Credit for the true author

Set in two places on the hosted Space, always:

- `thingy_author:` in the README metadata - the repository's front
  page then shows the tile as "by" this name rather than the hosting
  account.
- The `AUTHOR` line at the top of `app.py` - the app opens with
  "By **author**".

## Verification before it goes live

Whoever promotes the thingy opens the hosted Space, confirms it
builds and runs, exercises its controls, and makes simple fixes if
needed. Then Charlie adds it to the collection as with any thingy.
