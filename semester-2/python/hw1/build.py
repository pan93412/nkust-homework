import os
import sys


EMBED_CMD = "//embed: "
RUN_CMD = "//run: "
OUT_FILENAME = "main_embed.typ"
COMPILE_CMD = f"typst compile {OUT_FILENAME}"

new_typ = []

with open("main.typ") as f:
    for line in f.readlines():
        # embed the content of file to the main.typ
        if line.startswith(EMBED_CMD):
            filename = line[len(EMBED_CMD):].strip()
            with open(filename) as f:
                new_typ.extend(f.readlines())

        # run the command and write the result
        elif line.startswith(RUN_CMD):
            cmd = line[len(RUN_CMD):].strip()
            with os.popen(cmd) as process:
                response = process.read()

                if response != "":
                    new_typ.append(response)
                else:
                    new_typ.append("無輸出。")

        else:
            new_typ.append(line)

with open(OUT_FILENAME, "w") as f:
    f.write("".join(new_typ))

if len(sys.argv) > 1 and sys.argv[1] == "--compile":
    os.system(COMPILE_CMD)
else:
    print(f"run `{COMPILE_CMD}`!")
