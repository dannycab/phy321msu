#!/bin/bash

THEME_PATH="../slide_themes/"
THEME="nord.css"

# This script is used to generate the list of all the files in the repository

marp --theme ${THEME_PATH}${THEME} ../slides

marp --theme ${THEME_PATH}${THEME} ../slides --pdf