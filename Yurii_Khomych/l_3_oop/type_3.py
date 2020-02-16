def f(self, obj):
    print("attr =", obj.attr)


Foo = type("Foo", (), {"attr": 100, "attr_val": f})

x = Foo()
print(x.attr)
print(x.attr_val())


# the same as
def f(obj):
    print("attr =", obj.attr)


class Foo:
    attr = 100
    attr_val = f


x = Foo()
print(x.attr)
print(x.attr_val())
