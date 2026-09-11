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
- **Python:** two routes.
  - **Free:** Gradio-Lite inside a static Space. Before writing any
    code, read the Python guide at
    https://cabouman-thingy-repository.static.hf.space/python-thingy-guide.md
    and follow it exactly - it gives the pinned runtime version, a
    required shim that keeps the page working, the app-writing
    rules, and the list of usable packages. The Python runs in the
    visitor's browser; there is no GPU, and startup takes ten to
    fifteen seconds.
  - **Paid:** a standard Gradio Space (SDK `gradio`), which runs
    current Gradio on a server. It requires a paid Hugging Face
    plan - tell the person before going this route. Prefer it when
    the person has one.

## Submitting

When the person is happy with the thingy, they email the Space link
to Charles.Bouman@gmail.com with the subject
"Thingy submission: [name]". Charlie reviews it; accepted thingys
appear on the repository page automatically, ordered by likes.
