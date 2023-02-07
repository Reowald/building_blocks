from itertools import cycle
import asyncio

def endless():
    yield from cycle((9, 8, 7, 6))


e = endless()

total = 0

for i in e:
    if total < 30:
        print(i, end="")
        total += 1
    else:
        print()

        break


# >>> console next(e) e is still availble = is being genetrated

async def mygen(u: int = 10):
    """Yield powers of 2."""
    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        print(i)
        await asyncio.sleep(0.1)


async def main():
    g = [i async for i in mygen()]
    f = [j async for j in mygen() if not (j // 3 % 5)]
    return g, f

g, f = asyncio.run(main())

