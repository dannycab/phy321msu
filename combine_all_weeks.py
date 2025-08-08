#!/usr/bin/env python3
"""
Script to combine ALL week start and notes files into single files outside the week directories.
Updates image paths from ../../ to ../ when moving files.
"""

import os
import json
import re
from pathlib import Path

def read_notebook(filepath):
    """Read a notebook file and return its content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def read_markdown(filepath):
    """Read a markdown file and return its content as a list of lines."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def update_image_paths(content):
    """Update image paths from ../../ to ../"""
    if isinstance(content, list):
        # For notebook cells (list of strings)
        return [re.sub(r'\.\./\.\./images/', '../images/', line) for line in content]
    elif isinstance(content, str):
        # For individual lines or markdown content (string)
        return re.sub(r'\.\./\.\./images/', '../images/', content)
    else:
        return content

def combine_notebooks(start_file, notes_file, output_file):
    """Combine two notebook files into one."""
    start_nb = read_notebook(start_file)
    notes_nb = read_notebook(notes_file)
    
    # Create combined notebook
    combined_nb = {
        "cells": [],
        "metadata": start_nb.get("metadata", {}),
        "nbformat": start_nb.get("nbformat", 4),
        "nbformat_minor": start_nb.get("nbformat_minor", 4)
    }
    
    # Add cells from start file
    for cell in start_nb.get("cells", []):
        if "source" in cell:
            cell["source"] = update_image_paths(cell["source"])
        combined_nb["cells"].append(cell)
    
    # Add a separator cell
    separator_cell = {
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": ["---", "", "# Lecture Notes", ""]
    }
    combined_nb["cells"].append(separator_cell)
    
    # Add cells from notes file
    for cell in notes_nb.get("cells", []):
        if "source" in cell:
            cell["source"] = update_image_paths(cell["source"])
        combined_nb["cells"].append(cell)
    
    # Write combined notebook
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(combined_nb, f, indent=2)

def combine_markdown_files(start_file, notes_file, output_file):
    """Combine two markdown files into one."""
    start_content = read_markdown(start_file)
    notes_content = read_markdown(notes_file)
    
    # Update image paths for each line
    start_content_updated = []
    for line in start_content:
        start_content_updated.append(update_image_paths(line))
    
    notes_content_updated = []
    for line in notes_content:
        notes_content_updated.append(update_image_paths(line))
    
    # Combine content
    combined_content = start_content_updated + ["", "---", "", "# Lecture Notes", ""] + notes_content_updated
    
    # Write combined file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(combined_content))

def process_week(week_num):
    """Process a single week's files."""
    week_dir = Path(f"lecture-notes/week{week_num}")
    output_dir = Path("lecture-notes")
    
    if not week_dir.exists():
        print(f"Week {week_num} directory does not exist: {week_dir}")
        return False
    
    # Find start and notes files
    start_files = list(week_dir.glob(f"{week_num:02d}_start.*"))
    notes_files = list(week_dir.glob(f"{week_num:02d}_notes.*"))
    
    if not start_files:
        print(f"No {week_num:02d}_start file found in week{week_num} directory")
        return False
    
    if not notes_files:
        print(f"No {week_num:02d}_notes file found in week{week_num} directory")
        return False
    
    start_file = start_files[0]
    notes_file = notes_files[0]
    
    # Determine file extension
    if start_file.suffix == '.ipynb' and notes_file.suffix == '.ipynb':
        output_file = output_dir / f"{week_num:02d}_notes.ipynb"
        combine_notebooks(start_file, notes_file, output_file)
        print(f"Combined notebooks: {start_file} + {notes_file} -> {output_file}")
    elif start_file.suffix == '.md' and notes_file.suffix == '.md':
        output_file = output_dir / f"{week_num:02d}_notes.md"
        combine_markdown_files(start_file, notes_file, output_file)
        print(f"Combined markdown files: {start_file} + {notes_file} -> {output_file}")
    else:
        print(f"Mixed file types not supported for week {week_num}: {start_file.suffix} and {notes_file.suffix}")
        return False
    
    return True

def main():
    """Process all weeks 3-13."""
    weeks_to_process = range(3, 14)  # weeks 3 through 13
    successful_weeks = []
    failed_weeks = []
    
    print("Processing all week files...")
    print("=" * 50)
    
    for week_num in weeks_to_process:
        if process_week(week_num):
            successful_weeks.append(week_num)
        else:
            failed_weeks.append(week_num)
    
    print("=" * 50)
    print(f"Successfully processed weeks: {successful_weeks}")
    if failed_weeks:
        print(f"Failed to process weeks: {failed_weeks}")
    
    print("\nImage paths updated from ../../ to ../")
    print("All applicable files combined successfully!")

if __name__ == "__main__":
    main()
