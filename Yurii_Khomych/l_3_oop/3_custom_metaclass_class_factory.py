class Meta(type):
    def __init__(cls, name, bases, dct):
        cls.attr = 100


class X(metaclass=Meta):
    pass


class Y(metaclass=Meta):
    pass


class Z(metaclass=Meta):
    pass


print(Z.attr)
print(Y.attr)
print(X.attr)
