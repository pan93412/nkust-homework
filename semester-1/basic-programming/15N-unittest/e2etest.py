"""E2E Test framework"""

from typing import Any
import unittest
import unittest.mock as mock

import main as question1

class Question1Test(unittest.TestCase):
    def _execute(self, user_inputs: list[Any], stdout_response: list[Any]):
        with mock.patch("builtins.input", lambda _: user_inputs.pop()):
            with mock.patch("builtins.print", spec=print) as mocked_p:
                question1.main()
                print(mocked_p.call_args_list) # call_args_list = [12, 24, 36]
                assert mocked_p.call_args_list == [[str(v) for v in stdout_response]]

    def test_positive(self):
        return self._execute([30, 20, 10], [60])

    def test_negative(self):
        return self._execute([-30, -20, -10], [-60])

    def test_big_number(self) -> None:
        return self._execute([10**24, 10**48, 10**96], [1000000000000000000000000000000000000000000000001000000000000000000000001000000000000000000000000])

    def test_floats(self):
        return self._execute([1.11, 2.4356675, 3.1415926535], [6.6872601535000005])

    def test_random_order(self):
        return self._execute([37, 21, 63], [121])

if __name__ == '__main__':
    unittest.main()
