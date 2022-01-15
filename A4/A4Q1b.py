class Country:
    def __init__(self, name, pop, area):
        self.name = name
        self.population = pop
        self.area = area


c1 = Country('India', 1380000000, 328700000)
print(c1.area)
print(c1.name)
print(c1.population)
