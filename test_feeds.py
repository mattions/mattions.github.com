#!/usr/bin/env python3
"""
Test script to verify blog and X/Twitter feeds load correctly on the website.
Uses Playwright to automate browser testing and capture screenshots.
"""

import asyncio
import os
import sys
from playwright.async_api import async_playwright

# Start a local HTTP server to serve the site
import subprocess
import time
import signal

def start_server():
    """Start a local HTTP server to serve the site."""
    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", "8888"],
        cwd=os.path.dirname(os.path.abspath(__file__)),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(2)  # Wait for server to start
    return server

async def test_feeds():
    """Test that blog and X/Twitter feeds load correctly."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Navigate to the site
        await page.goto("http://localhost:8888", wait_until="networkidle", timeout=30000)
        
        # Test 1: Check blog feed loads
        print("Test 1: Checking blog feed...")
        try:
            blog_feed = await page.wait_for_selector("#blogFeed", timeout=10000)
            await page.wait_for_selector(".blog-item", timeout=10000)
            blog_items = await page.query_selector_all(".blog-item")
            if len(blog_items) > 0:
                print(f"✓ Blog feed loaded with {len(blog_items)} items")
                # Take screenshot of blog feed
                await page.screenshot(path="screenshot-blog-feed.png", full_page=False)
                print("✓ Screenshot saved: screenshot-blog-feed.png")
            else:
                print("✗ Blog feed is empty")
        except Exception as e:
            print(f"✗ Blog feed test failed: {e}")
        
        # Test 2: Check X/Twitter feed loads
        print("\nTest 2: Checking X/Twitter feed...")
        try:
            twitter_embed = await page.wait_for_selector("#twitterEmbed", timeout=10000)
            # Check if the embed or fallback is visible
            timeline = await page.query_selector("#twitterTimeline")
            fallback = await page.query_selector("#twitterFallback")
            
            if timeline and await timeline.is_visible():
                print("✓ X/Twitter embed loaded")
                await page.screenshot(path="screenshot-x-feed.png", full_page=False)
                print("✓ Screenshot saved: screenshot-x-feed.png")
            elif fallback and await fallback.is_visible():
                print("✓ X/Twitter fallback content is visible")
                await page.screenshot(path="screenshot-x-feed.png", full_page=False)
                print("✓ Screenshot saved: screenshot-x-feed.png")
            else:
                print("✗ X/Twitter feed is not visible")
        except Exception as e:
            print(f"✗ X/Twitter feed test failed: {e}")
        
        # Test 3: Check categories page
        print("\nTest 3: Checking categories page...")
        try:
            await page.goto("http://localhost:8888/categories.html", wait_until="networkidle", timeout=30000)
            categories_page = await page.wait_for_selector("h1", timeout=10000)
            if categories_page:
                print("✓ Categories page loaded")
                await page.screenshot(path="screenshot-categories.png", full_page=False)
                print("✓ Screenshot saved: screenshot-categories.png")
            else:
                print("✗ Categories page failed to load")
        except Exception as e:
            print(f"✗ Categories page test failed: {e}")
        
        await browser.close()

if __name__ == "__main__":
    # Start local server
    print("Starting local HTTP server...")
    server = start_server()
    
    try:
        # Run tests
        asyncio.run(test_feeds())
    finally:
        # Stop server
        print("\nStopping local HTTP server...")
        server.terminate()
        server.wait()
        print("Done!")
