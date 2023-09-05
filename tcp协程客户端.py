import socket
import time
from threading import Thread, current_thread


def dic_c():
    c = socket.socket()
    c.connect(('127.0.0.1', 5051))

    n = 0
    while True:
        res = f'{current_thread().name} say {n}'
        c.send(res.encode('utf-8'))
        data = c.recv(1024)
        print(data.decode('utf-8'))
        n += 1


if __name__ == '__main__':
    for _ in range(100):
        Thread(target=dic_c).start()
