from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, age: int, career: str, gender: str):
        self.age = age
        self.career = career
        self.gender = gender

    @abstractmethod
    def getCareer(self):
        pass

    def __record(self):
        return "hi"

    def getDescription(self):
        return f"I am {self.age}, {self.career}, {self.gender}"


class Student(Person):
    def __init__(self, age: int, gender: str):
        super().__init__(age, "Student", gender)

    def getCareer(self):
        return self.career

    def getDescription(self):
        return f"I am a student, {self.age}, {self.gender}"

    def getPersonDescription(self):
        return super().getDescription()


class Accountant(Person):
    def __init__(self, age: int, gender: str):
        super().__init__(age, "Accountant", gender)

    def getCareer(self):
        return self.career
