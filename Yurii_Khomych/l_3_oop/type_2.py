Foo = type("Foo", (), {"attr": 100, "attr_val": lambda x: x.attr})

x = Foo()
print(x.attr)
print(x.attr_val())


# the same as
class Foo:
    attr = 100

    def attr_val(self):
        return self.attr


x = Foo()
print(x.attr)
print(x.attr_val())
