import asyncio
import random


class Demo:
    def __init__(self):
        self.ltp = 0

    async def one(self):
        while True:
            self.ltp += random.uniform(-1, 1)
            await asyncio.sleep(0.1)

    async def two(self):
        while True:
            print(self.ltp)
            await asyncio.sleep(0.1)


# loop = asyncio.get_event_loop()
# d = Demo()
# loop.create_task(d.one())
# loop.create_task(d.two())
# loop.run_forever()