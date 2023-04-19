# Step 1: Import abc
from abc import ABC, abstractmethod

class Car(ABC):
    # Step 1: Add property `oil`
    def __init__(self, color: str, oil: int):
        self.color = color
        self.oil = oil

    # Step 1: Mark `setOil` an abstract method
    @abstractmethod
    def setOil(self) -> None: pass

    # Step 1: Mark `getOil` an abstract method
    @abstractmethod
    def getOil(self) -> int: pass

    def show(self) -> None:
        print(f'color={self.color}')

# Step 2: Add class `Trunk`, inherit from `Car`
class Trunk(Car):
    def __init__(self, dr: int, ow: str, co: str, oil: int):
        self.door = dr
        self.owner = ow

        # Step 2: Call `super().__init__`
        # to initialize color (and oil)
        super().__init__(co, oil)

    # Step 3: show() to print `door`,
    # `owner`, `color`, `oil`
    def show(self) -> None:
        print(f'door={self.door}, owner={self.owner}, color={self.color}, oil={self.oil}')

    # Step 2: Implement `setOil` and `getOil`
    def setOil(self, oil: int) -> None:
        self.oil = oil

    def getOil(self) -> int:
        return self.oil

myTrunk = Trunk(dr=2, ow='Me', co='blue', oil=95)
myTrunk.show()
