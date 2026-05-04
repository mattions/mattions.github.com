"""Check the content of the rendered page."""
import subprocess
import sys
import time
from playwright.sync_api import sync_playwright

server = subprocess.Popen(
    [sys.executable, '-m', 'http.server', '9999'],
    cwd='/home/fido/work/mattions.github.com',
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
time.sleep(2)

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
        page = browser.new_page()
        page.goto('http://localhost:9999/', wait_until='networkidle', timeout=30000)
        page.wait_for_timeout(2000)
        
        # Collect all console logs
        console_msgs = []
        page.on('console', lambda msg: console_msgs.append(f"[{msg.type}] {msg.text}"))
        
        # Re-navigate to capture fresh console
        page.goto('http://localhost:9999/', wait_until='networkidle', timeout=30000)
        page.wait_for_timeout(2000)
        
        print("=== CONSOLE MESSAGES ===")
        for msg in console_msgs:
            print(msg)
        
        if not console_msgs:
            print("(no console messages)")
        
        # Get page content summary
        content = page.evaluate('''() => {
            return {
                title: document.title,
                h1: document.querySelector('h1')?.textContent?.trim(),
                sections: Array.from(document.querySelectorAll('section')).map(s => s.id),
                projectCards: document.querySelectorAll('.project-card').length,
                socialLinks: document.querySelectorAll('.social-link').length,
                navItems: Array.from(document.querySelectorAll('.navbar-nav a')).map(a => a.textContent.trim()),
                hasPhoto: !!document.querySelector('.photo-frame img'),
                hasBlogSection: !!document.querySelector('#blog'),
                hasTwitterSection: !!document.querySelector('#social'),
                hasFooter: !!document.querySelector('.footer'),
                cssFile: !!document.querySelector('link[href*="main.css"]'),
                jsErrors: window.__jsErrors || []
            };
        }''')
        
        print("\n=== PAGE STRUCTURE ===")
        for key, val in content.items():
            print(f"  {key}: {val}")
        
        browser.close()

finally:
    server.terminate()
    server.wait()
