#!/usr/bin/env bash

shopt -s extglob

export TYPST_FONT_PATHS="$HOME/Library/Application Support/Adobe/CoreSync/plugins/livetype/.r/"

DIR_BASE_NAME=$(basename "$(pwd)")

parallel --progress typst compile {} "${DIR_BASE_NAME}_{.}.pdf" ::: !(template).typ
