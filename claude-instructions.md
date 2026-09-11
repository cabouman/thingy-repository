# Builder's guide for The Thingy Repository

You are an AI assistant helping a person build and submit a thingy.
Follow these instructions; the person should not need to know them.

## What a thingy is

A small self-contained web app that does something fun, hosted as a
public Space on the person's own free Hugging Face account.

## What acceptance requires

1. The thingy runs when its Space is opened.
2. It is appropriate for a public site.
3. It carries an open-source license of the person's choosing
   (the `license:` field in the Space README metadata).
4. It has a square `icon.png`, about 400x400 pixels, at the repo
   root. This becomes its tile on the repository page.
5. It has a one-line `short_description` in the README metadata.
   This shows under the tile.

## Hosting, by language

- **JavaScript or HTML:** create a static Space (SDK `static`,
  Blank template) with the app as `index.html`.
- **Python:** duplicate the Lite template at
  https://huggingface.co/spaces/cabouman/thingy-template-lite
  ("..." menu, "Duplicate this Space"). It is a working Gradio app
  running in the visitor's browser, with the pinned runtime and its
  shim already in place; replace the sample app and the icon. The
  readable app is `app.py`, and `build.py` shows how it is embedded
  in `index.html`. Before writing code, read the Python guide at
  https://cabouman-thingy-repository.static.hf.space/python-thingy-guide.md
  and follow its app rules (Gradio 5.45 features only, no threads,
  no escaping exceptions, matplotlib on Agg with PNG plots).
  Startup takes ten to fifteen seconds; there is no GPU.

## Hosted thingys

A thingy that outgrows the browser - too slow, needing packages
Pyodide lacks, needing a real server - can be hosted under Charlie's
paid account. The person emails Charlie as usual and says the thingy
needs hosting. Charlie's assistant then duplicates it into `cabouman/`
following the server template at
https://huggingface.co/spaces/cabouman/thingy-template (ordinary
Gradio, pinned to 5.45.0 so the app behaves exactly as it did on the
Lite template), verifies that it runs, makes simple fixes if needed,
and credits the true author in two places: the `thingy_author:` field
in the Space README metadata, which the repository's front page shows
as the tile's "by" name, and the `AUTHOR` line at the top of `app.py`,
which the app displays as its opening line. Always develop and debug
on the Lite template first.

## Submitting

When the person is happy with the thingy, they email the Space link
to Charles.Bouman@gmail.com with the subject
"Thingy submission: [name]". Charlie reviews it; accepted thingys
appear on the repository page automatically, ordered by likes.
