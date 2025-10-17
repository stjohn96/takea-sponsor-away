# Takea-Sponsor-Away

A browser extension for Chrome, Firefox, and other Chromium-based browsers that automatically removes sponsored products on Takealot.com.

## Features

- Automatically detects and removes all sponsored products from Takealot
- Completely removes sponsored products from the page (no empty spaces left behind)
- Works on search results, category pages, and other product listings
- Monitors for dynamically loaded content (infinite scroll, etc.)
- Instant removal (no animations)
- Lightweight and fast
- No configuration needed - just install and browse
- Works on both Chrome and Firefox

## Installation

### Chrome / Chromium Browsers

1. Download or clone this repository
2. Open Chrome and navigate to `chrome://extensions/`
3. Enable "Developer mode" (toggle in the top right)
4. Click "Load unpacked"
5. Select the extension directory
6. The extension icon should appear in your toolbar

### Firefox

1. Download or clone this repository
2. Open Firefox and navigate to `about:debugging#/runtime/this-firefox`
3. Click "Load Temporary Add-on..."
4. Navigate to the extension directory and select `manifest.json`
5. The extension will be loaded (note: temporary add-ons are removed when Firefox restarts)

**For permanent installation in Firefox:**
- The extension needs to be signed by Mozilla or you need to use Firefox Developer Edition/Nightly with `xpinstall.signatures.required` set to `false` in `about:config`

## Usage

Once installed, the extension works automatically:

1. Visit [Takealot.com](https://www.takealot.com/)
2. Browse or search for products
3. Sponsored products will be automatically removed from the page instantly
4. Check the browser console (F12) to see how many sponsored products were removed

## How It Works

The extension uses:
- **Content Script**: Scans the page for elements containing "Sponsored" tags and completely removes them from the DOM
- **MutationObserver**: Monitors for dynamically loaded content to catch newly added sponsored products
- **No Empty Spaces**: Products are completely removed from the page, so other products fill the space automatically

## Compatibility

- **Firefox** (version 109+)
- **Chrome** (version 88+)
- **Microsoft Edge** (version 88+)
- **Brave**
- **Opera**
- Other Chromium-based browsers supporting Manifest V3

## Privacy

This extension:
- Does NOT collect any data
- Does NOT track your browsing
- Does NOT send any information to external servers
- Only runs on Takealot.com pages

## Publishing

Want to publish this extension to the Chrome Web Store or Firefox Add-ons? See [PUBLISHING.md](PUBLISHING.md) for detailed instructions.

**Quick start:**
```bash
# Package for Chrome
python3 package-chrome.py

# Package for Firefox
python3 package-firefox.py
```

## Files

- `manifest.json` - Extension configuration
- `content.js` - Main script that detects and hides sponsored products
- `styles.css` - Styling rules for hiding elements
- `icons/` - Extension icons
- `package-chrome.py` - Script to create Chrome Web Store package
- `package-firefox.py` - Script to create Firefox Add-ons package
- `PUBLISHING.md` - Complete publishing guide
- `README.md` - This file

## Version History

- **1.0.0** - Initial release
  - Automatic removal of sponsored products
  - Dynamic content monitoring
  - Instant removal (no animations)
  - Support for Chrome, Firefox, and other Chromium-based browsers

