# try:
#     int(input())
# except Exception as e:
#     print(e)
# else:
#     print("else")
# finally:
#     print("fin")
#
#
my_list = [1,2,3,4]
#
# for item in my_list:
#     print(item)
#     if item == 3:
#         break
#     print("fine")
# else:
#     pass
#
# while my_list:
#     my_list.pop()
#
list_comp = [el for el in range(5)]
set_comp = {el for el in range(5)}
dict_comp = {el: el for el in range(5)}
gen_comp = {el for el in range(5)}
pass
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
# def my_sum(my_integers):
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
#     # Iterating over the Python args tuple
#     for x in list(args):
#         result += x
#     return result
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

# def concatenate(f, z, **kwargs):
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for arg in kwargs.values():
#         result += arg
#     return result
#
# fz_dict = {"f": 1, "z": 2, "za": 123}
# my_dict = {'a': 'Real', 'b': 'Python', 'c': 'Is', 'd': 'Great', 'e': '!'}
#
# new_dict = dict(**fz_dict, **my_dict)
# concatenate(**fz_dict, **my_dict)
# concatenate(f=1, z=2, kwargs=my_dict)
#
# my_tuple = 1, 3, 4
#
# a,b,c = my_tuple
# a, *b = my_tuple

# a = [*"RealPython"]


houses = ["Misha's house", "Darya's house", "Olen house", "Max's house"]

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
#         # Divides his work among two elves
#         deliver_presents_recursively(first_half)
#         deliver_presents_recursively(second_half)
#
# deliver_presents_recursively(houses=houses)
#
# def identity(x):
#      return x
#
# a = lambda x: x
#
# lambda x: x + 1
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
#     a = 10
# function()
# print()
#
# a = 5
# def function():
#     global a
#     print(a)
#     a = 10
# function()


def f1():
    a = 1
    b = 2

    def f2():
        # a += b
        nonlocal a
        a = a + b
        return a

    return f2()


f1()
