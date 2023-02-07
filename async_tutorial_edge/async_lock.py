import asyncio
import time



async def my_worker(lock):
    print('Obtain lock')
    async with lock:
        print('Locked')
        time.sleep(2)
    print('unlocked')


async def main():
    lock = asyncio.Lock()
    await asyncio.wait([my_worker(lock), my_worker(lock)])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print('Done')

loop.close()