from q7 import BoundedStack
import pytest


class TestBoundedStack:
    maxsize = 10

    def test_init(self):
        BoundedStack(self.maxsize)

    def test_push(self):
        s = BoundedStack(self.maxsize)

        with pytest.raises(Exception):
            for i in range(self.maxsize + 1):
                s.push(i)

    def test_pop(self):
        s = BoundedStack(self.maxsize)

        s.push(1)
        assert s.pop() == 1

        with pytest.raises(Exception):
            s.pop()

    def test_isempty(self):
        s = BoundedStack(self.maxsize)
        assert len(s) == 0

        s.push(1)
        assert len(s) == 1
