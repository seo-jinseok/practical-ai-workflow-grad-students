#!/usr/bin/env python3
"""
Screenshot capture script for Part 1 and Part 2 web pages
Uses Playwright to capture high-quality screenshots
"""

import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright

# Define screenshots to capture
SCREENSHOTS = {
    "part2": [
        {
            "url": "https://modelcontextprotocol.io/",
            "filename": "mcp-protocol-intro.png",
            "description": "MCP Protocol Introduction",
            "wait_for": "h1",  # Wait for main heading
        },
        {
            "url": "https://github.com/github/spec-kit",
            "filename": "speckit-repository.png",
            "description": "SpecKit Repository",
            "wait_for": "article",  # Wait for README article
        },
    ],
}

async def capture_screenshot(page, config, output_dir):
    """Capture a single screenshot"""
    url = config["url"]
    filename = config["filename"]
    description = config["description"]
    wait_for = config.get("wait_for", "body")
    
    print(f"\n📸 Capturing: {description}")
    print(f"   URL: {url}")
    
    try:
        # Navigate to URL
        await page.goto(url, wait_until="networkidle", timeout=30000)
        
        # Wait for specific element
        await page.wait_for_selector(wait_for, timeout=10000)
        
        # Additional wait for dynamic content
        await asyncio.sleep(2)
        
        # Take screenshot
        output_path = output_dir / filename
        await page.screenshot(path=str(output_path), full_page=False)
        
        # Check file size
        size_mb = output_path.stat().st_size / (1024 * 1024)
        print(f"   ✅ Saved: {filename} ({size_mb:.2f} MB)")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")
        return False

async def main():
    """Main function to capture all screenshots"""
    
    # Get base directory (repository root)
    base_dir = Path(__file__).parent
    
    # Define output directories
    part2_dir = base_dir / "v13.0_resources" / "part2" / "images"
    
    # Ensure directories exist
    part2_dir.mkdir(parents=True, exist_ok=True)
    
    print("🚀 Starting screenshot capture...")
    print(f"📁 Output directory: {part2_dir}")
    
    async with async_playwright() as p:
        # Launch browser
        print("\n🌐 Launching browser...")
        browser = await p.chromium.launch(headless=True)
        
        # Create context with specific viewport
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=1,
        )
        
        # Create page
        page = await context.new_page()
        
        # Capture Part 2 screenshots
        print("\n📋 Part 2 Screenshots:")
        success_count = 0
        total_count = len(SCREENSHOTS["part2"])
        
        for config in SCREENSHOTS["part2"]:
            if await capture_screenshot(page, config, part2_dir):
                success_count += 1
        
        # Close browser
        await browser.close()
        
        # Summary
        print("\n" + "="*60)
        print(f"✅ Successfully captured: {success_count}/{total_count} screenshots")
        print("="*60)
        
        if success_count == total_count:
            print("\n🎉 All screenshots captured successfully!")
            print("\n📝 Next steps:")
            print("   1. Review images in:", part2_dir)
            print("   2. Update documentation checksums")
            print("   3. Commit to git")
            return 0
        else:
            print("\n⚠️  Some screenshots failed. Check errors above.")
            return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)
