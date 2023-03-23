class Desk: pass
class Chair: pass
class Beaker: pass
class Scale: pass

class Laptop: pass

class Lab:
    laptop: Laptop | None

    def __init__(self, desk: Desk, chair: Chair, beaker: Beaker, scale: Scale):
        self.desk = desk
        self.chair = chair
        self.beaker = beaker
        self.scale = scale

    def place_laptop(self, laptop: Laptop):
        self.laptop = laptop

    def take_laptop_away(self):
        self.laptop = None

desk = Desk()
chair = Chair()
beaker = Beaker()
scale = Scale()

laptop = Laptop()

lab = Lab(desk, chair, beaker, scale)
lab.place_laptop(laptop)
lab.take_laptop_away()
