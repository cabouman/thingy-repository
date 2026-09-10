#!/usr/bin/env python3
"""Draw preview.png, the 1200x630 link-preview card for the Thingy Repository.

Run it if you change the look, then commit the new preview.png.

    python3 make_card.py
"""

import math
import pathlib

from PIL import Image, ImageDraw, ImageFont

HERE = pathlib.Path(__file__).parent

BG = (253, 243, 213)
INK = (45, 42, 38)
MUTED = (122, 108, 82)
ACCENT = (194, 142, 14)
CREAM = (250, 248, 244)
GOLD = (207, 185, 145)

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_PLAIN = "/System/Library/Fonts/Supplemental/Arial.ttf"


def draw_face(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=CREAM, outline=INK,
              width=int(r * 0.06))
    eye_dx, eye_y = r * 0.36, cy - r * 0.22
    eye_w, eye_h = r * 0.115, r * 0.30
    for sx in (-1, 1):
        ex = cx + sx * eye_dx
        d.rounded_rectangle(
            [ex - eye_w, eye_y - eye_h / 2, ex + eye_w, eye_y + eye_h / 2],
            radius=eye_w, fill=INK)
    mr = r * 0.60
    d.arc([cx - mr, cy - mr * 0.55, cx + mr, cy + mr * 1.15],
          start=25, end=155, fill=INK, width=int(r * 0.11))


def draw_star(d, cx, cy, r, fill):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    d.polygon(pts, fill=fill)


def draw_heart(d, cx, cy, r, fill):
    d.ellipse([cx - r, cy - r * 0.9, cx, cy + r * 0.1], fill=fill)
    d.ellipse([cx, cy - r * 0.9, cx + r, cy + r * 0.1], fill=fill)
    d.polygon([(cx - r * 0.98, cy - r * 0.18), (cx + r * 0.98, cy - r * 0.18),
               (cx, cy + r * 0.95)], fill=fill)


def tile(d, x, y, s, color):
    d.rounded_rectangle([x, y, x + s, y + s], radius=int(s * 0.18),
                        fill=color, outline=(45, 42, 38, 40), width=3)


def centred(d, text, font, cx, y, fill):
    left, top, right, bottom = d.textbbox((0, 0), text, font=font)
    d.text((cx - (right - left) / 2 - left, y - top), text, font=font, fill=fill)


def main():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    s, gap = 190, 48
    x0, y0 = W // 2 - (3 * s + 2 * gap) // 2, 78
    tile(d, x0, y0, s, GOLD)
    draw_face(d, x0 + s // 2, y0 + s // 2, int(s * 0.34))
    tile(d, x0 + s + gap, y0, s, (255, 233, 179))
    draw_star(d, x0 + s + gap + s // 2, y0 + s // 2 + 6, int(s * 0.36), ACCENT)
    tile(d, x0 + 2 * (s + gap), y0, s, CREAM)
    draw_heart(d, x0 + 2 * (s + gap) + s // 2, y0 + s // 2 + 8,
               int(s * 0.30), (240, 113, 103))

    f_title = ImageFont.truetype(FONT_BOLD, 84)
    f_sub = ImageFont.truetype(FONT_PLAIN, 36)
    f_url = ImageFont.truetype(FONT_PLAIN, 26)
    centred(d, "The Thingy Repository", f_title, W // 2, 356, INK)
    centred(d, "Thingys built by Friends of Charlie (FoC)", f_sub, W // 2, 470, MUTED)
    centred(d, "huggingface.co/spaces/cabouman/thingy-repository", f_url, W // 2, 546, MUTED)

    path = HERE / "preview.png"
    img.save(path)
    print(f"Wrote {path}  ({W}x{H})")


if __name__ == "__main__":
    main()
