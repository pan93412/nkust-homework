from typing import Callable, Generic, ParamSpec, TypeVar


P = ParamSpec("P")
O = TypeVar("O")


def describe_fn(description: str) -> Callable[[Callable[P, O]], "FnDescriber[P, O]"]:
    """The decorator of FnDescriber."""
    return lambda fn: FnDescriber(fn, description)


class FnDescriber(Generic[P, O]):
    def __init__(self, fn: Callable[P, O], description: str):
        self.fn = fn
        self.desc = description

    def __repr__(self):
        return self.desc

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> O:
        return self.fn(*args, **kwargs)
