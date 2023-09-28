import io
import json
from typing import TextIO


class DictReader(io.TextIOBase):
    brace_begin = False

    def __init__(self, io: TextIO):
        self.io = io

    def read(self, __size: int | None = None) -> str:
        output = ""
        stack = []

        for s in self.io.read(__size):
            match s:
                case '{':
                    stack.append(s)
                    output += s
                case '}' if len(stack) == 1:  # final
                    return output + s
                case '}':
                    stack.pop()
                    output += s
                case _ if len(stack) != 0:
                    output += s

        return output

    def __getattr__(self, item):
        return getattr(self.io, item)


if __name__ == '__main__':
    with open("03-write-to-file.txt", "r") as f:
        nf = DictReader(f)
        data = json.load(nf)

        print(data)
        print(type(data))
