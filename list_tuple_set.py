# https://www.youtube.com/watch?v=W8KRzm-HUcc


courses = ['history', 'math', 'physics', 'pogs']

# everything
print(courses[:])

# first is inclusisve but the second isn't
print(courses[0:4])

# this is called slcing
print(courses[2:3])

courses.append('ART')

courses.insert(1, 'geo')
print(courses)

other_courses = ('money', 'home')

courses.insert(0, other_courses)
print(courses)

print(courses[0])

courses = ['history', 'math', 'physics', 'pogs']

courses.extend(other_courses)
print(courses)

# append and extend and insert
courses.remove('math')

popped = courses.pop()
print(popped)

courses.reverse()
print(courses)

courses.sort()

print(courses)

nums = [1, 4, 5, 6, 7, 3, 5]

nums.sort()
print(nums)

courses.sort(reverse=True)
nums.sort(reverse=True)

# new list
new_course = sorted(courses)
new_nums = sorted(nums)

print(courses)
print(nums)

print(sum(nums))

print(min(nums))

print(courses.index('history'))
print(courses.index('money'))
#
addr = [b'\x00\x10', b'\x01\x10', b'\x10\x10', b'\x11\x10']

addr_pos = int.from_bytes(addr[3], 'little')
hex_addr = hex(addr_pos)

print(f'location of {hex_addr}')
print(addr.index(b'\x11\x10'))

print(b'\x11\x10' in addr)

print('for loop executed')

print('loops')

for item in courses:
    print(item)

for course in courses:
    print(course)

for index, course in enumerate(courses):
    print(index, course)

for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = ', '.join(courses)

print(course_str)


new_list = course_str.split(', ')
print(new_list)

## TUPLES immutable

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


#Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()

