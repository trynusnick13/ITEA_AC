def simple_function(a):
    def line(b=0):
        def compute(x):
            return [a + b * xi for xi in x]

        return compute
    #
    # def squad():
    #     return 1
    # if a == 1:
    #     return line
    # else:
    #     return squad

simple_function(3)()(1)
x = range(-4, 4, 1)
print(f"x {list(x)}".format(list(x)))
print(f"constant {simple_function(3)()(x)}")
print(f"line {simple_function(3)(-2)(x)}")

line_through_zero = simple_function(0)
print(f"line through zero {line_through_zero(1)(x)}")
