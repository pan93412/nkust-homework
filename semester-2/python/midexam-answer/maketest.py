import os
import re
import shutil
import tempfile

from pathlib import Path

# copy test files
tmpdir = Path(tempfile.mkdtemp())
shutil.copytree(Path("."), tmpdir, dirs_exist_ok=True)

# parsing src
filename_regex = re.compile(r"(c\d{9})_(.+)_第(.)題.py")
number_map = {
    "一": "1",
    "ㄧ": "1",
    "二": "2",
    "三": "3",
    "四": "4",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4"
}

srcpath = Path("src")
for filename in os.listdir(srcpath):
    match = filename_regex.match(filename)
    if match:
        schid, name, question_number = match.groups()
        question_number = number_map[question_number]

        question_id = f"p{question_number}"

        shutil.copyfile(srcpath / filename, tmpdir / question_id / f"{question_id}.py")

os.system(f"pytest --html output.html {tmpdir.absolute()}")
