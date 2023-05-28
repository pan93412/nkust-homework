from math import floor


class Decryptor:
    def __init__(self, y: str):
        self.y = y

    @classmethod
    def decrypt_char(cls, c: str):
        # X * 3 % 10 = Y
        # (Y + 10 * k) / 3 = X when 0 < k <= 4

        k = 0
        y = int(c)

        for k in range(0, 4):
            x = (y + 10 * k) / 3
            if 0 <= x < 10 and x.is_integer():
                return str(floor(x))

        raise Exception("no such answer")


    def decrypt(self) -> str:
        x = "".join(map(self.decrypt_char, self.y))
        return x
