#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <markdown-file>"
    exit 1
fi

MARKDOWN_FILE=$1
THEME_PATH="../themes/"
THEME="king.css"

## Generate HTML Slides
marp --theme ${THEME_PATH}${THEME} --allow-local-files ${MARKDOWN_FILE}

## Generate PDF Slides
marp --theme ${THEME_PATH}${THEME} --allow-local-files --pdf ${MARKDOWN_FILE}

## Generate Cover Image
marp --theme ${THEME_PATH}${THEME} --allow-local-files --image png ${MARKDOWN_FILE}
