# https://realpython.com/primer-on-python-decorators/

# def hi(name):
#     return f'Some {name}'
#
# def nice(name):
#     return f'Some {name} and continued'
#
# def greet(greet_func):
#     return greet_func('bob')
#
#
# print(greet(hi))
# print(greet(nice))
# print(hi('Josh'))

# def parent():
#     print("Printing from the parent() function")
#
#     def first_child():
#         print("Printing from the first_child() function")
#
#     def second_child():
#         print("Printing from the second_child() function")
#
#     second_child()
#     first_child()
#
#
# parent()
# # first_child()

# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#
#
# first = parent(1)
# second = parent(2)
#
# print(first)
# print(second)
#
# print(first())
# print(second())

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# def say_whee():
#     print("Whee!")
#
#
# say_whee = my_decorator(say_whee)
#
# print(say_whee())

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)

print(say_whee())