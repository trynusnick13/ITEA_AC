# https://www.youtube.com/watch?v=yk-IXz0DjTY&list=PLTgRMOcmRb3Oih3rUyrD_R_i1YyCdvoIO&index=4
# https://habr.com/en/sandbox/43504/
# https://habr.com/ru/post/335866/


def add(a, b, c):
    return a + b + c


print(add(10, 100, 1000))

from functools import partial

add_10 = partial(add, 10)
add_10_100 = partial(add_10, 100)
print(add_10_100(1000))


from inspect import signature


def curry(fnc):
    def inner(arg):
        if len(signature(fnc).parameters) == 1:
            return fnc(arg)
        return curry(partial(fnc, arg))

    return inner


@curry
def add(a, b, c):
    return a + b + c


print(add(10)(100)(1000))
