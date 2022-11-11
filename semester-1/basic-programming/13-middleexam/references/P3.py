'''Question 3

Licensed under AGPL-3.0-only.'''

from typing import Tuple

subject_order = ["平時", "期中考", "期末考"]

def get_score_input_and_its_percent(prompt: str) -> Tuple[float, float]:
    s = float(input(prompt))
    p = float(input("占總成績(%)："))

    return (s, p)

def get_level(score: float) -> str:
    '''Get the level of a score.

    The value is one of ``A``, ``B``, ``C``, ``D``, and ``E``.

    Exception
    ==========
    Raise ``ValueError`` when the value is out of range.'''

    if 0 <= score <= 100:
        return  "A" if 90 <= score else \
                "B" if 80 <= score < 90 else \
                "C" if 70 <= score < 80 else \
                "D" if 60 <= score < 70 else \
                "E"
    else:
        raise ValueError(f"傳入之分數 ({score}) 超出合理分數 ([0, 100]) 區間。請檢查輸入。")


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
