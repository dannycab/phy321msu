#!/usr/bin/env python3
"""
Helper script to convert SVG files and export to PNG using Inkscape CLI.
Resizes to specified width and saves both SVG and PNG with the same name.
"""

import subprocess
import sys
import argparse
from pathlib import Path


def convert_svg(input_file, width, output_dir=None, trim=False):
    """
    Convert SVG to PNG and resize to specified width using Inkscape.

    Args:
        input_file: Path to input SVG file
        width: Width in pixels for output
        output_dir: Output directory (defaults to input file directory)
        trim: Whether to trim to content bounding box (no white edges)

    Returns:
        bool: True if successful, False otherwise
    """
    input_path = Path(input_file)

    if not input_path.exists():
        print(f"Error: File not found: {input_file}")
        return False

    if not input_path.suffix.lower() == '.svg':
        print(f"Error: File must be SVG format, got: {input_path.suffix}")
        return False

    # Use input directory if output_dir not specified
    if output_dir is None:
        output_dir = input_path.parent
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

    stem = input_path.stem

    # Paths for output files
    output_svg = output_dir / f"{stem}.svg"
    output_png = output_dir / f"{stem}.png"

    try:
        # Export to PNG with specified width
        png_cmd = [
            "inkscape",
            str(input_path),
            f"--export-type=png",
            f"--export-filename={output_png}",
            f"--export-width={width}",
        ]

        # Add trimming option if requested
        if trim:
            png_cmd.append("--export-area-drawing")
            print(f"Exporting PNG ({width}px width, trimmed to content) to: {output_png}")
        else:
            print(f"Exporting PNG ({width}px width) to: {output_png}")

        subprocess.run(png_cmd, check=True, capture_output=True)

        # Copy SVG to output directory if different
        if input_path != output_svg:
            import shutil
            print(f"Copying SVG to: {output_svg}")
            shutil.copy2(input_path, output_svg)

        print(f"✓ Successfully created:")
        print(f"  - {output_svg}")
        print(f"  - {output_png}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"Error running Inkscape: {e}")
        if e.stderr:
            print(f"stderr: {e.stderr.decode()}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Convert SVG to PNG using Inkscape CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python convert_svg.py diagram.svg 800
  python convert_svg.py diagram.svg 1200 -o output/
  python convert_svg.py images/graphic.svg 600
  python convert_svg.py diagram.svg 800 --trim
  python convert_svg.py diagram.svg 1200 -o output/ -t
        """
    )

    parser.add_argument("filename", help="Input SVG filename")
    parser.add_argument("width", type=int, help="Output width in pixels")
    parser.add_argument("-o", "--output", dest="output_dir",
                        help="Output directory (default: same as input file)")
    parser.add_argument("-t", "--trim", action="store_true",
                        help="Trim to content bounding box (remove white edges)")

    args = parser.parse_args()

    success = convert_svg(args.filename, args.width, args.output_dir, args.trim)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
