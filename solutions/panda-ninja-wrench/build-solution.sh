#!/bin/bash

# Check if exactly one argument is passed
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <notebook-name-without-extension>"
    exit 1
fi

# Assign the argument to a variable
NOTEBOOK_NAME=$1

# Remove .ipynb or .pdf extension if present
if [[ "$NOTEBOOK_NAME" == *.ipynb ]]; then
    echo "Warning: Removing .ipynb extension from input"
    NOTEBOOK_NAME="${NOTEBOOK_NAME%.ipynb}"
elif [[ "$NOTEBOOK_NAME" == *.pdf ]]; then
    echo "Warning: Removing .pdf extension from input"
    NOTEBOOK_NAME="${NOTEBOOK_NAME%.pdf}"
fi

# Define the notebook and output file names
NOTEBOOK_FILE="${NOTEBOOK_NAME}.ipynb"
OUTPUT_FILE="${NOTEBOOK_NAME}.pdf"

# Check if the notebook file exists
if [ ! -f "$NOTEBOOK_FILE" ]; then
    echo "Error: Notebook file '$NOTEBOOK_FILE' does not exist."
    exit 1
fi

# Check if the template file exists
TEMPLATE_FILE="template.tex"
if [ ! -f "$TEMPLATE_FILE" ]; then
    echo "Warning: Template file '$TEMPLATE_FILE' does not exist. Running basic conversion."
    # Convert Jupyter Notebook to PDF using pandoc and xelatex without the template
    pandoc "$NOTEBOOK_FILE" --output "$OUTPUT_FILE" --pdf-engine=xelatex --pdf-engine-opt=-shell-escape
else
    # Convert Jupyter Notebook to PDF using pandoc, xelatex, and the custom template
    pandoc "$NOTEBOOK_FILE" --output "$OUTPUT_FILE" --pdf-engine=xelatex --template="$TEMPLATE_FILE" --pdf-engine-opt=-shell-escape
fi

# Check if the conversion was successful
if [ $? -eq 0 ]; then
    echo "Conversion successful: '$OUTPUT_FILE' created."
else
    echo "Error: Conversion failed."
    exit 1
fi