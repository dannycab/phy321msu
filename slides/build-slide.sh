#!/bin/bash

# Check if the number of arguments passed to the script is exactly 1
if [ "$#" -ne 1 ]; then
    # If not, print the usage message and exit with status code 1 (indicating an error)
    echo "Usage: $0 <markdown-file>"
    exit 1
fi

# Assign the first argument passed to the script to the variable MARKDOWN_FILE
MARKDOWN_FILE=$1

# Define the path to the directory containing the theme files
THEME_PATH="../themes/"

# Define the name of the theme file to be used
THEME="king.css"

## Generate HTML Slides
# The following would generate HTML slides from the markdown file using the specified theme.
# marp --theme ${THEME_PATH}${THEME} --allow-local-files ${MARKDOWN_FILE}

## Generate PDF Slides
# This command generates PDF slides from the markdown file using the specified theme.
marp --theme ${THEME_PATH}${THEME} --allow-local-files --pdf ${MARKDOWN_FILE}

## Generate Cover Image
# This command generates a cover image (in PNG format) from the markdown file using the specified theme.
marp --theme ${THEME_PATH}${THEME} --allow-local-files --image png ${MARKDOWN_FILE}