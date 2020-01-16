def change(func_1, func_2, func_3):
    def inner_func(arg):
        return func_1(func_2(func_3(arg)))

    return inner_func


def kilometer2meter(dist):
    """ Function that converts km to m. """
    return dist * 1000


def meter2centimeter(dist):
    """ Function that converts m to cm. """
    return dist * 100


def centimeter2feet(dist):
    """ Function that converts cm to ft. """
    return dist / 30.48


kilometer2meter_result = kilometer2meter(565)
meter2centimeter_result = meter2centimeter(kilometer2meter_result)
centimeter2feet_result = centimeter2feet(meter2centimeter_result)

centimeter2feet_result = centimeter2feet(meter2centimeter(kilometer2meter(565)))


transform = change(centimeter2feet, meter2centimeter, kilometer2meter)
e = transform(565)
print(e)
result = change(centimeter2feet, meter2centimeter, kilometer2meter)(565)
