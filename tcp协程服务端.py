from gevent import monkey

monkey.patch_all()
import socket
# from multiprocessing import Process
# from threading import Thread
from gevent import spawn


def run(ip, port):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen(5)
    print('建立服务器')
    while True:
        conn, addr = s.accept()
        print('建立连接')
        spawn(task, conn)


def task(conn):
    # 通信循环
    while True:
        try:
            data = conn.recv(1024)
        except:
            break
        if not data:
            break
        print(data.decode('utf-8'))
        conn.send(data.upper())
        print('传输完毕')
    conn.close()


if __name__ == '__main__':
    g = spawn(run, '127.0.0.1', 5051)
    g.join()
