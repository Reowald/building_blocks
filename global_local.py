x = 6

# this is all within the script

def example():
    global x
    z = 5
    print(x)
    print(x + 5)
    x += 1
    print(x)


example()

x = 6


def example():

    globx = x
    print(globx)
    globx += 5

    return globx


example()