#!/usr/bin/env bash

rm -r dist
mkdir dist
parallel --progress --bar typst compile --root "{}" "{}/main.typ" "dist/{}.pdf" ::: *
