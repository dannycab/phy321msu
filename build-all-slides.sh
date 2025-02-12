#!/bin/bash

SLIDE_PATH="../slides/"
THEME_PATH="../themes/"
THEME="graph_paper.css"

# This script is used to generate the list of all the files in the repository
# and convert them to PDF using the specified theme.

# # Generate slides with the specified theme
marp --theme ${THEME_PATH}${THEME} --allow-local-files ../slides
if [ $? -ne 0 ]; then
    echo "Failed to generate slides with theme ${THEME_PATH}${THEME}"
    exit 1
fi

# Generate PDF from slides with the specified theme
marp --theme ${THEME_PATH}${THEME} --allow-local-files --pdf ../slides
if [ $? -ne 0 ]; then
    echo "Failed to generate PDF from slides with theme ${THEME_PATH}${THEME}"
    exit 1
fi

# Generate cover image from slides with the specified theme
marp --theme ${THEME_PATH}${THEME} --allow-local-files --image png ../slides
if [ $? -ne 0 ]; then
    echo "Failed to generate cover image from slides with theme ${THEME_PATH}${THEME}"
    exit 1
fi