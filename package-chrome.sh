#!/bin/bash
# Package extension for Chrome Web Store

echo "📦 Packaging Takea-Sponsor-Away for Chrome Web Store..."

# Remove old package if it exists
rm -f takea-sponsor-away-chrome.zip

# Create the package
zip -r takea-sponsor-away-chrome.zip \
  manifest.json \
  content.js \
  styles.css \
  icons/ \
  -x "*.git*" \
  -x "*.DS_Store" \
  -x "*.md" \
  -x "*.sh" \
  -x "*.zip" \
  -x "*Gemini_Generated_Image*" \
  -x "LICENSE"

if [ $? -eq 0 ]; then
    echo "✅ Chrome package created: takea-sponsor-away-chrome.zip"
    echo "📊 Package contents:"
    unzip -l takea-sponsor-away-chrome.zip
    echo ""
    echo "🚀 Next steps:"
    echo "   1. Go to https://chrome.google.com/webstore/devconsole"
    echo "   2. Click 'New Item'"
    echo "   3. Upload takea-sponsor-away-chrome.zip"
else
    echo "❌ Error creating package"
    exit 1
fi

