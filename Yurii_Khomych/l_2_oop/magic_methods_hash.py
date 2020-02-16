class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        # self.id = id_

    def __eq__(self, other):
        return hash((self.age, self.name)) == hash((other.age, other.name))

    def __hash__(self):
        print("The hash is:")
        return hash((self.age, self.name))


person = Person(23, "Adam")
person2 = Person(23, "Adam")
person2.name = "Jony"
person == person2
hash(person2)
hash(person)
users = {
    person: {"pets": ["Barsik", "Tuzik"]},
    person2: {"toys": ["car", "doll"]},
}
unique_users = {person2, person}
print(unique_users)

hash(1)
hash(2)
hash(2.1)
hash("2.1")
hash(("2.1"))
# hash(["2.3"])

my_tuple = ([], [])
my_tuple[0].append(1)
pass