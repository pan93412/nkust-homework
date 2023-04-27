from dataclasses import dataclass


@dataclass
class Account:
    money: int
    owner: str

    def income(self, cash: int):
        self.money += cash

    def outcome(self, cash: int):
        if self.money < cash:
            raise BalanceNotEnough()

        self.money -= cash

    def getMoney(self):
        return self.money

    def getOwner(self):
        return self.owner

class BalanceNotEnough(Exception):
    pass
