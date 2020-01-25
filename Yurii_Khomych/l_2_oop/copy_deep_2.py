import copy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"


class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return f"Rectangle({self.topleft!r}, " f"{self.bottomright!r})"


a = Point(23, 42)
b = copy.copy(a)

rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)

rect.topleft.x = 999
print(rect)
print(srect)


drect = copy.deepcopy(srect)
drect.topleft.x = 222
print(drect)
print(rect)
print(srect)
