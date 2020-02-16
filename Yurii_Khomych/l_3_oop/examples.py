# class Foo:
#     pass
#
#
#
# obj = Foo()
# obj.__class__
# # <class '__main__.Foo'>
# type(obj)
# # <class '__main__.Foo'>
# obj.__class__ is type(obj)
# # True
#
# for t in int, float, dict, list, tuple:
#     print(type(t))
#
# type(type)
#
# type(3)
#
# type(["foo", "bar", "baz"])
# # <class 'list'>
#
# t = (1, 2, 3, 4, 5)
# type(t)
# # <class 'tuple'>
#
#
# class Foo:
#     pass
#
#
# type(Foo())
# my_func = lambda self, a: a
#
# Bar = type("Bar", (Foo,), {"a": 1, "my_func": my_func})
#
# bar = Bar()
# result_list = []
# for element in range(10):
#     Bar = type("Bar", (Foo,), {"element": element, "my_func": my_func})
#     bar = Bar()
#     bar.my_func()
#     result_list.append(bar)

#
# def my_decorator(func):
#     def wrapper():
#         wrapper.count += 1
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     wrapper.count = 0
#     return wrapper
#
# @my_decorator
# def say_whee():
#     print("Whee!")
#
# decorated_say_whee = my_decorator(say_whee)
# decorated_say_whee()
# print()
#
# import functools
#
#
# def do_twice(func):
#     @functools.wraps(func)
#     def wrapper_do_twice(*args, **kwargs):
#         res = func(*args, **kwargs)
#         func(*args, **kwargs)
#         return res
#     return wrapper_do_twice
#
#
# @do_twice
# @do_twice
# def return_greeting(name):
#     # __doc__ = """My doc"""
#     print("Creating greeting")
#     return f"Hi {name}"
#
# greeting = return_greeting("Sergey")
# print()

# import random
# PLUGINS = dict()
#
# def register(func):
#     """Register a function as a plug-in"""
#     PLUGINS[func.__name__] = func
#     return func
#
# @register
# def say_hello(name):
#     return f"Hello {name}"
#
# @register
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"
#
# def randomly_greet(name):
#     greeter, greeter_func = random.choice(list(PLUGINS.items()))
#     print(f"Using {greeter!r}")
#     return greeter_func(name)
#
# randomly_greet("Sergey")
#
# import functools
#
# def debug(func):
#     """Print the function signature and return value"""
#     @functools.wraps(func)
#     def wrapper_debug(*args, **kwargs):
#         args_repr = [repr(a) for a in args]                      # 1
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
#         signature = ", ".join(args_repr + kwargs_repr)           # 3
#         print(f"Calling {func.__name__}({signature})")
#         value = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {value!r}")           # 4
#         return value
#     return wrapper_debug

# @debug
# def make_greeting(name, age=None):
#     if age is None:
#         return f"Howdy {name}!"
#     else:
#         return f"Whoa {name}! {age} already, you are growing up!"
# make_greeting("Benjamin")
# make_greeting("Richard", age=112)
#
# @debug
# class TimeWaster:
#     def __init__(self, max_num):
#         self.max_num = max_num
#
#     def waste_time(self, num_times):
#         for _ in range(num_times):
#             sum([i**2 for i in range(self.max_num)])
#
# t = TimeWaster(1)
# t.waste_time(1)
# print()
#
# def repeat(_func=None, *, num_times=2):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper_repeat(*args, **kwargs):
#             for _ in range(num_times):
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper_repeat
#
#     if _func is None:
#         return decorator_repeat
#     else:
#         return decorator_repeat(_func)
# @repeat
# def say_whee():
#     print("Whee!")
#
# @repeat(num_times=3)
# def greet(name):
#     print(f"Hello {name}")
#
# say_whee()
# greet("Penny")
#
# import sqlalchemy


class BaseInsight:
    def __init__(self, api, period):
        self.api = api
        self.period = period

    def get_attribute_value(self, name):
        return "attribute value"


insight = BaseInsight(api=4, period=7)
attr_value = insight.get_attribute_value("attribute value")
print()
