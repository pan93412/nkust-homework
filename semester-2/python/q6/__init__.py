import math


class Sphere:
    def __init__(self, r: int):
        self.rad = r

    def volume(self):
        return (4/3)*math.pi*(self.rad**3)

    def surface_area(self):
        return 4*math.pi*(self.rad**2)

    def __repr__(self):
        return f"Sphere object, rad = {self.rad}"

    def __str__(self):
        return f"Sphere object, rad = {self.rad}, volume = {self.volume()}, surface area = {self.surface_area()}"
