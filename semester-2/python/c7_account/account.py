from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Account:
    balance: Decimal

    def despoit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> int:
        self.balance -= amount
        return amount

    def add_interest(self, rate: Decimal) -> None:
        self.balance += self.balance * rate

