from dataclasses import field, dataclass


@dataclass()
class User:
    name: str
    number: int
    score: list[int] = field(default_factory=list)


subjects_order = ["國文", "數學", "英文"]

users = [
    User("林大明", 1),
    User("陳大中", 2),
    User("林大明", 11),
]

# 根據 score_order 錄入成績。
for user in users:
    for subject in subjects_order:
        user.score.append(int(input(
            f"請輸入{user.name}的{subject}成績："
        )))

output_buffer: list[list[str]] = [
    ["姓名", "座號"] + subjects_order
]

for user in users:
    user_buffer: list[str] = [user.name, f"{user.number:>4}"]

    for score in user.score:
        user_buffer.append(f"{score:>4}")

    output_buffer.append(user_buffer)

print("\n".join(map(lambda to_tab_buf: "\t".join(to_tab_buf), output_buffer)))
