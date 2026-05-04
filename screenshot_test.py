"""Screenshot test for the modernized website."""
import subprocess
import time
import sys
import os
from playwright.sync_api import sync_playwright

# Start the server
server = subprocess.Popen(
    [sys.executable, '-m', 'http.server', '8080'],
    cwd='/home/fido/work/mattions.github.com',
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
time.sleep(2)

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )
        context = browser.new_context(
            viewport={'width': 1280, 'height': 900},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        )
        page = context.new_page()
        
        # Navigate
        page.goto('http://localhost:9999/', wait_until='networkidle', timeout=30000)
        
        # Wait for page to load
        page.wait_for_timeout(1000)
        
        # Get title
        title = page.title()
        print(f"Title: {title}")
        
        # Screenshot 1: Full page (hero)
        page.screenshot(path='/tmp/homepage_full.png', full_page=True)
        print("Screenshot 1: Full page saved")
        
        # Screenshot 2: Hero section only
        page.goto('http://localhost:9999/', wait_until='networkidle', timeout=30000)
        page.wait_for_timeout(500)
        hero = page.locator('.hero')
        hero.screenshot(path='/tmp/homepage_hero.png')
        print("Screenshot 2: Hero section saved")
        
        # Scroll to projects
        page.evaluate('window.scrollTo(0, document.body.scrollHeight / 2)')
        page.wait_for_timeout(1000)
        projects = page.locator('#projects')
        projects.screenshot(path='/tmp/homepage_projects.png')
        print("Screenshot 3: Projects section saved")
        
        # Scroll to blog
        page.evaluate('window.scrollTo(0, document.body.scrollHeight * 0.7)')
        page.wait_for_timeout(1000)
        blog = page.locator('#blog')
        blog.screenshot(path='/tmp/homepage_blog.png')
        print("Screenshot 4: Blog section saved")
        
        # Full page scroll
        page.goto('http://localhost:9999/', wait_until='networkidle', timeout=30000)
        page.wait_for_timeout(2000)
        # Scroll to bottom
        page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        page.wait_for_timeout(1000)
        page.screenshot(path='/tmp/homepage_bottom.png')
        print("Screenshot 5: Bottom of page saved")
        
        # Check for errors
        console_logs = page.locator('body').evaluate('''() => {
            return document.querySelectorAll('*').length + ' elements on page';
        }''')
        print(f"Page elements: {console_logs}")
        
        browser.close()
        print("\nAll screenshots captured successfully!")

finally:
    server.terminate()
    server.wait()
