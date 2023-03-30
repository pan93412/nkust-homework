class Role:
    def __init__(self, n, h, w):
        self.name = n
        self.height = h
        self.weapon = w

    def printName(self):
        print(self.name)

    def printWeapon(self):
        print(self.weapon)

    def __str__(self):
        return f"{self.name} and {self.weapon}"

    def __eq__(self, other):
        return self.name == other.name


master = Role("master", "178", "no")
print(master)
monkey = Role("monkey", "188", "golden cudgel")
print(monkey)

print(master == monkey)
