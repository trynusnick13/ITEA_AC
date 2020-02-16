import functools

#
# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper_repeat(*args, **kwargs):
#             for _ in range(num_times):
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper_repeat
#     return decorator_repeat
#
# @repeat(num_times=4)
# def greet(name):
#     print(f"Hello {name}")
#
# greet("My name")
#


def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value

        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


@repeat
def say_whee():
    print("Whee!")


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


say_whee()
greet("Penny")
