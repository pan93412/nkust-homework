class Car:
    def __init__(self, color) -> None:
        self.color = color

    def show(self):
        print(f'color={self.color}')

class Trunk(Car):
    def __init__(self, dr, ow, co):
        super().__init__(co)
        self.door = dr
        self.owner = ow

    def show(self):
        for key, value in self.__dict__.items():
            print(f'{key}={value}')
