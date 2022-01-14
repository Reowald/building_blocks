import asyncio
import time
import random


async def send(arb_id, msg):
    await asyncio.sleep(arb_id)
    return arb_id, msg

async def send_recv(arb_id, msg):
    await asyncio.sleep(arb_id)
    print(random.randint(0, 10))
    return arb_id, msg


async def main():
    # print(f"started at {time.strftime('%X')}")
    #
    # await say_after(1, 'hello')
    # await say_after(2, 'world')
    #
    # print(f"finished at {time.strftime('%X')}")

    task1 = asyncio.create_task(send(1, 'buffered message'))

    task2 = asyncio.create_task(send_recv(2, 'requested information'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
