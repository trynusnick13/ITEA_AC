# Parent class
class Dog:

    # Class attribute
    species = "mammal"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} RUN so rapidly {}".format(self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    species = "reptile"
    pass


# Child classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)
print(jim.description())
bobik = RussellTerrier("Bobik", 1)

# Child classes have specific attributes
# and behaviors as well
print(jim.run("slowly"))
