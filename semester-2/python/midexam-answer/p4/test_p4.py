from .p4 import AnotherBase, Derived


class TestAnotherBase:
    def test_foo2(self):
        assert AnotherBase().foo2() == "woo"


class TestDerived:
    def test_foo2(self):
        assert Derived().foo2() == "wooooooooooooo"
