from q6 import Sphere
import math

class TestSphere:
    rad = 10

    def test_init(self):
        s = Sphere(self.rad)
        assert s.rad == self.rad

    def test_volume(self):
        s = Sphere(self.rad)
        assert s.volume() == (4/3)*math.pi*(s.rad**3)

    def test_surface_area(self):
        s = Sphere(self.rad)
        assert s.surface_area() == 4*math.pi*(s.rad**2)

    def test_repr(self):
        s = Sphere(self.rad)
        assert repr(s) == f"Sphere object, rad = {s.rad}"

    def test_str(self):
        s = Sphere(self.rad)
        assert str(s) == f"Sphere object, rad = {s.rad}, volume = {s.volume()}, surface area = {s.surface_area()}"
