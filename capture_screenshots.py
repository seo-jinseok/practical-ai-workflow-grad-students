from playwright.sync_api import sync_playwright
import os

output_dir = "/Users/truestone/Dropbox/repo/University/Generative AI Special Lecture - Graduate School/v13.0_resources/part2/images"
os.makedirs(output_dir, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    
    # Capture mcp-protocol-intro.png
    page.goto('https://modelcontextprotocol.io/')
    page.wait_for_load_state('networkidle')
    page.screenshot(path=os.path.join(output_dir, 'mcp-protocol-intro.png'))
    
    # Capture speckit-repository.png
    page.goto('https://github.com/github/spec-kit')
    page.wait_for_load_state('networkidle')
    page.screenshot(path=os.path.join(output_dir, 'speckit-repository.png'))
    
    browser.close()

print(f"Screenshots saved in {output_dir}")