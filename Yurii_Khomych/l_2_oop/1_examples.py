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


# class Dog:

    # Class Attribute
    # species = "mammal"

    # Initializer / Instance Attributes
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    # instance method
    # def description(self):
    #     return f"{self.name} is {self.age} years old"

    # instance method
    # def speak(self, sound):
    #     return "{} says {}".format(self.name, sound)


# Instantiate the Dog object
# mikey = Dog("Mikey", 6)
#
# call our instance methods
# print(mikey.description())
# print(mikey.speak("Gruff Gruff"))

# period = insight.get("period") or 7

# period = 7 if (isinstance(insight["period"], int) and insight["period"] > 4) or insight["period"] is None else insight["period"]
# period = 7 if insight["period"] > 4 else insight.get("period", 7)
# period = insight.get("period") if insight["period"] <= 4 else 7


# any([key in insight for key in ("name", "key2") for insight in insights])

# any([isinstance(insight["metric_weight"], int) for insight in insights])
# any([key in insights for key in ("metric_weight", "key2")])

my_dict = {1:
     lambda ins_period, sum, sum_level, sum_general, **kwargs:
     (sum * sum_level / sum_general) / ins_period}
    # ins_period=insight["period"],
    # sum=insight["sum"],
    # sum_level=insight["sum_level"],
    # sum_general=insight["sum_general"],
    # jony=1,
    # misha=1,

pass