from dataclasses import field, dataclass
from typing import Callable, Iterator


@dataclass()
class User:
    name: str
    number: int
    score: list[int] = field(default_factory=list)


class UserScoreManager:
    """管理使用者的成績。"""

    def __init__(self, subjects_order: list[str], data_getter: Callable[[str], int]):
        """
        Parameters
        ==========

        - subjects_order: 科目順序
        - data_source_getter:
            取資料的來源函數。
            Parameter 1 是 prompt；
            Return Value 是錄入之成績。
        """
        self.subjects_order = subjects_order
        self.data_source_getter = data_getter

    def record(self, user: User) -> None:
        """將成績錄入到指定的 user 中"""
        for subject in self.subjects_order:
            user.score.append(self.data_source_getter(f"請輸入{user.name}的{subject}成績："))

    def record_all(self, users: list[User]) -> Iterator[None]:
        """將成績錄入到指定的 users 名單中

        回傳一個 Iterator。"""
        return map(self.record, users)


class UserInfoPrinter:
    """根據設定輸出使用者的資訊。"""

    subjects_order: list[str]

    def __init__(self, subjects_order: list[str]):
        self.subjects_order = subjects_order

    def format(self, users: list[User]) -> str:
        output_buffer: list[list[str]] = [["姓名", "座號"] + self.subjects_order]

        for user in users:
            user_buffer: list[str] = [user.name, f"{user.number:>4}"]

            for score in user.score:
                user_buffer.append(f"{score:>4}")

            output_buffer.append(user_buffer)

        return "\n".join(map(lambda to_tab_buf: "\t".join(to_tab_buf), output_buffer))


subjects_order = ["國文", "數學", "英文"]

users = [
    User("林大明", 1),
    User("陳大中", 2),
    User("林大明", 11),
]

recorder = UserScoreManager(subjects_order, lambda p: int(input(p)))
list(recorder.record_all(users))

printer = UserInfoPrinter(subjects_order)
result = printer.format(users)

print(result)
