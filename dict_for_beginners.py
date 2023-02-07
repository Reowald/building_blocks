from typing import List

student = {'name': 'wah wah', 'courses': ['math', 'Science']}

print(student.get('phone', 'Not Found'))
print(student.get('name'))

student['phone'] = '555-555'
student['name'] = 'Jane'


print(student)
student.update({'name': 'JAX', 'age': 26, 'phone': '1648634-541'})
print(student)

student['name'] = 'new name'

print(student)


age = student.pop('age')

print(age)
print(len(student))
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

print('this is a good implementation')
for key, value in student.items():
    print(key, value)

print(type(student))

import collections



data_dict = collections.defaultdict(lambda : 'pid not avalible')

list_of_ids = [b'\x00\x10', b'\x01\x10', b'\x10\x10',
               b'\x11\x10', b'\x12\x10', b'\x13\x10']

respond_arbid = [268439810, 268444162]

respond_dict = {respond_arbid[i]: data_dict for i in range(len(respond_arbid))}

# Python code to demonstrate defaultdict

# importing "collections" for defaultdict
import collections

# declaring defaultdict
# sets default value 'Key Not found' to absent keys
defd = collections.defaultdict(lambda: 'Key Not found')

# initializing values
defd['a'] = 1

# initializing values
defd['b'] = 2

# printing value
print("The value associated with 'a' is : ", end="")
print(defd['a'])

# printing value associated with 'c'
print("The value associated with 'c' is : ", end="")
print(defd['c'])