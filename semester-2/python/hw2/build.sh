#!/usr/bin/env bash
# -*- coding: utf-8 -*-

for i in q1 q2 q3
do
    git archive HEAD $i --format=zip --output answers/$i-src.zip
    typst c $i/README.typ answers/$i-readme.pdf
done
