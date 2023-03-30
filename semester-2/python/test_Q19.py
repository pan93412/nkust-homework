from unittest.mock import NonCallableMock, call, patch
from Q19 import Person, Student


class TestPerson:
    def test_init(self):
        assert Person('John').name == "John"

    @patch('builtins.print')
    def test_print_name(self, print: NonCallableMock):
        Person('John').print_name()

        print.assert_called_once_with('John')


class TestStudent:
    def test_init(self):
        s = Student('Alex', 'male')

        assert s.name == "Alex"
        assert s.gender == "male"

    @patch('builtins.print')
    def test_print_info(self, print: NonCallableMock):
        Student('Alex', 'male').print_info()

        assert call('Alex') in print.mock_calls
        assert call('male') in print.mock_calls
