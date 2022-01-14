import pandas as pd


# sum_integers_list.py
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result


list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))


# sum_integers_args.py
def my_sum_arg(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result


print(my_sum_arg(1, 2, 3))

# change_list.py MUTABLE
my_list = [1, 2, 3]
my_list[0] = 9
print(my_list)

# # change_tuple.py IMUTABLE
# my_tuple = (1, 2, 3)
# my_tuple[0] = 9
# print(m


b = [1, 2, 3, 4, 5, 56, 6, 9]

def change_to(*numbers: int):
    a = str(numbers)
    return a

c = change_to(b)
print(c)



import pandas as pd
import numpy as np

d = {"jam_b": [0.0, 12, 66, 100], "PB": [1.00, 10, 68, 21], "Marms": [2.0, 55, 654, 14]}

print(d)
print(type(d))
print(len(d))

e = pd.Series(d)
f = pd.Series(e, index=['jam_b', 'PB', 'Marms'])

print(e)
print(type(e))
print(f)
print(type(f))
print(e['jam_b'])
print(e['PB'])
print(e['Marms'])

print(f)
print(type(f))

f = e['Marms']
print('length of f is ', len(f), 'and the type is', type(f[1]))


def add_something(data_input):
    for i in range(0, len(data_input)):
        data_input[i] = data_input[i] + 1
        print(data_input[i])
    return data_input


x = add_something(f)
print('The answer is', x)

# *args multiple aguments
# key word argyments IE a=1234

