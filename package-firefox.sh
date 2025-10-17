#!/bin/bash
# Package extension for Firefox Add-ons

echo "📦 Packaging Takea-Sponsor-Away for Firefox Add-ons..."

# Remove old package if it exists
rm -f takea-sponsor-away-firefox.zip

# Create the package (same contents as Chrome)
zip -r takea-sponsor-away-firefox.zip \
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
    echo "✅ Firefox package created: takea-sponsor-away-firefox.zip"
    echo "📊 Package contents:"
    unzip -l takea-sponsor-away-firefox.zip
    echo ""
    echo "🚀 Next steps:"
    echo "   1. Go to https://addons.mozilla.org/developers/"
    echo "   2. Click 'Submit a New Add-on'"
    echo "   3. Upload takea-sponsor-away-firefox.zip"
else
    echo "❌ Error creating package"
    exit 1
fi

