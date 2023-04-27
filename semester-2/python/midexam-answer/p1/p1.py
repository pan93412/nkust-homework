from typing import Callable


class Trapezoid:
    top: int
    bottom: int
    height: int

    __no = 999

    def __init__(
        self, top: int, bottom: int, height: int, printer: Callable[[str], None] = print
    ):
        self.printer = printer
        self.setTop(top)
        self.setBottom(bottom)
        self.setHeight(height)

    def getTop(self):
        return self.top

    def getButton(self):
        return self.getBottom()

    def getBottom(self):
        return self.bottom

    def getHeight(self):
        return self.height

    def setTop(self, value: int):
        if value < 0:
            self.printer("Not a valid number. Fallback to 0.")
            value = 0

        self.top = value

    def setButton(self, value: int):
        return self.setBottom(value)

    def setBottom(self, value: int):
        if value < 0:
            self.printer("Not a valid number. Fallback to 0.")
            value = 0

        self.bottom = value

    def setHeight(self, value: int):
        if value < 0:
            self.printer("Not a valid number. Fallback to 0.")
            value = 0

        self.height = value

    def __str__(self):
        parameter_map = [self.top, self.bottom, self.height]
        parameter_str = ",".join((str(v) for v in parameter_map))

        return f"Trapezoid({parameter_str})"

    def getArea(self):
        return ((self.top + self.bottom) * self.height) / 2

    def __lt__(self, other: "Trapezoid"):
        return self.getArea() < other.getArea()
