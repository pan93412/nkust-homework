import json
from serializer.serializer import Serializer
from structures.response import Response


class JsonSerializer(Serializer[str]):
    def serialize_response(self, response: Response) -> str:
        return json.dumps(response.to_dict(), ensure_ascii=False, indent=4)
