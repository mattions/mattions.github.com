#!/usr/bin/env python3
"""Capture QA screenshots of the website."""

import subprocess
import os

screenshots = [
    ("http://localhost:8888/", "screenshot-home-full.png", "Full homepage with blog, X feed, and projects"),
    ("http://localhost:8888/#blog", "screenshot-blog-feed.png", "Blog feed section"),
    ("http://localhost:8888/#social", "screenshot-x-feed.png", "X/Twitter feed section"),
    ("http://localhost:8888/#projects", "screenshot-projects.png", "Projects section"),
]

for url, filename, desc in screenshots:
    outpath = f"/home/fido/work/mattions.github.com/{filename}"
    print(f"Capturing: {filename} ({desc})")
    result = subprocess.run(
        ["playwright", "screenshot", "--viewport-size=1440,900", url, outpath],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  ✗ Failed: {result.stderr[:300]}")
    else:
        print(f"  ✓ Saved ({os.path.getsize(outpath)} bytes)")
