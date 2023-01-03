#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Question 2"""

from abc import ABC, abstractmethod
from typing import Callable, Type

from textui import TextUi


class Approach(ABC):
    """一個處理方式的抽象類別"""

    @classmethod
    def _parse_input(cls, data: str) -> tuple[str, int]:
        [award, amount] = data.split(" ")
        amount = int(amount)

        return award, amount

    @abstractmethod
    def input(self, input_method: Callable[[str], str]) -> None:
        """這裡可以輸入內容，並放入自己的 container 中"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class DictApproach(Approach):
    """處理方式 1：字典"""

    award_table: dict[str, int]

    def __init__(self) -> None:
        self.award_table = {}

    def input(self, input_method: Callable[[str], str]) -> None:
        for _ in range(0, 4):
            award, amount = self._parse_input(input_method(""))
            self.award_table[award] = amount

    def __str__(self) -> str:
        return "\n".join(
            f"{award}牌得到 {amount} 面" for (award, amount) in self.award_table.items()
        )


class ListApproach(Approach):
    """處理方式 2：串列"""

    display_name: list[str]
    award_amount: list[int]

    def __init__(self):
        self.display_name = []
        self.award_amount = []

    def input(self, input_method: Callable[[str], str]) -> None:
        for _ in range(0, 4):
            display_name, amount = self._parse_input(input_method(""))
            self.display_name.append(display_name)
            self.award_amount.append(amount)

    def __str__(self) -> str:
        return "\n".join(
            f"{display_name}牌得到 {amount} 面"
            for (display_name, amount) in zip(self.display_name, self.award_amount)
        )


class ApproachDistributor:
    """根據輸入取得做法"""
    approach_map: dict[str, Type[Approach]]

    def __init__(self):
        self.approach_map = {}

    def register(self, approach_name: str, approach: Type[Approach]) -> None:
        self.approach_map[approach_name] = approach

    def __call__(self, approach_name: str) -> Type[Approach]:
        if approach_name not in self.approach_map:
            raise ValueError(f"找不到做法 {approach_name}")

        return self.approach_map[approach_name]


class Q2TextUi(TextUi):
    approach_distributor: ApproachDistributor

    def __init__(self):
        self.approach_distributor = ApproachDistributor()
        self.approach_distributor.register("1", DictApproach)
        self.approach_distributor.register("2", ListApproach)

    def main(self):
        approach_name = input("處理方式 (1)字典 (2)串列：")
        approach = self.approach_distributor(approach_name)()

        approach.input(self.input)
        print(str(approach))


if __name__ == "__main__":
    Q2TextUi()()
