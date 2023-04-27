class Base:
    def __foo(self):
        pass


class AnotherBase:
    def foo2(self):
        return "woo"


class Derived(Base, AnotherBase):
    def foo2(self):
        return "wooooooooooooo"
