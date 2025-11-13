# Screenshot Capture Instructions

**Status**: Awaiting manual capture or Cline MCP automation

## Required Screenshots

### 1. MCP Protocol Introduction
- **URL**: https://modelcontextprotocol.io/
- **Filename**: `mcp-protocol-intro.png`
- **Resolution**: 1920x1080
- **Focus**: Protocol overview, key features, architecture diagram

### 2. SpecKit Repository
- **URL**: https://github.com/github/spec-kit
- **Filename**: `speckit-repository.png`
- **Resolution**: 1920x1080
- **Focus**: README, repository description, key features

## Capture Methods

### Method 1: Cline MCP Automation (Recommended)

1. Open Cline in VS Code
2. Verify MCP server active: Check `cline_mcp_settings.json` for `@srigi/mcp-webpage-screenshot`
3. Execute these prompts sequentially:

**Prompt 1**:
```
https://modelcontextprotocol.io/의 스크린샷을 1920x1080 해상도로 캡처하고 
v13.0_resources/part2/images/mcp-protocol-intro.png로 저장해주세요.
```

**Prompt 2**:
```
https://github.com/github/spec-kit의 스크린샷을 1920x1080 해상도로 캡처하고 
v13.0_resources/part2/images/speckit-repository.png로 저장해주세요.
```

### Method 2: Manual Capture (Fallback)

1. Open Chrome/Edge browser
2. Press F12 → Device Toolbar (Cmd+Shift+M on Mac)
3. Set custom resolution: 1920x1080
4. Navigate to URL
5. Scroll to show key content
6. Right-click → "Capture screenshot" or use extension
7. Save as PNG with specified filename

### Method 3: Playwright Script (Advanced)

```bash
# Install Playwright if not already installed
pnpm playwright install chromium

# Run capture script (create if needed)
node capture-screenshots.js
```

## Validation Checklist

After capture, verify:

- [ ] File exists at correct path
- [ ] PNG format
- [ ] 1920x1080 resolution
- [ ] File size < 2MB
- [ ] Clear, readable content
- [ ] No artifacts or cut-off elements

## Git Commit

Once validated:

```bash
git add v13.0_resources/part2/images/*.png
git commit -m "Add Part 2 MCP screenshots: protocol intro and SpecKit repo"
git push
```

## Documentation Update

After successful capture, update:

1. `v13.0_resources/part2/12_screenshot_descriptions.md` - Mark checklist items as [x]
2. `Context_and_Planning/demo-files/06-mcp-installation/screenshots-checklist.md` - Update Part 2 section
3. Add generation date and commit hash for traceability

---

**Created**: 2025-11-12
**Status**: Directory created, awaiting screenshot generation
