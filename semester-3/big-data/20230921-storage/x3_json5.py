from typing import TypedDict, cast

import json5

d = """
{
    // JSON5 支援註解
    "name": "John",
    // 以及末尾 comma
    "age": 19,
}
"""


class Structure(TypedDict):
    name: str
    age: int


if __name__ == "__main__":
    # deserialize JSON5
    deserialized_object = cast(Structure, json5.loads(d))

    # print result
    print(f"{deserialized_object['name']} is {deserialized_object['age']} years old")
