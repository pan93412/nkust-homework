import os


EMBED_CMD = "//embed: "
RUN_CMD = "//run: "

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

with open("main_embed.typ", "w") as f:
    f.write("".join(new_typ))

print("run `typst compile main_embed.typ`!")
