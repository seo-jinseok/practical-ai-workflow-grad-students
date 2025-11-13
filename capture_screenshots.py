from playwright.sync_api import sync_playwright
import os

output_dir = "/Users/truestone/Dropbox/repo/University/Generative AI Special Lecture - Graduate School/v13.0_resources/part2/images"
os.makedirs(output_dir, exist_ok=True)

def launch_browser(playwright):
    """Attempt to launch Chromium first, then fall back to WebKit to avoid macOS sandbox issues."""
    launch_attempts = [
        ("chromium", {"channel": "chrome", "headless": True}),
        ("chromium", {"headless": True}),
        ("webkit", {"headless": True}),
    ]

    last_error = None
    for browser_name, kwargs in launch_attempts:
        try:
            browser_type = getattr(playwright, browser_name)
            print(f"Trying to launch {browser_name} with options {kwargs}...")
            return browser_type.launch(**kwargs), browser_name
        except Exception as exc:
            last_error = exc
            print(f"Failed to launch {browser_name}: {exc}")

    raise RuntimeError(
        "Unable to launch any Playwright browser. "
        "See Context_and_Planning/demo-files/06-mcp-installation/troubleshooting-quick.md "
        "for macOS bootstrap_check_in mitigation steps."
    ) from last_error


with sync_playwright() as p:
    browser, backend = launch_browser(p)
    print(f"Using {backend} backend for screenshots.")
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
