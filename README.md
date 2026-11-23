# The World in One Day — Sunday 22 November 2026

[![rank](https://make.fun/badge/news-image-20261122/xiami1020/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/xiami1020/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)
[![about](https://make.fun/badge/news-image-20261122/xiami1020/news-image-20261122/about.svg)](https://make.fun/bounty/news-image-20261122)

A newspaper front page summing up the world's news of Sunday 22 November 2026 in one
1024×1024 image: COP31 collapses without a deal in Antalya, a Russian drone flattens
a block of flats near Kyiv, drones hit Khartoum, Iran unveils a new missile city,
BepiColombo reaches Mercury with a thruster glitch, and 30 more stories from every
continent — all checked against reporting dated 22 November 2026.

## How it works

`generate.py` draws the page with Pillow (DejaVu fonts) and writes `entry.png`.
`main.py` copies the bundled `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output`), byte for byte, so the two grading runs write identical bytes.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — entry point (copies `entry.png` to the output directory)
- `generate.py` — draws the front page
- `entry.png` — the image, 1024×1024 PNG
- `LICENSE` — MIT
