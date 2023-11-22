import math

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def invert_coordinates(self):
        self._x, self._y = self._y, self._x 

    def distance_to(self, other_point):
        dx = self._x - other_point.x
        dy = self._y - other_point.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return f"({self._x}, {self._y})"

# Test program
point = Point(3, 4)
print("Point:", point)
print("X Coordinate:", point.x)

point.x = 0
print("After setting X coordinate to 0:", point)
