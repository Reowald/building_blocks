# https://www.youtube.com/watch?v=QVdf0LgmICw

#LEGB

# x = 'global x'
# print(x)

import builtins
print(dir(builtins))

m = min([5 ,2, 4, 5, 6])

def test(z):
    # global x
    # y = 'local y'
    z = 'local x'
    # print(y)
    # print(x)
    print(z)

test('')
# print(y)
# print(x)
# print(z)

#enclosing

def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
# inner()
# print(x)