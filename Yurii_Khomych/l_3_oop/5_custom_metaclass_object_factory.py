# Metaclasses are sometimes referred to as class factories.


class Foo:
    # Object factory
    def __init__(self):
        self.attr = 100


x = Foo()
print(x.attr)
y = Foo()
print(y.attr)
z = Foo()
print(z.attr)
