import json

import xmltodict

with open("05-xml-example.xml") as f:
    obj = xmltodict.parse(f.read())
    print(json.dumps(obj, indent=4, ensure_ascii=False))

    print(obj['school'])
    print(obj['school']['course']['title'])
    print(len(obj['school']['course']['participants']['student']))
