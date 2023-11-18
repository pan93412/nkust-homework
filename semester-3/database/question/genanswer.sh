#!/usr/bin/env bash
# -*- coding: utf-8 -*-

parallel -j 32 mysqlsh --result-format json/array --sql --host localhost --database mmisdb '<' '{}' '>' '{.}.ans' ::: *.sql
