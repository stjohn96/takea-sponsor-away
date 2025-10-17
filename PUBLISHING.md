# Publishing Guide

This guide will walk you through publishing the Takea-Sponsor-Away extension to both the Chrome Web Store and Firefox Add-ons.

## Prerequisites

### Chrome Web Store
- A Google account
- One-time developer registration fee: $5 USD
- Register at: https://chrome.google.com/webstore/devconsole

### Firefox Add-ons
- A Firefox account (free)
- Register at: https://addons.mozilla.org/developers/

## Packaging for Chrome Web Store

### 1. Create the Package

The Chrome Web Store accepts a ZIP file containing all extension files. Create it using the provided Python script:

```bash
# From the project root directory
python3 package-chrome.py
```

Or if you have `zip` command available:
```bash
./package-chrome.sh
```

**What to include:**
- `manifest.json`
- `content.js`
- `styles.css`
- `icons/` directory (all icon files)

**What to exclude:**
- `.git` directory
- `.md` files (README, INSTALL, etc.) - these go in the store listing
- Image sources
- Development files

### 2. Upload to Chrome Web Store

1. Go to [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore/devconsole)
2. Pay the $5 one-time registration fee (if not already registered)
3. Click "New Item"
4. Upload your `takea-sponsor-away-chrome.zip` file
5. Fill in the store listing:
   - **Name:** Takea-Sponsor-Away
   - **Summary:** Automatically removes sponsored products on Takealot.com
   - **Description:** Use content from README.md
   - **Category:** Shopping
   - **Language:** English
   - **Icons:** Upload the icon files (128x128 required)
   - **Screenshots:** Create 1-5 screenshots showing the extension in action (1280x800 or 640x400)
   - **Promotional images:** Optional but recommended
   - **Privacy practices:** Select "Does not collect user data"

6. Set pricing to "Free"
7. Select distribution: "Public" or "Unlisted"
8. Submit for review

**Review Process:**
- Typically takes a few hours to a few days
- You'll receive an email when approved or if changes are needed

## Packaging for Firefox Add-ons

### 1. Create the Package

Firefox accepts a ZIP file (`.zip`) or signed XPI file. For initial submission, use ZIP:

```bash
# From the project root directory
python3 package-firefox.py
```

Or if you have `zip` command available:
```bash
./package-firefox.sh
```

**Important:** The package contents should be identical to Chrome's package:
- `manifest.json` (already configured for both browsers)
- `content.js`
- `styles.css`
- `icons/` directory

### 2. Upload to Firefox Add-ons

1. Go to [Firefox Add-ons Developer Hub](https://addons.mozilla.org/developers/)
2. Sign in with your Firefox account (free, no registration fee)
3. Click "Submit a New Add-on"
4. Choose "On this site" (listed on AMO)
5. Upload your `takea-sponsor-away-firefox.zip` file
6. Fill in the listing details:
   - **Name:** Takea-Sponsor-Away
   - **Summary:** Automatically removes sponsored products on Takealot.com (max 250 chars)
   - **Description:** Use content from README.md
   - **Categories:** Shopping
   - **Support email:** Your email
   - **Support website:** GitHub repo URL
   - **License:** Same as your repo (check LICENSE file)
   - **Privacy Policy:** "This extension does not collect any user data"
   - **Icons:** Already included in the ZIP
   - **Screenshots:** Upload 1-5 screenshots

7. **Source Code Submission:**
   - If your code is exactly what's in the ZIP (no build process), select "No"
   - If you use build tools, you may need to submit source code

8. **Version Notes:** Describe what's in this version
9. Submit for review

**Review Process:**
- Firefox has a more thorough manual review process
- Typically takes 1-7 days
- Reviewers may ask questions or request changes
- Once approved, it's automatically signed and published

## Version Updates

When releasing updates:

1. **Update version in manifest.json:**
   ```json
   "version": "1.1.0"
   ```

2. **Create new packages** for both Chrome and Firefox

3. **Upload to respective stores:**
   - Chrome: Upload new ZIP in the same item
   - Firefox: Create new version submission

4. **Include version notes** describing what changed

## Best Practices

### Screenshots
Create high-quality screenshots showing:
1. Extension in action (sponsored products being removed)
2. Before/after comparison
3. Extension working on different Takealot pages

Recommended tools:
- Use browser's built-in screenshot tool (F12 > Device toolbar for consistent sizing)
- Annotate with arrows/highlights to show what's happening
- Keep text readable

### Store Listing Optimization
- Use clear, concise language
- Highlight key features (instant removal, no data collection, etc.)
- Include keywords: "Takealot", "sponsored", "ad blocker", "shopping"
- Add "South Africa" since Takealot is SA-specific

### Privacy & Permissions
Both stores are strict about privacy:
- Clearly state you don't collect data
- Only request necessary permissions
- Our extension only needs `host_permissions` for takealot.com

## Promotional Images (Optional)

### Chrome Web Store Promotional Tile
- Small: 440x280 PNG
- Large: 920x680 PNG or 1400x560 PNG

### Firefox Add-ons
- No specific promotional images required
- Good screenshots are enough

## Post-Publication

### Chrome Web Store
- Your extension will be at: `https://chrome.google.com/webstore/detail/[extension-id]`
- Track stats in the Developer Dashboard
- Respond to user reviews

### Firefox Add-ons
- Your extension will be at: `https://addons.mozilla.org/firefox/addon/takea-sponsor-away/`
- Track stats in the Developer Hub
- Respond to user reviews

## Troubleshooting

### Common Issues

**Chrome Web Store:**
- **"Manifest version not supported":** Make sure you're using Manifest V3
- **"Icons missing":** Ensure all icon sizes are included
- **"Policy violation":** Ensure privacy practices are accurate

**Firefox Add-ons:**
- **"Invalid extension ID":** Check `browser_specific_settings.gecko.id` in manifest
- **"Manifest errors":** Validate your manifest.json
- **"Source code required":** Our extension has no build process, so just ZIP should be fine

### Validation Tools

**Before submitting:**
- Test in both browsers thoroughly
- Use Firefox's `about:debugging` to test loading
- Use Chrome's `chrome://extensions/` in developer mode

## Support

If you encounter issues:
- **Chrome:** [Chrome Web Store Support](https://support.google.com/chrome_webstore/)
- **Firefox:** [Add-ons Support](https://extensionworkshop.com/documentation/publish/)

## Automation (Future)

Consider using `web-ext` for Firefox automation:
```bash
npm install -g web-ext
web-ext build
web-ext sign --api-key=... --api-secret=...
```

For Chrome, manual upload is required (no CLI tool for publishing).

