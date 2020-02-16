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

    def __call__(self, abc):
        print("Start amount: {}".format(self.amount))
        print("Transactions: ")
        for transaction in self:
            print(transaction)
        print("\nBalance: {}".format(self.balance))
        return abc

    def __enter__(self):
        print("ENTER WITH: Making backup of transactions for rollback")
        self._copy_transactions = list(self._transactions)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("EXIT WITH:", end=" ")
        if exc_type:
            self._transactions = self._copy_transactions
            print("Rolling back to previous transactions")
            print(
                "Transaction resulted in {} ({})".format(
                    exc_type.__name__, exc_val
                )
            )
        else:
            print("Transaction OK")


def validate_transaction(acc, amount_to_add):
    with acc as a:
        print("Adding {} to account".format(amount_to_add))
        a.add_transaction(amount_to_add)
        print("New balance would be: {}".format(a.balance))
        if a.balance < 0:
            raise ValueError("sorry cannot go in debt!")


acc = Account("bob", 10)
# Add call possibility for class
acc()

# acc.add_transaction(20)
# acc.add_transaction(-10)
# acc.add_transaction(50)
# acc.add_transaction(-20)
# acc.add_transaction(30)


# context manager usage
acc4 = Account("sue", 10)

print("\nBalance start: {}".format(acc4.balance))
validate_transaction(acc4, 20)

print("\nBalance end: {}".format(acc4.balance))

# get exception
acc4 = Account("sue", 10)

print("\nBalance start: {}".format(acc4.balance))
try:
    validate_transaction(acc4, -50)
except ValueError as exc:
    print(exc)

print("\nBalance end: {}".format(acc4.balance))
