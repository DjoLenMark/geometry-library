import math
from .shape import Shape

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if any(side <= 0 for side in (a, b, c)):
            raise ValueError("Длины сторон должны быть положительными числами.")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Треугольник с такими сторонами не существует.")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right_triangle(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)
