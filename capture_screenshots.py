#!/usr/bin/env python3
"""Capture QA screenshots of the website."""

import subprocess
import sys

# URLs to capture
screenshots = [
    ("http://localhost:8888/", "screenshot-home-full.png", "Full homepage"),
    ("http://localhost:8888/blog", "screenshot-blog.png", "Blog page"),
    ("http://localhost:8888/categories", "screenshot-categories.png", "Categories page"),
]

for url, filename, description in screenshots:
    print(f"📸 Capturing: {description} -> {filename}")
    try:
        result = subprocess.run([
            "playwright",
            "screenshot",
            "--viewport-size=1280,800",
            url,
            filename
        ], capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print(f"   ✅ Success")
        else:
            print(f"   ⚠️  Failed: {result.stderr}")
    except FileNotFoundError:
        print(f"   ⚠️  Playwright not found")
    except Exception as e:
        print(f"   ⚠️  Error: {e}")

print("\n📊 Screenshots captured!")
