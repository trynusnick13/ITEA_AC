class Meta(type):
    def __new__(cls, name, bases, dct):
        result = super().__new__(cls, name, bases, dct)
        result.attr = 100
        return result

    # def __init__(self, name):
    #     self.name = name


class Foo(metaclass=Meta):
    pass


class Bar(metaclass=Meta):
    pass


class Qux(metaclass=Meta):
    pass


print(Foo.attr)
print(Bar.attr, Qux.attr)


class DictLike(type):
    def __getitem__(self, arg):
        return getattr(self, arg)

    def items(cls):
        return (
            (i, cls.__getitem__(i))
            for i in cls.__dict__
            if not i.startswith("__")
        )

    def values(cls):
        return (
            cls.__getitem__(i) for i in cls.__dict__ if not i.startswith("__")
        )


class STATUS(metaclass=DictLike):
    IN_PROCESS = 4
    FINISHED = 20
    FAILED = 30


STATUS.items()
STATUS["IN_PROCESS"]
STATUS.IN_PROCESS
