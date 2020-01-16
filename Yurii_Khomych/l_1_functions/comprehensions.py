# List

squares = []
for x in range(10):
    squares.append(x * x)

squares = [x * x for x in range(10)]
# squares = (x * x for x in range(10))

even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x * x)

even_squares = [x * x for x in range(10) if x == 0]

my_set = set()
for x in range(-9, 10):
    my_set.add(x * x)

set_comp = {x * x for x in range(-9, 10)}

dict_comprehension = {x: x * x for x in range(5)}

# nested comprehensions
