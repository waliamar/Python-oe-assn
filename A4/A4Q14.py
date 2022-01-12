class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width


r1 = Rectangle(5, 2)
print(r1.area())
