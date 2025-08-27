#!/usr/bin/env python3

"""
Simple Marp slide builder that just works.
Usage: python3 build-slide-simple.py slides/day-01-introduction.md
"""

import os
import subprocess
import sys

def build_slide(markdown_file):
    """Build a single slide deck using Marp CLI."""
    
    # Get the absolute paths
    markdown_path = os.path.abspath(markdown_file)
    slides_dir = os.path.dirname(markdown_path)
    base_name = os.path.splitext(os.path.basename(markdown_path))[0]
    
    # Output files
    html_output = os.path.join(slides_dir, f"{base_name}.html")
    
    # Check if markdown file exists
    if not os.path.exists(markdown_path):
        print(f"Error: {markdown_path} does not exist")
        return False
    
    # Simple marp command - run from the slides directory
    cmd = [
        "marp",
        "--allow-local-files",
        "--html",
        "--output", html_output,
        os.path.basename(markdown_path)
    ]
    
    print(f"Building slide: {markdown_file}")
    print(f"Command: {' '.join(cmd)}")
    print(f"Working directory: {slides_dir}")
    
    try:
        # Run marp from the slides directory
        result = subprocess.run(
            cmd,
            cwd=slides_dir,
            capture_output=True,
            text=True,
            check=True
        )
        
        print(f"✓ Successfully built: {html_output}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Error building slide:")
        print(f"  Return code: {e.returncode}")
        print(f"  STDOUT: {e.stdout}")
        print(f"  STDERR: {e.stderr}")
        return False
    except FileNotFoundError:
        print("✗ Error: 'marp' command not found. Please install Marp CLI:")
        print("  npm install -g @marp-team/marp-cli")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 build-slide-simple.py <markdown-file>")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    success = build_slide(markdown_file)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
