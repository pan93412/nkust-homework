from typing import Callable, Generic, TypeVar


I1 = TypeVar("I1")
O = TypeVar("O")

class FnDescriber1(Generic[I1, O]):
    def __init__(self, fn: Callable[[I1], O], description: str):
        self.fn = fn
        self.desc = description

    def __repr__(self):
        return self.desc

    def __call__(self, i: I1) -> O:
        return self.fn(i)
