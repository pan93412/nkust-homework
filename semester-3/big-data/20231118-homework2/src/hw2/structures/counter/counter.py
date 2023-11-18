from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class Counter(ABC, Generic[T]):
    @abstractmethod
    def next(self) -> T:
        pass
