#!/usr/bin/env python3

"""
Working Marp slide builder that copies images alongside HTML.
Usage: python3 build-slide-working.py slides/day-01-introduction.md
"""

import os
import subprocess
import sys
import shutil

def build_slide_with_images(markdown_file):
    """Build slide and copy images to same directory as HTML."""
    
    # Get paths
    markdown_path = os.path.abspath(markdown_file)
    slides_dir = os.path.dirname(markdown_path)
    base_name = os.path.splitext(os.path.basename(markdown_path))[0]
    
    # Output file in slides directory
    html_output = os.path.join(slides_dir, f"{base_name}.html")
    
    # Build with marp
    cmd = [
        "marp",
        "--theme", "themes/graph_paper.css",
        "--allow-local-files",
        "--html", 
        "--output", html_output,
        markdown_file
    ]
    
    print(f"Building: {markdown_file}")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✓ HTML built: {html_output}")
        
        # Copy images directory to slides directory if it doesn't exist there
        images_source = os.path.join(slides_dir, "images")
        if os.path.exists(images_source):
            print(f"✓ Images already in slides directory: {images_source}")
        else:
            # Look for images in parent directory
            parent_images = os.path.join(os.path.dirname(slides_dir), "images")
            if os.path.exists(parent_images):
                print(f"→ Copying images from {parent_images} to {images_source}")
                shutil.copytree(parent_images, images_source)
            else:
                print(f"⚠ Warning: No images directory found")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Error: {e.stderr}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 build-slide-working.py <markdown-file>")
        sys.exit(1)
    
    if build_slide_with_images(sys.argv[1]):
        print("✓ Slide built successfully!")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
