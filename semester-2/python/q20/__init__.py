from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def food(self):
        pass


class Cat(Animal):
    def sound(self):
        return 'meow'

    def food(self):
        return 'cat eating'

class Dog(Animal):
    def sound(self):
        return 'woof'

    def food(self):
        return 'dog eating'
