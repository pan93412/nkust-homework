#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import subprocess
from tempfile import NamedTemporaryFile, TemporaryFile


templates = """
= Homework 2's Run Result

== Command

```
{command}
```

== Logs

```
{stderr}
```

== CLI Output

Colors have been stripped.

```
{stdout}
```

== JSON Output

```json
{json}
```
"""


def escape_ansi(line):
    ansi_escape = re.compile(r"(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]")
    return ansi_escape.sub("", line)


cmd_to_execute = ["rye", "run", "python3", "src/hw2", "epage", "https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw"]
o = subprocess.run(cmd_to_execute, capture_output=True)

with open("output.json", "r") as output_json:
    renderred = templates.format(
            command=cmd_to_execute,
            stderr=escape_ansi(o.stderr.decode()).strip(),
            stdout=escape_ansi(o.stdout.decode()).strip(),
            json=output_json.read(),
        )

with NamedTemporaryFile("w") as f:
    f.write(renderred)
    f.flush()
    subprocess.run(["typst", "compile", f.name, "docs/example.pdf"])
