from random import choices
from textui import TextUi

class TwoATwoB:
    # 可能的輸入答案
    answer_set = ["red", "blue", "yellow", "green"]

    response = {
        "correct": "1",
        "incorrect_pos": "2",
        "no_such_color": "3"
    }

    def __init__(self) -> None:
        # 我們背後的正確答案
        self.our_answer = choices(self.answer_set, k=4)

    def verify(self, input: list[str]) -> str:
        buf = ""

        for idx, entry in enumerate(input):
            if entry not in self.our_answer:
                buf += self.response["no_such_color"]
            elif entry != self.our_answer[idx]:
                buf += self.response["incorrect_pos"]
            else:
                buf += self.response["correct"]

        return buf


class Q4TextUi(TextUi):
    loop = True
    attempts = 0

    def __init__(self) -> None:
        self.game_board = TwoATwoB()

    def main(self):
        if self.attempts >= 10:
            print("挑戰失敗")
            exit()

        inputs = self.input_split("")(" ")
        result = self.game_board.verify(inputs)

        if result == "1111":
            print("正確答案")
            exit()

        print(result)
        self.attempts += 1

if __name__ == "__main__":
    Q4TextUi()()
