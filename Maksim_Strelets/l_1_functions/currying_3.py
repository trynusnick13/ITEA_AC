def change(b, c, d):
    def a(x):
        return b(c(d(x)))

    return a


def daystohour(time):
    """ Function that converts days to hours. """
    return time * 24


def hourstominutes(time):
    """ Function that converts hours to minutes. """
    return time * 60


def minutestoseconds(time):
    """ Function that converts minutes to seconds. """
    return time * 60


transform = change(minutestoseconds, hourstominutes, daystohour)
e = transform(10)
print(e)
