# this is for a deprecated module
import _thread
import time

def print_epoch(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "-----------", time.time())


try:
    _thread.start_new_thread(print_epoch, ("thread 1", 2))
    _thread.start_new_thread(print_epoch, ("thread 2", 4))
except:
    print('This is an error')

#provides a mechanism for the thread creation before script execution completes
# input()

while 1:
    pass

