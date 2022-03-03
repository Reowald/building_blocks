import threading
import time


def print_epoch(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "-----------", time.time())


def print_cube(num):
    print("Cube = {}".format(num*num*num))

def print_sq(num):
    print("Square = {}".format(num*num))

if __name__ == "__main__":
    # t1 = threading.Thread(target=print_epoch, args=("Thread 1", 2))
    # t2 = threading.Thread(target=print_epoch, args=("Thread 2", 4))
    t1 = threading.Thread(target=print_cube, args=(2,))
    t2 = threading.Thread(target=print_sq, args=(2,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done")