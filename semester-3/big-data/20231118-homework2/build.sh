#!/usr/bin/env bash
# -*- coding: utf-8 -*-

echo "執行結果"
python3 docs/build.py
mv docs/example.pdf 執行結果.pdf

echo "心得報告"
TYPST_FONT_PATHS="$HOME/Library/Application Support/Adobe/CoreSync/plugins/livetype/.r/" typst compile docs/main.typ 心得報告.pdf

echo "程式碼"
git archive -o 程式碼.zip HEAD .
