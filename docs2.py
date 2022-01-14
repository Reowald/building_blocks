import asyncio
import datetime


async def display_date(time: float, reference: str):
    loop = asyncio.get_running_loop()
    end_time = loop.time() + time
    output = []
    while True:
        t = datetime.datetime.now()
        output.append(t)
        print(t, reference)

        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)
    return output


async def main():

    task1 = asyncio.create_task(display_date(10, 'id 1'))
    task2 = asyncio.create_task(display_date(3.0, 'id 2'))
    a = await asyncio.gather(task1)
    b = await asyncio.gather(task2)

    print('asyncio task has now completed. below is data gathered from the tasks')

    print(type(a))
    print(type(b))
    print(a)
    print(b)

    # another way to do the above is as below
    c = await asyncio.gather(
        display_date(1.5, 'id 3'),
        display_date(6, 'id 4'),
        display_date(0.25, 'id 5'),
        display_date(0.5, 'id 6'))

    print(c)
    print(len(c))


# asyncio.run(display_date())

asyncio.run(main())
