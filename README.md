# Takea-Sponsor-Away

A Chrome/Chromium browser extension that automatically removes sponsored products on Takealot.com.

## Features

- Automatically detects and removes all sponsored products from Takealot
- Completely removes sponsored products from the page (no empty spaces left behind)
- Works on search results, category pages, and other product listings
- Monitors for dynamically loaded content (infinite scroll, etc.)
- Smooth fade-out animation when removing products
- Lightweight and fast
- No configuration needed - just install and browse

## Installation

## Usage

Once installed, the extension works automatically:

1. Visit [Takealot.com](https://www.takealot.com/)
2. Browse or search for products
3. Sponsored products will be automatically removed from the page with a smooth fade-out effect
4. Check the browser console (F12) to see how many sponsored products were removed

## How It Works

The extension uses:
- **Content Script**: Scans the page for elements containing "Sponsored" tags and completely removes them from the DOM
- **MutationObserver**: Monitors for dynamically loaded content to catch newly added sponsored products
- **No Empty Spaces**: Products are completely removed from the page, so other products fill the space automatically

## Compatibility

- Chrome (version 88+)
- Microsoft Edge (version 88+)
- Brave
- Other Chromium-based browsers supporting Manifest V3

## Privacy

This extension:
- Does NOT collect any data
- Does NOT track your browsing
- Does NOT send any information to external servers
- Only runs on Takealot.com pages

## Files

- `manifest.json` - Extension configuration
- `content.js` - Main script that detects and hides sponsored products
- `styles.css` - Styling rules for hiding elements
- `icons/` - Extension icons
- `README.md` - This file

## Version History

- **1.0.0** - Initial release
  - Automatic hiding of sponsored products
  - Dynamic content monitoring
  - Support for Chrome/Chromium browsers

