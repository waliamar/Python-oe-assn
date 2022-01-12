class Rocket():
    def __init__(self, x, y):
        self.latitude = int(x)
        self.longitude = int(y)

    def position(self):
        return (self.latitude, self.longitude)


rockets = []
for i in range(5):
    r = Rocket(0, 5*i)
    rockets.append(r)

for b in rockets:
    print(b.position())
