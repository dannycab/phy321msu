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

# Check if the notebook file exists
if [ ! -f "$NOTEBOOK_FILE" ]; then
    echo "Error: Notebook file '$NOTEBOOK_FILE' does not exist."
    exit 1
fi

# Convert Jupyter Notebook to HTML using nbconvert
jupyter nbconvert --execute --to html "$NOTEBOOK_FILE" --output "$HTML_FILE"

# Check if the HTML conversion was successful
if [ $? -eq 0 ]; then
    echo "HTML conversion successful: '$HTML_FILE' created."
else
    echo "Error: HTML conversion failed."
    exit 1
fi