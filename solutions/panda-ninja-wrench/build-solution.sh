#!/bin/bash

# Check if at least one argument is passed
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <notebook-name-without-extension>"
    exit 1
fi

# Assign the first argument to a variable
NOTEBOOK_NAME=$1

# Remove .ipynb extension if present
if [[ "$NOTEBOOK_NAME" == *.ipynb ]]; then
    echo "Warning: Removing .ipynb extension from input"
    NOTEBOOK_NAME="${NOTEBOOK_NAME%.ipynb}"
fi

# Define the notebook and output file names
NOTEBOOK_FILE="${NOTEBOOK_NAME}.ipynb"
HTML_FILE="${NOTEBOOK_NAME}.html"
TEMP_NOTEBOOK_FILE="${NOTEBOOK_NAME}_temp.ipynb"

# Check if the notebook file exists
if [ ! -f "$NOTEBOOK_FILE" ]; then
    echo "Error: Notebook file '$NOTEBOOK_FILE' does not exist."
    exit 1
fi

# Remove the fencing from the notebook using a Python script
python3 - <<EOF
import json

with open("$NOTEBOOK_FILE", "r") as f:
    notebook = json.load(f)

for cell in notebook["cells"]:
    if cell["cell_type"] == "markdown":
        new_source = []
        in_admonition = False
        for line in cell["source"]:
            if line.startswith("::{admonition} SOLUTION :class: hint") or line.startswith("```"):
                in_admonition = True
            elif line.startswith(":::") or line.startswith("```"):
                in_admonition = False
            elif not in_admonition:
                new_source.append(line)
        cell["source"] = new_source

with open("$TEMP_NOTEBOOK_FILE", "w") as f:
    json.dump(notebook, f, indent=1)
EOF

# Convert the modified notebook to HTML using nbconvert
jupyter nbconvert --execute --to html "$TEMP_NOTEBOOK_FILE" --output "$HTML_FILE"

# Check if the HTML conversion was successful
if [ $? -eq 0 ]; then
    echo "HTML conversion successful: '$HTML_FILE' created."
    # Remove the temporary notebook file
    rm "$TEMP_NOTEBOOK_FILE"
else
    echo "Error: HTML conversion failed."
    # Remove the temporary notebook file
    rm "$TEMP_NOTEBOOK_FILE"
    exit 1
fi