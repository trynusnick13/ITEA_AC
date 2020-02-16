from decorators import count_calls, do_twice

# @count_calls
# def say_whee():
#     print("Whee!")
#
#
# print(say_whee())
# print(say_whee())
# print(say_whee())


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


hi_adam = return_greeting("Adam")
print(hi_adam)
