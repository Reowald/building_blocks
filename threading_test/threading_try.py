import threading
import time
import random

p = [12.7, 12.5, 34, 56, 85]


def change_p():
    global p
    while True:
        for i in range(len(p)):
            p[i] = random.random()
            time.sleep(0.5)


def read_p():
    global p
    while True:
        for i in range(len(p)):
            print(p[i])
            time.sleep(1)



t1 = threading.Thread(target=read_p)
t2 = threading.Thread(target=change_p)

t1.start()
t2.start()

t1.join()
t2.join()