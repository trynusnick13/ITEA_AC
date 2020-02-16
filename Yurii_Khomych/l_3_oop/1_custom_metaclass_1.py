# class Foo:
#     pass
#
# f = Foo()
#
# def new(cls):
#     x = object.__new__(cls)
#     x.attr = 100
#     return x
#
# def init(self, ):
#     self.new_attr = 200
#
# Foo.__init__ = init
#
# Foo.__new__ = new
#
# f1 = Foo()
# f1.attr


# g = Foo()
# g.attr


from pprint import pprint


class Tag1:
    pass


class Tag2:
    pass


class Tag3:
    def tag3_method(self):
        pass


class MetaBase(type):
    def __new__(mcl, name, bases, nmspc):
        print("MetaBase.__new__\n")
        return super().__new__(mcl, name, bases, nmspc)

    def __init__(cls, name, bases, nmspc):
        print("MetaBase.__init__\n")
        super(MetaBase, cls).__init__(name, bases, nmspc)

    def __call__(self, *args, **kwargs):
        print("we are in call")
        super().__call__(*args, **kwargs)


class MetaNewVSInit(MetaBase):
    def __new__(mcl, name, bases, nmspc):
        # First argument is the metaclass ``MetaNewVSInit``
        print("MetaNewVSInit.__new__")
        for x in (mcl, name, bases, nmspc):
            pprint(x)
        print("")
        # These all work because the class hasn't been created yet:
        if "foo" in nmspc:
            nmspc.pop("foo")
        name += "_x"
        bases += (Tag1,)
        nmspc["baz"] = 42
        return super().__new__(mcl, name, bases, nmspc)

    def __init__(cls, name, bases, nmspc):
        # First argument is the class being initialized
        print("MetaNewVSInit.__init__")
        for x in (cls, name, bases, nmspc):
            pprint(x)
        print("")
        if "bar" in nmspc:
            nmspc.pop("bar")  # No effect
        name += "_y"  # No effect
        bases += (Tag2,)  # No effect
        nmspc["pi"] = 3.14159  # No effect
        super(MetaNewVSInit, cls).__init__(name, bases, nmspc)
        # These do work because they operate on the class object:
        cls.__name__ += "_z"
        cls.__bases__ += (Tag3,)
        cls.e = 2.718

    def __call__(self, *args, **kwargs):
        print("we are in call 2")
        super().__call__(*args, **kwargs)

class Test(metaclass=MetaNewVSInit):
    # __metaclass__ = MetaNewVSInit
    def __init__(self):
        print("Test.__init__")

    def foo(self):
        print("foo still here")

    def bar(self):
        print("bar still here")


t = Test()
print("class name: " + Test.__name__)
print("base classes: ", [c.__name__ for c in Test.__bases__])
print([m for m in dir(t) if not m.startswith("__")])
t.bar()
print(t.e)
