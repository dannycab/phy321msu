#!/usr/bin/env python3
"""
build.py

A build script for the phy321msu book project. This script provides several
utility functions to build the book in different formats (HTML, PDF), update
content, deploy to GitHub Pages, and open the generated files for viewing.

Usage:
    python build.py [task]

Available tasks:
    pdf        Build the book as a PDF using Jupyter Book's pdflatex builder.
    web        Deploy the HTML build to GitHub Pages using ghp-import.
    update     Build the book as HTML (default builder).
    rebuild    Update notebook kernels and rebuild the book from scratch.
    viewhtml   Open the generated HTML index page in the default browser.
    viewpdf    Open the generated PDF in the default PDF viewer.
    all        Run a full build: rebuild, pdf, rebuild, and web (in order).

If no task is specified, 'rebuild' is run by default.
"""

import argparse
import subprocess
import sys
from pathlib import Path

BOOK_DIR = "."
BUILD_DIR = "/_build/html"
TEX_DIR = "/_build/latex"
PDF_FILE = "book.pdf"


def run(cmd):
    """
    Run a shell command and exit if it fails.

    Args:
        cmd (str): The shell command to execute.

    Returns:
        None

    Raises:
        SystemExit: If the command returns a non-zero exit code.
    """
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)


def pdf():
    """
    Build the book as a PDF using Jupyter Book's pdflatex builder.

    Returns:
        None
    """
    run(f"jupyter-book build {BOOK_DIR} --builder pdflatex")


def web():
    """
    Deploy the HTML build to GitHub Pages using ghp-import.

    Returns:
        None
    """
    run(f"ghp-import -n -p -f {BOOK_DIR}{BUILD_DIR}")


def update():
    """
    Build the book as HTML using the default Jupyter Book builder.

    Returns:
        None
    """
    run(f"jupyter-book build {BOOK_DIR}")


def rebuild():
    """
    Update notebook kernels and rebuild the book from scratch.

    This runs the 'update_kernels.py' script and then builds all pages.

    Returns:
        None
    """
    run(f"python {BOOK_DIR}/update_kernels.py")
    run(f"jupyter-book build --all {BOOK_DIR}")


def viewhtml():
    """
    Open the generated HTML index page in the default web browser.

    Returns:
        None
    """
    run(f"open {BOOK_DIR}{BUILD_DIR}/index.html")


def viewpdf():
    """
    Open the generated PDF file in the default PDF viewer.

    Returns:
        None
    """
    run(f"open {BOOK_DIR}{TEX_DIR}/{PDF_FILE}")


def all_tasks():
    """
    Run a full build and deployment sequence.

    This runs, in order:
        1. rebuild
        2. pdf
        3. rebuild
        4. web

    Returns:
        None
    """
    rebuild()
    pdf()
    rebuild()
    web()


def main():
    """
    Parse command-line arguments and execute the selected task.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(
        description="Build script for phy321msu book"
    )
    parser.add_argument(
        "task",
        nargs="?",
        default="rebuild",
        choices=["pdf", "web", "update", "rebuild", "viewhtml", "viewpdf", "all"],
        help="Task to run (default: rebuild)"
    )
    args = parser.parse_args()

    tasks = {
        "pdf": pdf,
        "web": web,
        "update": update,
        "rebuild": rebuild,
        "viewhtml": viewhtml,
        "viewpdf": viewpdf,
        "all": all_tasks,
    }

    tasks[args.task]()


if __name__ == "__main__":
    main()