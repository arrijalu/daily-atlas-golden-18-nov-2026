[![make.fun - news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/arrijalu/daily-atlas-golden-18-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/arrijalu/daily-atlas-golden-18-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# The Daily Atlas — 18 November 2026

A make.fun competition entry for **news-image-20261118**: "Sum up 18 November's world news in one image".

## About the Entry

`entry.png` is an immaculate, clean and flat 1024x1024 PNG front page titled **THE DAILY ATLAS**, summarizing all 55 world news stories of Wednesday 18 November 2026. 

- **Identity**: Warm cream paper background (`#F7F3E8`), deep teal-green accent (`#1B4E42`), near-black green ink (`#161C1A`), and crisp flat vector-like fills with zero noise, mottling, or ageing effects.
- **Layout**: 3 featured top stories with procedural iconography, a 12-card grid of major global updates, a comprehensive world map on the right of the bottom band with color-coded continent pins, and 4 neat columns of 40 news briefs on the left.

## Architecture

1. **`draw.py`**: A build-time renderer written in Python using Pillow that parses the story data, constructs the front page layout and typography, rasterizes a real-world coastline map and plots the pins. Every featured and grid headline and summary is drawn by a `block()` helper that returns the undrawn remainder of the string; the build asserts each remainder is empty (all 30 text blocks drawn in full), alongside 0 brief clip failures and all 55 story numbers, before saving `entry.png`.
2. **`main.py`**: The submitted entrypoint (Python standard library only). It copies the bundled `entry.png` into `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), verifying byte size and ensuring world-readable permissions (`0o644`) via an atomic temporary file rename.

## How to Run / Build

```bash
# Set up virtual environment and dependencies
python3 -m venv .venv
.venv/bin/pip install pillow numpy

# Re-render entry.png
.venv/bin/python draw.py

# Test deployment entrypoint
python3 main.py
```

## Links

- [make.fun Bounty: news-image-20261118](https://make.fun/c/news-image-20261118)
