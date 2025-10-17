#!/usr/bin/env python3
"""
Package extension for Firefox Add-ons
"""

import zipfile
import os
from pathlib import Path

# Files and directories to include
INCLUDE = [
    'manifest.json',
    'content.js',
    'styles.css',
    'icons/',
]

# Patterns to exclude
EXCLUDE_PATTERNS = [
    '.git',
    '.DS_Store',
    '.md',
    '.py',
    '.sh',
    '.zip',
    'Gemini_Generated_Image',
    'LICENSE',
    'PUBLISHING.md',
    'README.md',
    '__pycache__',
]

OUTPUT_FILE = 'takea-sponsor-away-firefox.zip'

def should_exclude(path):
    """Check if path should be excluded"""
    path_str = str(path)
    return any(pattern in path_str for pattern in EXCLUDE_PATTERNS)

def create_package():
    """Create Firefox Add-ons package"""
    print("📦 Packaging Takea-Sponsor-Away for Firefox Add-ons...")
    
    # Remove old package if exists
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    
    file_count = 0
    
    with zipfile.ZipFile(OUTPUT_FILE, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in INCLUDE:
            path = Path(item)
            
            if path.is_file():
                if not should_exclude(path):
                    zipf.write(path, path)
                    file_count += 1
                    print(f"  ✓ Added {path}")
            
            elif path.is_dir():
                for file_path in path.rglob('*'):
                    if file_path.is_file() and not should_exclude(file_path):
                        zipf.write(file_path, file_path)
                        file_count += 1
                        print(f"  ✓ Added {file_path}")
    
    print(f"\n✅ Firefox package created: {OUTPUT_FILE}")
    print(f"📊 Total files: {file_count}")
    
    # List contents
    print("\n📋 Package contents:")
    with zipfile.ZipFile(OUTPUT_FILE, 'r') as zipf:
        for info in zipf.filelist:
            print(f"   {info.filename} ({info.file_size} bytes)")
    
    print("\n🚀 Next steps:")
    print("   1. Go to https://addons.mozilla.org/developers/")
    print("   2. Click 'Submit a New Add-on'")
    print(f"   3. Upload {OUTPUT_FILE}")

if __name__ == '__main__':
    create_package()

