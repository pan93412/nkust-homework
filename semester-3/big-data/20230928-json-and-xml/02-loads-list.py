import json

json_text = """
    [
        {
            "hello": 1
        },
        {
            "hello": 2
        }
    ]
"""

if __name__ == '__main__':
    print(json.loads(json_text))