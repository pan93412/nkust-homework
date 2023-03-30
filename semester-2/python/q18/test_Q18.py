from unittest.mock import NonCallableMock, call, patch
from q18 import Trunk


class TestTrunk:
    def test_init(self):
        Trunk(4, 'John', 'red')

    @patch('builtins.print')
    def test_show(self, print: NonCallableMock):
        t = Trunk(4, 'John', 'red')
        t.show()

        assert call('door=4') in print.mock_calls
        assert call('owner=John') in print.mock_calls
        assert call('color=red') in print.mock_calls
