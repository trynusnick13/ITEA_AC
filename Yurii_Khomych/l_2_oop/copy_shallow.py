xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)  # Make a shallow copy

xs.append(["new sublist"])
print(ys)
xs[1][0] = "X"
print(xs)
print(ys)
