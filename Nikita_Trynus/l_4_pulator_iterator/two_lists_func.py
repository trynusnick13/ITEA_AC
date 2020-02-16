"""
Write a function that accepts two lists and returns a new iterable with each of the given items "interleaved"
(item 0 from iterable 1, then item 0 from iterable 2, then item 1 from iterable 1, and so on).
 Here's an example (which returns lists): >>> interleave([1, 2, 3, 4], [5, 6, 7, 8]) [1, 5, 2, 6, 3, 7, 4, 8]
"""


def interleave(list_1, list_2):
    new_iterable = []
    for i, j in zip(list_1, list_2):
        new_iterable.extend((i,j))
    return new_iterable

def generator_squared_interleave(list_1, list_2):
    a = list(map(lambda x,y: x**y, list_1,list_2))

    # b = (lambda x,y: x**y for x in list_1 for y in list_2)
    # b = [lambda x, y: x ** y for x in list_1 for y in list_2]
    for i in a:
        yield i
