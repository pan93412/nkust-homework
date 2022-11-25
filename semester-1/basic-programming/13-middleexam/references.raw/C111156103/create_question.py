# License: AGPL-3.0-only

import shutil, sys

question_id = sys.argv[1]
fn = f"P{question_id}.py"

with open(fn, "w") as f:
    print(f"Writing file: {fn}")
    f.write(f"""'''Question {question_id}

Licensed under AGPL-3.0-only.'''

def main():
    pass

if __name__ == "__main__":
    main()
else:
    raise RuntimeError("Unexpected environment.")
""")
