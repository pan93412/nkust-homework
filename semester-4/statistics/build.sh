#!/usr/bin/env bash

shopt -s extglob

export TYPST_FONT_PATHS="$HOME/Library/Application Support/Adobe/CoreSync/plugins/livetype/.r/"

rm -r dist
mkdir dist

parallel --progress --bar typst compile --root "{//}" {} "$(pwd)/dist/{//}_{/.}.pdf" ::: */!(template|typst-sympy-calculator).typ
