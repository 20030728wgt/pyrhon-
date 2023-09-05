import asyncio
from threading import Thread, current_thread


async def recv():
    print('进⼊IO')
    await asyncio.sleep(3)
    print('结束IO')
    return 'hello'


async def f1():
    print('f1 start', current_thread())
    data = await recv()
    print('结果', data)
    print('f1 end', current_thread())


async def f2():
    print('f2 start', current_thread())
    data = await recv()
    print('结果', data)
    print('f2 end', current_thread())


tasks = [f1(), f2()]
asyncio.run(asyncio.wait(tasks))
