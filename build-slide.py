#!/usr/bin/env python3

"""
build-slide.py

A script to build slides from a Markdown file using Marp.
Supports generating HTML, PDF, and PNG cover images with custom themes.

Usage:
    python build-slide.py <markdown_file> [options]

Options:
    -t, --theme-path   Path to the theme directory (default: ./themes/)
    --theme            Theme file name (default: graph_paper.css)
    -o, --output-dir   Output directory (default: same as source file)
    --html             Generate HTML slides only
    --pdf              Generate PDF slides only
    --image            Generate PNG cover image only
"""

import argparse
import os
import subprocess
import sys
import shutil

def run_marp(markdown_file, theme_path, theme, output_dir,
             build_html, build_pdf, build_image):
    """
    Run Marp CLI to generate slides in different formats.

    Args:
        markdown_file (str): Path to the Markdown file.
        theme_path (str): Directory containing the theme CSS.
        theme (str): Theme CSS file name.
        output_dir (str): Directory to output generated files.
        build_html (bool): Whether to generate HTML output.
        build_pdf (bool): Whether to generate PDF output.
        build_image (bool): Whether to generate PNG cover image.
    """
    # Get the base name of the markdown file (without extension)
    base_name = os.path.splitext(os.path.basename(markdown_file))[0]
    # Define output file paths for each format
    out_html = os.path.join(output_dir, f"{base_name}.html")
    out_pdf = os.path.join(output_dir, f"{base_name}.pdf")
    out_png = os.path.join(output_dir, f"{base_name}.png")

    # Build the theme argument for Marp CLI (use absolute path)
    theme_file = os.path.abspath(os.path.join(theme_path, theme))
    theme_arg = f"--theme {theme_file}"
    # Allow Marp to access local files
    allow_local = "--allow-local-files"
    
    # Copy images directory to output directory if it exists and is different
    source_dir = os.path.dirname(os.path.abspath(markdown_file))
    images_source = os.path.join(source_dir, "images")
    images_dest = os.path.join(output_dir, "images")
    
    if os.path.exists(images_source) and source_dir != output_dir:
        if os.path.exists(images_dest):
            shutil.rmtree(images_dest)
        shutil.copytree(images_source, images_dest)

    # Generate HTML output if requested
    if build_html:
        subprocess.run(
            f"marp {theme_arg} {allow_local} -o {os.path.abspath(out_html)} {os.path.basename(markdown_file)}",
            shell=True, check=True, cwd=os.path.dirname(os.path.abspath(markdown_file))
        )
    # Generate PDF output if requested
    if build_pdf:
        subprocess.run(
            f"marp {theme_arg} {allow_local} --pdf -o {os.path.abspath(out_pdf)} {os.path.basename(markdown_file)}",
            shell=True, check=True, cwd=os.path.dirname(os.path.abspath(markdown_file))
        )
    # Generate PNG cover image if requested
    if build_image:
        subprocess.run(
            f"marp {theme_arg} {allow_local} --image png -o {os.path.abspath(out_png)} {os.path.basename(markdown_file)}",
            shell=True, check=True, cwd=os.path.dirname(os.path.abspath(markdown_file))
        )

def main():
    """
    Parse command-line arguments and invoke Marp build process.
    """
    parser = argparse.ArgumentParser(
        description="Build slides from markdown using Marp."
    )
    parser.add_argument(
        "markdown_file",
        help="Path to the markdown file."
    )
    parser.add_argument(
        "-t", "--theme-path",
        default="./themes/",
        help="Path to theme directory."
    )
    parser.add_argument(
        "--theme",
        default="graph_paper.css",
        help="Theme file name."
    )
    parser.add_argument(
        "-o", "--output-dir",
        help="Output directory (default: same as source file)."
    )
    parser.add_argument(
        "--html",
        action="store_true",
        help="Generate HTML slides only."
    )
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="Generate PDF slides only."
    )
    parser.add_argument(
        "--image",
        action="store_true",
        help="Generate PNG cover image only."
    )

    args = parser.parse_args()

    # Check if the markdown file exists
    if not os.path.isfile(args.markdown_file):
        print(f"Error: File '{args.markdown_file}' does not exist.")
        sys.exit(1)

    # Determine output directory
    if args.output_dir:
        output_dir = args.output_dir
    else:
        # Default to the directory of the source markdown file
        output_dir = os.path.dirname(os.path.abspath(args.markdown_file))
    os.makedirs(output_dir, exist_ok=True)

    # If no specific build flag is set, generate all outputs
    if not (args.html or args.pdf or args.image):
        build_html = build_pdf = build_image = True
    else:
        build_html = args.html
        build_pdf = args.pdf
        build_image = args.image

    # Run Marp with the specified options
    run_marp(
        args.markdown_file,
        args.theme_path,
        args.theme,
        output_dir,
        build_html,
        build_pdf,
        build_image
    )

if __name__ == "__main__":
    main()