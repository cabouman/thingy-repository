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

## Linked thingys (Option 1)

A thingy that already runs somewhere on the web - GitHub Pages, a
personal site - joins the repository through a frame: a tiny static
Space whose page embeds the thingy's address in a full-window iframe.
Duplicate the frame template at
https://huggingface.co/spaces/cabouman/thingy-template-link and set
four things: the `THINGY_URL` line in `index.html`, the title (in
both `index.html` and the README), `icon.png`, and `thingy_author:`.
If the person has a Hugging Face account, the frame belongs in it, so
the likes accrue to them; if not, they simply email Charlie the URL,
icon, and a one-line description, and Charlie's assistant builds the
frame under Charlie's account with the person credited. Check that
the thingy's host allows embedding (GitHub Pages does); if it
refuses, the frame's "open directly" link still works, but tell the
person their thingy will not display inline.

## Hosted thingys

A thingy that needs a real server can be hosted under Charlie's paid
account. That route has its own guide:
https://cabouman-thingy-repository.static.hf.space/hosted-thingy-guide.md

## Submitting

When the person is happy with the thingy, they email the Space link
to Charles.Bouman@gmail.com with the subject
"Thingy submission: [name]". Charlie reviews it; accepted thingys
appear on the repository page automatically, ordered by likes.
