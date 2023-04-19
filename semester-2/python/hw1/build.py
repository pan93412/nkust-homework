import os
import sys


EMBED_CMD = "//embed: "
RUN_CMD = "//run: "
CODEBLOCK_CMD = "//cb: "
OUT_FILENAME = "main_embed.typ"
COMPILE_CMD = f"typst compile {OUT_FILENAME}"

CODEBLOCK_TEMPLATE = """
#srcresult("{filename}")[
  #code[
    ```py3
{code}
    ```
  ]
][
  ```
{output}
  ```
]
""".strip()

new_typ = []

def embed(filename):
    with open(filename) as f:
        return f.readlines()

def run(cmd):
    with os.popen(cmd) as process:
        response = process.read()

        return response if response != "" else "無輸出。"

with open("main.typ") as f:
    for line in f.readlines():
        # embed the content of file to the main.typ
        if line.startswith(EMBED_CMD):
            filename = line[len(EMBED_CMD):].strip()
            new_typ.extend(embed(filename))

        # run the command and write the result
        elif line.startswith(RUN_CMD):
            cmd = line[len(RUN_CMD):].strip()
            new_typ.append(run(cmd))

        elif line.startswith(CODEBLOCK_CMD):
            filename = line[len(CODEBLOCK_CMD):].strip()

            new_typ.append(CODEBLOCK_TEMPLATE.format(
                filename=filename,
                code="".join(embed(filename)),
                output=run(f"python3 {filename}")
            ))

        else:
            new_typ.append(line)

with open(OUT_FILENAME, "w") as f:
    f.write("".join(new_typ))

if len(sys.argv) > 1 and sys.argv[1] == "--compile":
    os.system(COMPILE_CMD)
else:
    print(f"run `{COMPILE_CMD}`!")
