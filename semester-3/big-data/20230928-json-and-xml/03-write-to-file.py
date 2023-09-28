import json
import tempfile

json_text = """
    [{
        "hello": 1
    },{
        "hello": "你好!"
    }]
"""

if __name__ == '__main__':
    json_object: dict

    # write json_text to a temporary file
    with tempfile.TemporaryFile("w+") as tf:
        tf.write(json_text)

        # loads the text from stream.
        tf.seek(0)
        json_object = json.load(tf)

    # write to another file, with indent and
    # unicode.
    with open("03-write-to-file.txt", "w") as outf:
        json.dump(json_object, outf, indent=4, ensure_ascii=False)
