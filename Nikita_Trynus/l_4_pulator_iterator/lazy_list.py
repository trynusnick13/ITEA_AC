"""
Create list like class which can apply only integer values (Develop two classes using UserList and list)
 and have 3 main list methods (pop, append, extend).
"""
from collections import UserList


class LazyList(list, UserList):
    def __init__(self, *args):
        for i in args[0]:
            if not isinstance(i, int):
                raise AttributeError('Only integer is acceptable')

            else:
                super().__init__(*args)

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise AttributeError('Only integer is acceptable')
        else:
            super().__setitem__(key, value)

    def append(self, value):
        if not isinstance(value, int):
            raise AttributeError('Only integer is acceptable')
        else:
            super().append(value)

    def pop(self):
        raise AttributeError("I am lazy list, sorry (((")

    def append(self, list_to_extend):
        for element in list_to_extend:
            if not isinstance(element, int):
                raise AttributeError('Only integer is acceptable')
            else:
                super().append(element)

a = LazyList((1, 2, 3))
# a.append(1.2)
b = LazyList((1, 2, 3))
a.extend(b)
print(a)