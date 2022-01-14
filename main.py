import random
import time
import asyncio

# def print(name):
#     print(f'Hi, {name}')

requests = []
arb_id = 0
last_arb_id = 1
new_msg_recv = False

#if __name__ == '__main__':

while True:
    # time.sleep(1)
    print(len(requests))
    # print(new_msg_recv)
    arb_id = input('Enter an arbitration id: ')
    requests.append(arb_id)
    if last_arb_id == arb_id:
        print(True)
    last_arb_id = arb_id
    # if new_msg_recv:
    #     requests = [requests, int(arb_id)]
    #     print(f"New message received {arb_id}")
    #     last_arb_id = arb_id
    #     new_msg_recv = False
    # elif not new_msg_recv:
    #     requests = [requests, int(arb_id)]
    #     new_msg_recv = True
    # else:
    #     print('No message received!')
