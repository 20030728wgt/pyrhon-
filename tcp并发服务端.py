import socket
from multiprocessing import Process
from threading import Thread

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 5051))
s.listen(5)
print('建立服务器')


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
    while True:
        conn, addr = s.accept()
        print('建立连接')
        p = Process(target=task, args=(conn,))
        # p = Thread(target=task, args=(conn,))
        p.start()
