import random
from unittest.mock import MagicMock
from .p1 import Trapezoid
import pytest

POSITIVE = 0b1
NEGATIVE = 0b10
ZERO_ALLOWED = 0b100


def generate_random_number(mode: int) -> int:
    n = random.randint(
        -(10**24) if mode & NEGATIVE else -1,
        10**24 if mode & POSITIVE else 1,
    )

    if n == 0 and not mode & ZERO_ALLOWED:
        return generate_random_number(mode)

    return n


def generate_get_cases(mode=POSITIVE):
    for _ in range(0, 10**3):
        v = [
            generate_random_number(mode),
            generate_random_number(mode),
            generate_random_number(mode),
        ]

        yield pytest.param(*v, id="top,bottom,height")


def generate_set_positive_case():
    for _ in range(0, 10**3):
        yield pytest.param(generate_random_number(POSITIVE), id="value")


def generate_set_negative_case():
    for _ in range(0, 10**3):
        yield pytest.param(generate_random_number(NEGATIVE), id="value")


class TestTrapezoid:
    @pytest.mark.parametrize("top,bottom,height", generate_get_cases())
    def test_construction(self, top: int, bottom: int, height: int):
        trapezoid = Trapezoid(top=top, bottom=bottom, height=height)

        assert trapezoid.top == top
        assert trapezoid.bottom == bottom
        assert trapezoid.height == height

    def test_construction_not_positive(self):
        printer = MagicMock()
        trapezoid = Trapezoid(-1, -1, -1, printer)

        assert printer.call_count == 3
        assert trapezoid.top == 0
        assert trapezoid.bottom == 0
        assert trapezoid.height == 0

    @pytest.mark.parametrize("top,bottom,height", generate_get_cases())
    def test_get_top(self, top: int, bottom: int, height: int):
        trapezoid = Trapezoid(top, bottom, height)
        assert top == trapezoid.getTop()

    @pytest.mark.parametrize("top,bottom,height", generate_get_cases())
    def test_get_bottom(self, top: int, bottom: int, height: int):
        trapezoid = Trapezoid(top, bottom, height)
        assert bottom == trapezoid.getBottom()

    @pytest.mark.parametrize("top,bottom,height", generate_get_cases())
    def test_get_height(self, top: int, bottom: int, height: int):
        trapezoid = Trapezoid(top, bottom, height)
        assert height == trapezoid.getHeight()

    @pytest.mark.parametrize("value", generate_set_positive_case())
    def test_set_top_positive(self, value: int):
        printer = MagicMock()

        trapezoid = Trapezoid(0, 0, 0, printer)

        trapezoid.setTop(value)

        printer.assert_not_called()
        assert value == trapezoid.top

    @pytest.mark.parametrize("value", generate_set_positive_case())
    def test_set_bottom_positive(self, value: int):
        printer = MagicMock()

        trapezoid = Trapezoid(0, 0, 0, printer)

        trapezoid.setBottom(value)

        printer.assert_not_called()
        assert value == trapezoid.bottom

    @pytest.mark.parametrize("value", generate_set_positive_case())
    def test_set_height_positive(self, value: int):
        printer = MagicMock()

        trapezoid = Trapezoid(0, 0, 0, printer)

        trapezoid.setHeight(value)

        printer.assert_not_called()
        assert value == trapezoid.height

    @pytest.mark.parametrize("value", generate_set_negative_case())
    def test_set_top_negative(self, value: int):
        printer = MagicMock()

        trapezoid = Trapezoid(0, 0, 0, printer)

        trapezoid.setTop(value)

        printer.assert_called_once_with("Not a valid number. Fallback to 0.")
        assert trapezoid.top == 0

    @pytest.mark.parametrize("value", generate_set_negative_case())
    def test_set_bottom_negative(self, value: int):
        printer = MagicMock()

        trapezoid = Trapezoid(0, 0, 0, printer)

        trapezoid.setBottom(value)

        printer.assert_called_once_with("Not a valid number. Fallback to 0.")
        assert trapezoid.bottom == 0

    @pytest.mark.parametrize("value", generate_set_negative_case())
    def test_set_height_negative(self, value: int):
        printer = MagicMock()

        trapezoid = Trapezoid(0, 0, 0, printer)

        trapezoid.setHeight(value)

        printer.assert_called_once_with("Not a valid number. Fallback to 0.")
        assert trapezoid.height == 0

    @pytest.mark.parametrize("top,bottom,height", generate_get_cases())
    def test_str(self, top: int, bottom: int, height: int):
        trapezoid = Trapezoid(top, bottom, height)

        assert str(top) in str(trapezoid)
        assert str(bottom) in str(trapezoid)
        assert str(height) in str(trapezoid)

    @pytest.mark.parametrize(
        "top,bottom,height,area", [(1, 1, 1, 1.0), (9, 12, 50, 525.0)]
    )
    def test_area(self, top: int, bottom: int, height: int, area: float):
        trapezoid = Trapezoid(top, bottom, height)
        assert trapezoid.getArea() == area

    def test_lt(self):
        trapezoidA = Trapezoid(1, 1, 1)
        trapezoidB = Trapezoid(1, 1, 2)
        assert trapezoidA < trapezoidB
