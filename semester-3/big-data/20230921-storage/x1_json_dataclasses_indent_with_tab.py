# raw-file: ch1_3.py
import dataclasses
import json


@dataclasses.dataclass(order=True)
class Player:
    name: str
    team: str


if __name__ == "__main__":
    players = [
        Player("Stephen Curry", "Golden State Warriors"),
        Player("Kevin Durant", "Golden State Warriors"),
        Player("Lebron James", "Cleveland Cavaliers"),
        Player("James Harden", "Houston Rockets"),
        Player("Paul Gasol", "San Antonio Spurs"),
    ]
    serialized_with_indent = json.dumps(
        [dataclasses.asdict(player) for player in players], indent="\t"
    )
    print("Serialized with Indent:", serialized_with_indent)

    serialized_with_sk = json.dumps(
        [dataclasses.asdict(player) for player in players], sort_keys=True, indent="\t"
    )
    print("Serialized with sort keys:", serialized_with_sk)  # 沒差
