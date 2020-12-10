import math


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt((self.coor1[0] - self.coor2[0]) ** 2 \
                         + (self.coor1[1] - self.coor2[1]) ** 2)

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        if (x1 > x2):
            return (y1 - y2) / (x1 - x2)
        elif (x1 < x2):
            return (y2 - y1) / (x2 - x1)
        else:
            return float("inf")


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * self.radius * math.pi * (self.radius + self.height)


c = Cylinder(2, 3)

print(f"Volume is {c.volume()}")
print(f"Surface area is {c.surface_area()}")
