import math


class Shape():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Point(Shape):
    pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def contains(self, clazz):
        c = []
        p = []
        for v in self.__dict__.values():
            c.append(v)
        for v in clazz.__dict__.values():
            p.append(v)
        if ((p[0] - c[0])**2 + (p[1] - c[1])**2 <= c[2] * c[2]) is True:
            print("True")
        else:
            print("False")


class Triangle(Shape):
    def __init__(self, x, y, heigth, length):
        super().__init__(x, y)
        self.heigth = heigth
        self.length = length

    def square(self):
        return self.heigth * self.length / 2


class Parallelogram (Shape):
    def __init__(self, x, y, a, b, angle):
        super().__init__(x, y)
        self.angle = angle
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b * math.sin(math.radians(self.angle))


class Scenne:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def square(self):
        for f in self._figures:
            print(f.square())

    def total_square(self):
        return sum(f.square() for f in self._figures)


p = Point(1, 42)
c = Circle(0, 0, 10)
c.contains(p)
t = Triangle(0, 0, 3, 4)
pa = Parallelogram(0, 0, 4, 6, 38)
scenne = Scenne()
scenne.add_figure(t)
scenne.add_figure(pa)
scenne.square()
print(scenne.total_square())
