#!/usr/bin/env bash
# -*- coding: utf-8 -*-

parallel -j 32 mysqlsh --table --sql --host localhost --database mmisdb '<' '{}' '>' '{.}.ans' ::: *.sql
