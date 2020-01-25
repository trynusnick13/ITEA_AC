class Number:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Number(self.number + other.number)

    def __mul__(self, other):
        return Number(self.number * other.number)

    def __sub__(self, other):
        return Number(self.number - other.number)

    def __repr__(self):
        return f"<Number: {self.number}>"


nsum = Number(1) + Number(2)
print(nsum)
nmul = Number(1) * Number(2)
print(nmul)
nsub = Number(1) - Number(2)
print(nsub)
print(sum([Number(1), Number(2), Number(3)], Number(0)))
