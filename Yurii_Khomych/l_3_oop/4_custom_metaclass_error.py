def new(cls):
    x = type.__new__(cls)
    x.attr = 100
    return x


type.__new__ = new
