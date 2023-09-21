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
    json_obj1 = json.dumps([dataclasses.asdict(player) for player in players])
    print("Serialized:", json_obj1)
