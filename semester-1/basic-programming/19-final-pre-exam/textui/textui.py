'''TextUI / The TUI interface for Final Pre-Exam.'''

from abc import ABC, abstractmethod
from typing import Callable

# ABC is a Abstract Base Class (ABC).
#
# We abstract the common parts of a basic TUI interface.
class TextUi(ABC):
    '''
    Properties
    ==========

    loop: bool
        Should this interface be looped?
        By default, it is False.

    input_until_condition: (str) -> bool | None
        The end condition of ``input_until`` method.
        See ``input_until()`` for more information.
    '''
    loop: bool = False

    input_until_condition: Callable[[str], bool] | None = None

    # The delegation of ``input()` so we can replace
    # this instance to any other input easily.
    input: Callable[[str], str] = input

    def input_int(self, prompt: str = "") -> int:
        return int(self.input(prompt))

    def input_split(self, prompt: str = "") -> Callable[[str | None], list[str]]:
        '''The wrapper of ``input().split()``'''
        return lambda sep: input(prompt).split(sep)

    def input_exit(self, prompt: str = ""):
        '''The ``input()`` wrapper that will ``exit()``
        when the ``self.input_until_condition(input)`` fulfilled.'''
        i = self.input(prompt)

        if self.input_until_condition \
            and self.input_until_condition(i):
            exit()

        return i

    @abstractmethod
    def main(self) -> None:
        '''Main application.

        When ``loop == True``, it will be re-called
        until `exit()` has been called.
        '''
        pass

    def on_exit(self) -> None:
        '''The method that will be called when
        ``exit()`` has been called.'''
        pass

    def on_final(self) -> None:
        '''The method that will be called after all hooks
        (for example, 'on_exit')'''
        pass

    def __call__(self) -> None:
        try:
            while self.loop:
                self.main()
        except (SystemExit):
            self.on_exit()
        finally:
            self.on_final()
