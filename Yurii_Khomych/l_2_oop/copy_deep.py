import copy

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)

xs[1][0] = "X"

print(xs)
print(zs)
