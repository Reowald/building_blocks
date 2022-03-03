import time
import multiprocessing
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f'Wait for {seconds}')
    time.sleep(seconds)
    return print(f'Done... {seconds}')


# do_something()
# do_something()

# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)
#
# #if __name__ == '__main__': for windows
# if __name__ == '__main__':
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        finish = time.perf_counter()
        print(f'Finished process in {round(finish - start, 5)} seconds(s)')
        # print(results)

# if __name__ == '__main__':
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         secs = [5, 4, 3, 2, 1]
#         results = [executor.submit(do_something, sec) for sec in secs]
#
#         for f in concurrent.futures.as_completed((results)):
#             print(f.result())
#
#         finish = time.perf_counter()
#         print(f'Finished process in {round(finish - start, 5)} seconds(s)')

processes = []

# if __name__ == '__main__': #for windows
#     for _ in range(10):
#         p = multiprocessing.Process(target=do_something, args=[1.5])
#         p.start()
#         processes.append(p)
#
#     for process in processes:
#         process.join()

finish = time.perf_counter()

# print(f'Finished process in {round(finish - start, 5)} seconds(s)')

