import json

json_text = """
    {
        "hello": 1
    }
"""

json_object = json.loads(json_text)
print(json_object)