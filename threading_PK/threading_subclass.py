import threading
import time


def print_epoch(name_of_thread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(name_of_thread, "-----------", time.time())


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    # def run(self) -> None:
    def run(self):
        print('Start of thread', self.name)
        print_epoch(self.name, self.delay)
        print('End of thread', self.name)

if __name__ == "__main__":

    t1 = MyThread('thread - 1', 2)
    t2 = MyThread('thread - 2', 5)

    t1.start()
    t2.start()
    print(t1.getName())
    print(t2.getName())
    print(threading.active_count())
    print(threading.currentThread())
    print(threading.enumerate())

    t1.join()
    t2.join()

    print('Done')