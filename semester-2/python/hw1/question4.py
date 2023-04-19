from dataclasses import dataclass

# Step 1: Create a data class called Trapezoid
@dataclass(frozen=True)
class Trapezoid:
    top: int
    bottom: int
    height: int

    # Step 2: getArea() to calculate the area
    # of the trapezoid
    def getArea(self):
        return (self.top + self.bottom) * self.height / 2

# Step 3: Create an instance of Trapezoid,
# and print the area
w0 = Trapezoid(top=1, bottom=2, height=3)
print(w0.getArea())
