from dataclasses import dataclass


@dataclass
class StandardWeight:
    height: int
    gender: int

    def calculate(self):
        match self.gender:
            case 1:
                return (self.height - 80) * 0.7
            case 2:
                return (self.height - 70) * 0.6
            case _:
                raise Exception("unexpected gender")

