class Account:
    def __init__(self, m: int):
        self.m = m

    def despoit(self, n: int):
        self.m += n

    def withdraw(self, n: int):
        if self.m >= n:
            self.m -= n
            return n
        else:
            self.m, old = 0, self.m
            return old

    def add_interest(self, n: float):
        self.m *= (1+n)

    def balance(self):
        return self.m

    def __str__(self):
        return f"Account({self.m})"
