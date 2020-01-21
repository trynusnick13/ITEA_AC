# try:
#     one = int("1")
#     # raise EOFError
#     one / 0
# except TypeError as e:
#     print(e)
# except EOFError as e:
#     print(e)
# except Exception as e:
#     print(e, "other exception")
# else:
#     print("Else statement")
# finally:
#     print("Execute always")

# my_list = [1,2,3,4]
#
# for item in my_list:
#     print(item)
#     if item == 4:
#         continue
# else:
#      print("fine")
#
# None
#
# while my_list:
#     print(my_list.pop())
# else:
#     print("gocha")


# if el:

# list_comp = [element for element in range(5)]
# set_comp = {element for element in range(5)}
# dict_comp = {element: element - 1 for element in range(5)}
# gen_exp = (element for element in range(5))
# pass

#
# def add_one(number):
#      y = number + 1
#      return y
#
#
# x = add_one(2)
# x
#
# a = []
#
# def add_to_list(l):
#     for x in range(0,3):
#         l.append(x)
#     return l
#
# b = add_to_list(a)
# a
# 3
#
# *a, b = 1, 2, 3, 4, 5
# a, *b = 1, 2, 3, 4, 5
# a, *b, c = 1, 2, 3, 4, 5
# pass


# def my_sum(my_integers): # * vs no *
#     result = 0
#     for x in my_integers:
#         result += x
#     return result
#
# list_of_integers = [1, 2, 3]
# print(my_sum(list_of_integers))
# print()

#
# def my_sum(a, b, *args):
#     result = 0
    # Iterating over the Python args tuple
    # for x in list(args):
    #     result += x
    # return result
# my_sum(1, 2, 3, 4, 5, 6)
#
# a, b, *c = 1, 2, 3, 4, 5
#
# print()


#
# def my_sum(*integers):
#     result = 0
#     for x in integers:
#         result += x
#     return result
#
# print(my_sum(1, 2, 3))


# integers type is tuple

# def concatenate(*args, **kwargs):
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for arg in kwargs.values():
#         result += arg
#     return result

# concatenate("1", "2", a="Real", b="Python", c="Is", d="Great", e="!")
# concatenate(fz_dict)
# fz_dict = {"f": 1, "z": 2, "za": 123}
# my_dict = {'a': 'Real', 'b': 'Python', 'c': 'Is', 'd': 'Great', 'e': '!'}
#
# dict(a=1, b=2)
# new_dict = dict(**fz_dict, **my_dict)
# concatenate(**fz_dict, **my_dict)
# concatenate(f=1, z=2, kwargs=my_dict)

# def my_func(a, b, *, **kwargs):
#     print(a, b, kwargs)

# my_func(1, 2, 3, 4, a=56)
# pass
# list1 = [1, 2, 3]
# list2 = [4, 5]
# list3 = [6, 7, 8, 9]
#
# sum(*list1, *list2, *list3)
#
# my_tuple = 1, 3, 4
#
# a,b,c = my_tuple
# a, *b = my_tuple

# a = [*"RealPython"]


# houses = ["Misha's house", "Darya's house", "Olen house", "Max's house", "Best house"]

# Each function call represents an elf doing his work
# def deliver_presents_recursively(houses):
#     # Worker elf doing his work
#     if len(houses) == 1:
#         house = houses[0]
#         print("Delivering presents to", house)
#
#     # Manager elf doing his work
#     else:
#         mid = len(houses) // 2
#         first_half = houses[:mid]
#         second_half = houses[mid:]
#
# #         # Divides his work among two elves
#         deliver_presents_recursively(first_half)
#         deliver_presents_recursively(second_half)
# #
# deliver_presents_recursively(houses=houses)
# def factorial_recursive(n):
    # Base case: 1! = 1
    # if n == 1:
    #     return 1

    # Recursive case: n! = n * (n-1)!
    # else:
    #     return n * factorial_recursive(n-1)
#
# x = factorial_recursive(10)

#
def identity(x):
     return x
a = lambda x: x + 1
#
# a = filter(lambda arg, arg_2: arg if arg > 1 else "Fine" if arg > 2 else "Good", [1,2,3])


pass

# def my_func():
#     a = lambda: 1
#     b = lambda: 2
#     def my_inner_func():
#         a()
#
# def get_network_name(network_name):
#     if network_name == "facebook":
#         return lambda: "facebook"
#     elif network_name == "google":
#         return lambda: "google"
#
# def get_network_func(network_name):
#     return {
#         "facebook": lambda : "facebook",
#         "google": lambda : "google",
#     }.get(network_name, lambda: "Unused network")
#
# for network in ("snap", "google"):
#     get_network_func(network_name=network)()

#
# (lambda x: x + 1)(2)
# # 3
#
# add_one = lambda x: x + 1
# add_one(2)
# # 3
# a=3
# def add_one(x):
#     global a
#     def abc(a, b, c):
#
#         return a, b, c
#     a = a + 1
#     return x + 1
#
# sum()
# str
# list


# b = 6
# def f1(a):
#     print(a)
#     print(b)
# f1(a=12)
#
# b = 6
#
# def f1(a):
#     print(a)
#     print(b)
#
#     def f2():
#         c = a + b
#         return c * 3
#
#     return f2()
#
# print(f1(a=12))

#
# a = 5
# def function():
#     print(a)
    # a = 10
# function()
# print()
#
# a = 5
# def function():
#     global a
#     print(a)
#     a = 10
# function()

#
# a = 1
# def f1():
#     a = 1
#     b = 2
#     global a
#
#     def f2():
#         # a += b
#         nonlocal a
#         a = a + b
#         return a
#
#     return f2()
#
#
# f1()
# def facebook_processor(name, age, male=None):
#     return f"{name}, {age}"


# def get_network_func(network_name, **kwargs):
#     return {
#         "facebook": lambda : facebook_processor(name="Mark", age=30, **kwargs),
#         "google": lambda : "google",
#     }.get(network_name, lambda: "Unused network")
#
# get_network_func(network_name="facebook")(male="MAN")



def a():
     return 1


def b():
     return 1


class A:
     pass


{"A": 1, "A": 1}