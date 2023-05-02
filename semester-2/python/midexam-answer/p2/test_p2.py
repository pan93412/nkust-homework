import random

import pytest
from .p2 import Accountant, Person, Student

possible_genders = [
    "man",
    "female",
    "boy",
    "girl",
    "男生",
    "女生",
    "unknown",
    "不想透露",
    "trash bin",
]


def generate_construct_example():
    for _ in range(0, 10**3):
        p = [
            random.randint(0, 200),
            random.choice(["Student", "Accountant"]),
            random.choice(possible_genders),
        ]

        yield pytest.param(*p, id="age,career,gender")


def generate_construct_child_example():
    for _ in range(0, 10**3):
        p = [
            random.randint(0, 200),
            random.choice(possible_genders),
        ]

        yield pytest.param(*p, id="age,gender")


class MockPerson(Person):
    def getCareer(self):
        pass


class TestPerson:
    @pytest.mark.parametrize("age,career,gender", generate_construct_example())
    def test_construction(self, age: int, career: str, gender: str):
        # abstract method
        with pytest.raises(TypeError):
            Person(age=age, career=career, gender=gender)  # type:ignore

    @pytest.mark.parametrize("age,career,gender", generate_construct_example())
    def test_get_description(self, age: int, career: str, gender: str):
        assert (
            MockPerson(age, career, gender).getDescription()
            == f"I am {age}, {career}, {gender}"
        )


class TestStudent:
    @pytest.mark.parametrize("age,gender", generate_construct_child_example())
    def test_construction(self, age: int, gender: str):
        s = Student(age=age, gender=gender)

        assert s.age == age
        assert s.career == "Student"
        assert s.gender == gender

    @pytest.mark.parametrize("age,gender", generate_construct_child_example())
    def test_get_description(self, age: int, gender: str):
        assert (
            Student(age=age, gender=gender).getDescription()
            == f"I am a student, {age}, {gender}"
        )

    @pytest.mark.parametrize("age,gender", generate_construct_child_example())
    def test_get_person_description(self, age: int, gender: str):
        career = "Student"
        assert (
            Student(age, gender).getPersonDescription()
            == f"I am {age}, {career}, {gender}"
        )

    def test_get_career(self):
        s = Student(0, "")
        assert s.getCareer() == "Student"


class TestAccountant:
    @pytest.mark.parametrize("age,gender", generate_construct_child_example())
    def test_construction(self, age: int, gender: str):
        a = Accountant(age=age, gender=gender)

        assert a.age == age
        assert a.career == "Accountant"
        assert a.gender == gender

    def test_get_career(self):
        a = Accountant(0, "")
        assert a.getCareer() == "Accountant"
