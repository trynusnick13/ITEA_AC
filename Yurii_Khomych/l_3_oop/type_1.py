Foo = type("Foo", (), {})

x = Foo()
print(x)

Bar = type("Bar", (Foo,), dict(attr=100, ))

x = Bar()
print(x.attr)
print(x.__class__)
print(x.__class__.__bases__)

# the same as Bar
class Baz(Foo):
    attr = 100


x = Baz()
print(x.attr)
print(x.__class__)
print(x.__class__.__bases__)
