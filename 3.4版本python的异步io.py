import asyncio
import time
from threading import current_thread


# python3.4
@asyncio.coroutine
def f1():
    print('f1 start', current_thread())
    yield from asyncio.sleep(1)
    print('f1 end', current_thread())


@asyncio.coroutine
def f2():
    print('f2 start', current_thread())
    yield from asyncio.sleep(1)
    print('f2 end', current_thread())


tasks = [f1(), f2()]
loop = asyncio.get_event_loop()  # 产⽣（获取）⼀个事件循环
loop.run_until_complete(asyncio.wait(tasks))
