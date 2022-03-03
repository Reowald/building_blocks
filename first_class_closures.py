


def outer_f(msg):
    def inner_f():
        print(msg)
    return inner_f




first = outer_f('first')
second = outer_f('2nd')

# each of the variables can remember
first()
second()


