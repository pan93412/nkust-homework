from typing import Literal


class Person:
    def __init__(self, na: str):
        self.name = na

    def print_name(self):
        print(self.name)

class Student(Person):
    def __init__(self, name: str, gender: Literal["male", "female", "other"]):
        super().__init__(name)
        self.gender = gender

    def print_info(self):
        self.print_name()
        print(self.gender)
