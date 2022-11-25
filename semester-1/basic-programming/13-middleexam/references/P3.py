'''Question 3

Licensed under AGPL-3.0-only.'''

from typing import Tuple, Union

subject_order = ["平時", "期中考", "期末考"]

Score = Union[int, float]

class InputError(ValueError):
    def __init__(self, subject: str, score: Score, range: Tuple[Score, Score]):
        super().__init__(f"傳入之{subject} ({score}) 超出合理分數 ([{range[0]}, {range[1]}]) 區間。請檢查輸入。")
        self.subject = subject
        self.score = score
        self.range = range

def get_score_input_and_its_percent(prompt: str) -> Tuple[float, float]:
    # 2022-11-25: Check the passed value on input stage.

    s = float(input(prompt))
    if not 0 <= s <= 100: raise InputError("分數", s, (0, 100))

    p = float(input("占總成績(%)："))
    if not 0 <= p <= 100: raise InputError("比例", p, (0, 100))

    return (s, p)


def get_level(score: float) -> str:
    '''Get the level of a score.

    The value is one of ``A``, ``B``, ``C``, ``D``, and ``E``.

    Exception
    ==========
    Raise ``ValueError`` when the value is out of range.'''

    # 2022-11-25: Check the passed value on input stage.
    return  "A" if 90 <= score else \
            "B" if 80 <= score < 90 else \
            "C" if 70 <= score < 80 else \
            "D" if 60 <= score < 70 else \
            "E"


def main():
    subject_inputs = map(get_score_input_and_its_percent, map(
        lambda idx: f"{idx+1}.{subject_order[idx]}分數：",
        range(0, len(subject_order))
    ))

    avg_score = sum(map(lambda s: s[0] * 0.01 * s[1], subject_inputs))
    level = get_level(avg_score)

    print(f"總分為：{avg_score} 分，等級為 {level} 級。")

if __name__ == "__main__":
    try:
        main()
    except (ValueError) as e:
        print(f"錯誤：{str(e)}")
else:
    raise RuntimeError("Unexpected environment.")
