#!/usr/bin/env bash
# -*- coding: utf-8 -*-

echo -ne '[' > index
for s in $(find . -name '*.sql' | sed -e 's,^\./,,' | sort -V); do
    printf '"%s",' "${s%.*}" >> index
done
echo -ne ']' >> index

# strip trailing comma
sed -i '' 's/,]$/]/' index
