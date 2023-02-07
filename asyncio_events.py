import asyncio
import aiohttp
import random
import logging
import time
import signal
from collections import deque, Counter
import functools
import time
logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger()


class Agent:
    def __init__(self, org, _id):
        self.org = org
        self._id = _id
        self.task_count = 0

    async def work(self):
        log.debug(f'Agent {self._id} started his work')
        queue = self.org.task_queue
        event = self.org.event
        self.task_count = 0
        while True:
            await event.wait()
            task = await queue.get()
            try:
                delay = random.uniform(0.01, 2)
                await asyncio.sleep(delay)
                task_id, status = task
                entrance = await self.org.get_entrance()
                log.debug(f'Agent {self._id}, has got task with id {task_id},'
                          f' {status} one. Serving at entrance {entrance}')
                if status == 'bad':
                    log.debug(f'Agent {self._id} wait for blocked event')

                    if event.is_set():
                        await asyncio.sleep(5)
                        event.clear()
                        try:
                            if entrance not in self.org.banned_entrances:
                                self.org.banned_entrances.append(entrance)
                                log.debug(f'Stopped BY {self._id}! '
                                          f'Switching "{entrance}" entrance')
                                swapped = await self.org.swap_entance(entrance)
                                log.debug(f'new entrance is: {swapped}')
                            else:
                                log.debug('Skipping')
                        finally:
                            event.set()
                        log.debug('released')
                    task[1] = 'good'
                    await queue.put(task)
                    log.debug('PUT!')
                    continue
                self.task_count += 1

            except IndexError:
                log.debug(f'We are out of free entrances')
                await queue.put(task)
                event.clear()
            finally:
                if task:
                    queue.task_done()
        # log.debug(f' Agent {self._id} finished his job')


class Organization:
    def __init__(self, entrances, tasks_queue, concurrency):
        self.event = asyncio.Event()
        self.lock = asyncio.Lock()
        self.entrances = deque(entrances)
        self.task_queue = tasks_queue
        self.concurrency = concurrency
        self._working_entrance = None
        self.banned_entrances = []
        self.need_to_change_entrance = False
        self.agents = []
        self.lock_delay = concurrency * 0.05
        self.running = False

    async def get_entrance(self, force=False):
        with await self.lock:
            if self._working_entrance is None or force:
                self._working_entrance = self.entrances.popleft()
            return self._working_entrance


    async def swap_entance(self, entrance):
        await asyncio.sleep(0.001)
        try:
            self._working_entrance = self.entrances.popleft()
        except IndexError:
            self._working_entrance = None
            raise
        return self._working_entrance

    async def start_work(self):
        self.event.set()
        tasks = []
        self.running = True
        for i in range(self.concurrency):
            agent = Agent(self, i)
            self.agents.append(agent)
            tasks.append(asyncio.ensure_future(agent.work()))

        sched = asyncio.ensure_future(self.status_scheduler())
        await self.task_queue.join()

        print(self.task_queue.qsize())

        self.running = False
        self.get_status()

        log.debug('JOB DONE')
        log.debug(f'Banned entrances: {self.banned_entrances}')

        for task in tasks:
            if not task.done():
                task.cancel()

        if not sched.done():
            sched.cancel()

    def get_status(self):
        finished_tasks = sum(agent.task_count for agent in self.agents)
        tasks_by_agents = {f'Agent {agent._id}': agent.task_count
                           for agent in self.agents}
        log.debug(f'TOTAL FINISHED TASKS: {finished_tasks}')
        log.debug(f'Tasks by agents: {tasks_by_agents}')

    async def status_scheduler(self):
        while self.running:
            self.get_status()
            await asyncio.sleep(10)


if __name__ == '__main__':
    options = ['good', 'bad', 'not bad', 'something']


    tasks = [
        [0, 'good'], [1, 'bad'], [2, 'good'], [3, 'good'], [4, 'bad'],
        [5, 'good'], [6, 'good'], [7, 'good'], [8, 'good'], [9, 'good'],
        [10, 'good'], [11, 'good'], [12, 'good'], [13, 'good'], [14, 'bad'],
        [15, 'bad'], [16, 'bad'], [17, 'good'], [18, 'good'], [19, 'bad'],
        [20, 'good'], [21, 'good'], [22, 'bad'], [23, 'bad'], [24, 'good'], [
            25, 'good'], [26, 'good'], [27, 'good'], [28, 'bad'], [29, 'good'],
        [30, 'good'], [31, 'bad'], [32, 'bad'], [33, 'bad'], [34, 'bad'],
        [35, 'bad'], [36, 'bad'], [37, 'good'], [38, 'good'], [39, 'good'],
        [40, 'good'], [41, 'good'], [42, 'good'], [43, 'good'], [44, 'bad'],
        [45, 'bad'], [46, 'good'], [47, 'good'], [48, 'good'], [49, 'bad']
    ]
    # tasks = [[x, random.choice(options)] for x in range(50)]

    task_statuses = [x[1] for x in tasks]
    counter = Counter(task_statuses)
    log.info(counter)

    entrances = ['A', 'B', 'C', 'D', 'E', 'F']
    # entrances = ['A', 'B']

    concurrency = 10
    tasks_queue = asyncio.Queue()
    for task in tasks:
        tasks_queue.put_nowait(task)

    start = time.time()
    org = Organization(entrances, tasks_queue, concurrency)

    loop = asyncio.get_event_loop()


    def stop(loop):
        for task in asyncio.Task.all_tasks():
            if not task.done():
                task.cancel()
        loop.stop()


    def ask_exit(signame):
        print("got signal %s: exit" % signame)
        for task in asyncio.Task.all_tasks():
            if not task.done():
                task.cancel()
        stop(loop)

    for signame in ('SIGINT', 'SIGTERM'):
        loop.add_signal_handler(
            getattr(signal, signame),
            functools.partial(ask_exit, signame)
        )

    try:
        loop.run_until_complete(org.start_work())
    finally:
        loop.close()

    end = time.time()

    log.info(f'Time spent {end - start}')