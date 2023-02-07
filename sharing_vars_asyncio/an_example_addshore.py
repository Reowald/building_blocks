import asyncio


# Define 2 simple async methods that print numbers
async def print_ones(asyncState):
    while asyncState.should_print == 1:
        print(1)
        asyncState.counter = asyncState.counter + 1
        if asyncState.counter > 10:
            asyncState.should_print = 0
        await asyncio.sleep(0.1)


async def print_twos(asyncState):
    while asyncState.should_print == 1:
        print(2)
        asyncState.counter = asyncState.counter + 1
        if asyncState.counter > 10:
            asyncState.should_print = 0
        await asyncio.sleep(0.1)


# Define a main async method (our program)
async def program():
    # Setup an object to track our state in
    asyncState = type('', (), {})()
    asyncState.should_print = 1
    asyncState.counter = 0

    # Run both print method and wait for them to complete (passing in asyncState)
    await asyncio.gather(print_ones(asyncState), print_twos(asyncState))

    # Once both are complete print done
    print("done")


# Run our program until it is complete
loop = asyncio.get_event_loop()
loop.run_until_complete(program())
loop.close()