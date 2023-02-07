import asyncio
import time
import random

lst = []

async def news_producer(my_queue):
    while True:
        await asyncio.sleep(1)
        print('Putting on new item')
        lst.append(random.randint(1, 100))
        await my_queue.put(random.randint(1, 100))


async def news_consumer(id, my_queue):
    while True:
        print(f'Consumer: {id}, attempting to get data from queue')
        item = await my_queue.get()
        if item is None:
            print('is none')
            break
        print(f'Consumer: {id} consumed article with item: {item}')


async def main():
    # lock = asyncio.Lock()
    my_queue = asyncio.Queue(loop=loop)
    # await asyncio.wait([news_producer(lock), news_producer(lock)])
    await asyncio.wait([news_producer(my_queue), news_consumer(1, my_queue), news_consumer(1, my_queue)])



loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print('Done')

loop.close()