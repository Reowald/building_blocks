import threading

x = [12.7, 12.5, 34, 56, 85]

def thread_task(num, lock):
    global x
    lock.acquire()
    for i in range(len(x)):
        x[i] += num
    lock.release

def main_task():
    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args=(2, lock))
    t2 = threading.Thread(target=thread_task, args=(4, lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == '__main__':
    main_task()
    print('{}'.format(x))
