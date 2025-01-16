#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <markdown-file>"
    exit 1
fi

MARKDOWN_FILE=$1
THEME_PATH="../slide_themes/"
THEME="nord.css"

marp --theme ${THEME_PATH}${THEME} ${MARKDOWN_FILE}
marp --theme ${THEME_PATH}${THEME} ${MARKDOWN_FILE} --pdf