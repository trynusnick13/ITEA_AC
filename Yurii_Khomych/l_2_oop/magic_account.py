from functools import total_ordering


@total_ordering
class Account:
    """A simple account class"""

    def __init__(self, owner, amount=0):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):
        return "Account({!r}, {!r})".format(self.owner, self.amount)

    def __str__(self):
        return "Account of {} with starting amount: {}".format(
            self.owner, self.amount
        )

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __reversed__(self):
        return self[::-1]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance


acc = Account("bob")  # default amount = 0
acc = Account("bob", 10)

# __repr__ __str__
str(acc)
print(acc)
repr(acc)


# __len__, __getitem__, __reversed__
acc = Account("bob", 10)

acc.add_transaction(20)
acc.add_transaction(-10)
acc.add_transaction(50)
acc.add_transaction(-20)
acc.add_transaction(30)
#
acc.balance

# __len__, __getitem__, __reversed__

len(acc)

for t in acc:
    print(t)

acc[1]
list(reversed(acc))

# __eq__, __lt__
2 > 1
# True

"a" > "b"
# False

dir("a")

acc2 = Account("tim", 100)
acc2.add_transaction(20)
acc2.add_transaction(40)
acc2.balance

acc2 > acc

acc2 > acc
acc2 < acc

acc == acc2

acc3 = Account("tim", 100)
acc4 = Account("tim", 100)
acc3 == acc4
