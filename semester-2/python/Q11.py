from dataclasses import dataclass
from abc import ABC, abstractmethod

class Topping(ABC):
    def __init__(self):
        pass

    def price(self) -> float:
        return 2

    @abstractmethod
    def description(self) -> str: pass

class Cheese(Topping):
    def description(self): return "Cheese"

class Pepperoni(Topping):
    def description(self): return "Pepperoni"

class Ham(Topping):
    def description(self): return "Ham"

class ToppingBox(list[Topping]):
    def price(self) -> float:
        return sum([topping.price() for topping in self])

    def quantity(self) -> dict[str, int]:
        result = dict[str, int]()

        for topping in self:
            desc = topping.description()

            result[desc] = result[desc] + 1 if desc in result else 1

        return result

    def __str__(self) -> str:
        buf = ""

        for name, count in self.quantity().items():
            buf += f"{name} (x{count}), "

        return buf[:-2]

@dataclass
class Size:
    id: str
    name: str

    def __str__(self):
        return self.name


class Pizza(ABC):
    def __init__(self):
        self._toppings = ToppingBox()

    def add_topping(self, topping: Topping):
        self._toppings.append(topping)

    def description(self) -> str:
        return f"{self.size()} Pizza: {self._toppings}"

    def __str__(self) -> str:
        return self.description()

    @abstractmethod
    def size(self) -> Size: pass

    @abstractmethod
    def price(self) -> float: pass


class SmallPizza(Pizza):
    def size(self) -> Size:
        return Size("small", "Small")

    def price(self) -> float:
        return 14 + self._toppings.price()

class MediumPizza(Pizza):
    def size(self) -> Size:
        return Size("medium", "Medium")

    def price(self) -> float:
        return 12 + self._toppings.price()

class LargePizza(Pizza):
    def size(self) -> Size:
        return Size("large", "Large")

    def price(self) -> float:
        return 10 + self._toppings.price()

large_pizza = MediumPizza()

large_pizza.add_topping(Cheese())
large_pizza.add_topping(Cheese())
large_pizza.add_topping(Pepperoni())
large_pizza.add_topping(Ham())

print(large_pizza)
print(large_pizza.price())
