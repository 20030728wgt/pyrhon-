

import asyncio
import socket
import time

"""
事件循环
自动监测并执行我们添加给它的任务

任务列表 = [任务a, 任务b......]
while True:
    可执行任务列表, 已完成任务列表 = 监测任务列表
    for 任务 in 可执行任务列表：
        执行任务
        
    for 任务 in 已完成任务列表：
        移除任务
        
    终止事件循环

"""

from threading import current_thread
import asyncio
import time
from threading import current_thread


# python3.4
# @asyncio.coroutine
# def f1():
#     print('f1 start', current_thread())
#     yield from asyncio.sleep(1)
#     print('f1 end', current_thread())
#
#
# @asyncio.coroutine
# def f2():
#     print('f2 start', current_thread())
#     yield from asyncio.sleep(1)
#     print('f2 end', current_thread())
#
#
# tasks = [f1(), f2()]
# loop = asyncio.get_event_loop()  # 产⽣（获取）⼀个事件循环
# loop.run_until_complete(asyncio.wait(tasks))


# python3.5     async/await
# async def f1():
#     print('f1 start', current_thread())
#     await asyncio.sleep(1)
#     print('f1 end', current_thread())
#
#
# async def f2():
#     print('f2 start', current_thread())
#     data = await asyncio.sleep(1)
#     print('结果', data)
#     print('f2 end', current_thread())
#
#
# tasks = [f1(), f2()]
# loop = asyncio.get_event_loop()    # 产生（获取）一个事件循环
# loop.run_until_complete(asyncio.wait(tasks))

# python3.7
# asyncio.run(asyncio.wait(tasks))


"""
await后面只能跟一种对象，可等待的对象（协程对象，task对象，future对象）
阻塞操作必须替换成相应的异步库提供的函数：
time.sleep() -> asyncio.sleep()
server.accept() -> loop.sock_accept()
conn.recv() -> loop.sock_recv()
第三方异步库
aiohttp
aiomysql
...
"""


#
# async def recv():
#     print('进入IO')
#     await asyncio.sleep(3)
#     print('结束IO')
#     return 'hello'
#
#
# async def f1():
#     print('f1 start', current_thread())
#     data = await recv()
#     print('结果', data)
#     print('f1 end', current_thread())
#
#
# async def f2():
#     print('f2 start', current_thread())
#     data = await recv()
#     print('结果', data)
#     print('f2 end', current_thread())
#
#
# tasks = [f1(), f2()]
# asyncio.run(asyncio.wait(tasks))

#
# import asyncio
#
#
# async def nested():
#     print('进入IO')
#     await asyncio.sleep(3)
#     print('结束IO')
#     return 42
#
#
# async def main(name):
#     print(name, 'start')
#     # Schedule nested() to run soon concurrently
#     # with "main()".
#     task = asyncio.create_task(nested())
#
#     # "task" can now be used to cancel "nested()", or
#     # can simply be awaited to wait until it is complete:
#     res = await task
#     print(res)
#
#
# async def main2(name):
#     print(name, 'start')
#     # Schedule nested() to run soon concurrently
#     # with "main()".
#     task = asyncio.create_task(nested())
#     task.cancel()
#
#     # "task" can now be used to cancel "nested()", or
#     # can simply be awaited to wait until it is complete:
#     res = await task
#     print(res)
#
#
# asyncio.run(asyncio.wait([main('任务1'), main2('任务2')]))


# import asyncio
#
#
# async def nested():
#     print('进入IO')
#     await asyncio.sleep(3)
#     print('结束IO')
#     return 42
#
#
# async def main(name):
#     print(name, 'start')
#     # Schedule nested() to run soon concurrently
#     # with "main()".
#     task_list = [
#         asyncio.create_task(nested(), name='a'),
#         asyncio.create_task(nested(), name='b')
#     ]
#
#     # "task" can now be used to cancel "nested()", or
#     # can simply be awaited to wait until it is complete:
#     done, pending = await asyncio.wait(task_list)
#     print(done)
#     print(pending)
#     for task in done:
#         print(task.result(), task.get_name())
#
#
# asyncio.run(main('任务1'))


# import asyncio
#
#
# async def nested():
#     print('进入IO')
#     await asyncio.sleep(3)
#     print('结束IO')
#     return 42
#
#
# task_list = [
#     nested(),
#     nested(),
# ]
#
#
# done, pending = asyncio.run(asyncio.wait(task_list))
# print(done)


# Future对象

# async def f1(future):
#     await asyncio.sleep(3)
#     future.set_result('hello')
#
#
# async def main():
#     loop = asyncio.get_running_loop()
#     future = loop.create_future()
#     loop.create_task(f1(future))
#     res = await future
#     print(res)
#
#
# asyncio.run(main())


# def f1(x):
#     time.sleep(3)
#     return 'hello'
#
#
# async def main():
#     loop = asyncio.get_running_loop()
#     future = loop.run_in_executor(None, f1, 'xxx')
#     res = await future
#     print(res)
#
#
# asyncio.run(main())


# 迭代器
# class MyRange(object):
#     def __init__(self, start, end=None):
#         if end:
#             self.count = start - 1
#             self.end = end
#         else:
#             self.count = -1
#             self.end = start
#
#     def add_count(self):
#         self.count += 1
#         if self.count == self.end:
#             return None
#         return self.count
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         value = self.add_count()
#         if value is None:
#             raise StopIteration
#         return value
#
#
# for i in MyRange(10):
#     print(i)


# 异步迭代器
# class MyRange(object):
#     def __init__(self, start, end=None):
#         if end:
#             self.count = start - 1
#             self.end = end
#         else:
#             self.count = -1
#             self.end = start
#
#     async def add_count(self):
#         await asyncio.sleep(1)
#         self.count += 1
#         if self.count == self.end:
#             return None
#         return self.count
#
#     def __aiter__(self):
#         return self
#
#     async def __anext__(self):
#         value = await self.add_count()
#         if value is None:
#             raise StopAsyncIteration
#         return value
#
#
# async def main():
#     async for i in MyRange(10):
#         print(i)
#
#
# asyncio.run(main())

# 上下文管理器
# class Client(object):
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#
#     def recv(self):
#         pass
#
#     def __enter__(self):
#         self.c = socket.socket()
#         self.c.connect((self.ip, self.port))
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.c.close()
#
#
# with Client('127.0.0.1', 8080)as f:
#     f.recv()


# 异步上下文管理器
# class Client(object):
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#         self.loop = asyncio.get_running_loop()
#
#     async def recv(self):
#         data = await self.loop.sock_recv(self.c, 1024)
#         return data
#
#     async def send(self, data):
#         await self.loop.sock_sendall(self.c, data.encode('utf-8'))
#
#     async def __aenter__(self):
#         self.c = socket.socket()
#         # self.c.connect((self.ip, self.port))
#         # 异步连接服务端
#         await self.loop.sock_connect(self.c, (self.ip, self.port))
#         return self
#
#     async def __aexit__(self, exc_type, exc_val, exc_tb):
#         self.c.close()
#
#
# async def main():
#     async with Client('127.0.0.1', 8081) as f:
#         while True:
#             await f.send('abc')
#             data = await f.recv()
#             print(data)
#
#
# asyncio.run(main())

# uvloop
