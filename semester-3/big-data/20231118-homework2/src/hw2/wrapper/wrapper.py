from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from structures.response import Response

T = TypeVar("T")


class Wrapper(ABC, Generic[T]):
    """Wrapper wraps an object into a response."""

    @abstractmethod
    def wrap(self, obj: T) -> Response:
        """Wrap an object into a response."""
        pass
