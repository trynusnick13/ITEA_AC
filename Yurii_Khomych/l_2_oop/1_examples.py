# class Animal:
#     pass
#
#
# class Dog:
#
    # Class Attribute
    # species = 'mammal'
    #
    # Initializer / Instance Attributes
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #
    # def my_method(self):
    #     print()
#
# dog = Dog("Bobby", "John")
# dog.my_method()
#


# # Instantiate the Dog object
# philo = Dog("Philo", 5)
# mikey = Dog("Mikey", 6)
#
# # Access the instance attributes
# print("{} is {} and {} is {}.".format(
#     philo.name, philo.age, mikey.name, mikey.age))
#
# # Is Philo a mammal?
# if philo.species == "mammal":
#     print("{0} is a {1}!".format(philo.name, philo.species))


class Dog:

    # Class Attribute
    species = "mammal"

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Instantiate the Dog object
mikey = Dog("Mikey", 6)

# call our instance methods
print(mikey.description())
print(mikey.speak("Gruff Gruff"))
