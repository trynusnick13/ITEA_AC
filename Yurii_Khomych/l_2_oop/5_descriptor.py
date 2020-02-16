class RevealAccess:
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.__get__()
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        raise ValueError()

class MyClass:
    x = RevealAccess(initval=10, name='var "x"')
    y = 5

m = MyClass()
m.x
# Retrieving var "x"
# 10
m.x = 20
# Updating var "x"
m.x
# Retrieving var "x"
20
m.y
5