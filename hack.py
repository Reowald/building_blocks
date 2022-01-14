import asyncio

response = 0
count = 0

# essentially a delay function
async def handle(x):
    # print('waiting...')
    await asyncio.sleep(1)
    return x

# the doing command
async def run():
    global response
    global count
    count = 0
    for number in range(1, 21):
        response = await handle(number)
        # print(response)
        if response % 2 == 0:
            count = count + 1
            # run wait_for_next "in background" instead of blocking flow:
            asyncio.ensure_future(wait_for_next(response))

# collects and reports data
async def wait_for_next(x):
    while response == x:
        print('waiting...\n',
              'Even numbers found is', count, '\n',
              'Total numbers processed', response, 'of ', x)
        await asyncio.sleep(0.5)
    print('done')

# running the task
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
