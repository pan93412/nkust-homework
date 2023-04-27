import dataclasses
import random

import pytest
from .p3 import Account, BalanceNotEnough

name = [
    "Alex",
    "David",
    "Peter",
    "Thompson",
    "王曉明",
    "張小寒",
    "ABC",
    "\x00\x01\x02",
    "W" * 10,
]


class TestAccount:
    @pytest.mark.parametrize(
        "money,owner",
        [
            pytest.param(
                random.randint(0, 10**4), random.choice(name), id="money,name"
            )
            for _ in range(100)
        ],
    )
    def test_construction(self, money: int, owner: str):
        dataclasses.is_dataclass(Account(money, owner))

    @pytest.mark.parametrize(
        "money,cash1,cash2",
        [
            pytest.param(
                random.randint(0, 10**24),
                random.randint(0, 10**12),
                random.randint(0, 10**6),
                id="money,cash1,cash2",
            )
            for _ in range(100)
        ],
    )
    def test_income(self, money: int, cash1: int, cash2: int):
        account = Account(money, "ABC")
        assert account.money == money

        account.income(cash1)
        assert account.money == money + cash1

        account.income(cash2)
        assert account.money == money + cash1 + cash2

    @pytest.mark.parametrize(
        "money,cash1,cash2",
        [
            pytest.param(
                random.randint(10**23, 10**24),
                random.randint(10**11, 10**12),
                random.randint(10**5, 10**6),
                id="money,cash1,cash2",
            )
            for _ in range(100)
        ],
    )
    def test_outcome_success(self, money: int, cash1: int, cash2: int):
        account = Account(money, "ABC")
        assert account.money == money

        account.outcome(cash1)
        assert account.money == money - cash1

        account.outcome(cash2)
        assert account.money == money - cash1 - cash2

    @pytest.mark.parametrize(
        "money,cash",
        [
            pytest.param(
                random.randint(10**5, 10**6),
                random.randint(10**11, 10**12),
                id="money,cash",
            )
            for _ in range(100)
        ],
    )
    def test_outcome_balance_not_enough(self, money: int, cash: int):
        account = Account(money, "ABC")
        assert account.money == money
        assert account.money < cash

        with pytest.raises(BalanceNotEnough):
            account.outcome(cash)

    def test_get_owner(self):
        account = Account(12345, "ABC")
        assert account.getOwner() == "ABC"

    def test_get_money(self):
        account = Account(12345, "ABC")
        assert account.getMoney() == 12345
