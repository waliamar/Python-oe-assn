from math import pi


class Circle:
    def __init__(self, rad):
        self.radius = int(rad)

    def area(self):
        return pi*(self.radius**2)

    def perimeter(self):
        return 2*pi*self.radius


c1 = Circle(2)
print(c1.area())
print(c1.perimeter())
