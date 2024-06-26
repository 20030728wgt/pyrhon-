
import socket
import asyncio
# import uvloop
#
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())  #不支持windows系统在linux上可以使用极大提高效率


async def waiter(conn, loop):
    while True:
        try:
            data = await loop.sock_recv(conn, 1024)
            if not data:
                break
            await loop.sock_sendall(conn, data.upper())
        except ConnectionResetError:
            break
    conn.close()


async def main(ip, port):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip, port))
    server.listen(5)
    server.setblocking(False)
    loop = asyncio.get_running_loop()
    while True:
        conn, addr = await loop.sock_accept(server)
        # 创建task任务
        loop.create_task(waiter(conn, loop))


asyncio.run(main('localhost', 8081))

# FastAPI Django3....


# 实战
# 在线聊天室，进程+线程+协程，提高并发能力，自动更新，负载均衡
