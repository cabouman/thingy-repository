# The Thingy Repository

Source for the front page of the Thingy Repository, a gallery of small
web apps ("thingys") built by Friends of Charlie (FoC).

- Live page: https://huggingface.co/spaces/cabouman/thingy-repository
- The approved list is a Hugging Face collection:
  https://huggingface.co/collections/cabouman/the-thingy-repository

## How it works

`index.html` is the whole app. On each visit it reads the collection
through the Hugging Face API and draws one square tile per thingy,
sorted by likes (most liked first). A tile shows the Space's
`icon.png` if it has one, and otherwise falls back to the Space's
emoji on a colored square.

## Files

- `index.html` - the page
- `make_card.py` - draws `preview.png`, the 1200x630 link-preview card
- `.hf/README.md` - the metadata file deployed to the Space
- `.github/workflows/deploy-to-hf.yml` - pushes the page to the Space
  on every push to main (needs the `HF_TOKEN` repository secret)

## Submitting a thingy

Build your thingy as a public static Hugging Face Space under your own
account, give it an open-source license, a square `icon.png`, and a
short description, then email the link to Charles.Bouman@gmail.com
with the subject "Thingy submission: [name]". Full instructions are on
the live page.
