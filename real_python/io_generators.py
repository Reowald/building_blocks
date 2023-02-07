import asyncio


@asyncio.coroutine
def py34_coro():
    """Generator-based coroutine"""
    # No need to build these yourself, but be aware of what they are
    s = yield from stuff()
    return s


async def py35_coro():
    """Native coroutine, modern syntax"""
    s = await stuff()
    return s


async def stuff():
    return 0x10, 0x20, 0x30


def gen():
    yield 0x10, 0x20, 0x30


g = gen()
print(g)
print(next(g))
