#!/usr/bin/env bash
# -*- coding: utf-8 -*-

pnpm build
name=$(jq -r ".name" package.json)
git archive HEAD --format=zip --output answers/"$name"-src.zip
cp README.md answers/"$name"/README.md
