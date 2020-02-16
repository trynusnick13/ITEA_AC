# Currying in Python - Many to Single Argument

# a(x) = b(c(d(x)))
def change(b, c, d):
    def a(x):
        return b(c(d(x)))

    return a


# v(a, b, c, d, e) = w(x(y(z(a, b, c, d, e))))
def change(a=None):
    def w(b):
        def x(c):
            def y(d):
                def z(e):
                    print(a, b, c, d, e)

                return z

            return y

        return x

    return w


change(10)(20)(30)(40)(50)
