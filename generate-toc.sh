#!/usr/bin/env bash
# -*- coding: utf-8 -*-

pushd toc || exit $?
deno task run .. -o ../TOC.md || exit $?
popd || exit $?
