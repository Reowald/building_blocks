import pcm_can_read
import threading

setup = pcm_can_read.can_config('can0', '500000')

data = []

def data_read():
    try:
        while True:
            msg = setup.recv()
            message_received = pcm_can_read.status(msg)
            # data.append(message_received)
            data.append(message_received)
            return message_received

    except KeyboardInterrupt:
        print("keyboard interrupt!! YOU stopped the program")

    with open('data.txt', 'w') as f:
        for item in data:
            f.write("%s\n" % item)


pcm_can_read.close_can('can0')
