from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from structures.response import Response

O = TypeVar("O")


class Serializer(Generic[O], ABC):
    @abstractmethod
    def serialize_response(self, response: Response) -> O:
        pass
