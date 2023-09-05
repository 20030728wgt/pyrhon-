import socket
import time
c = socket.socket()
c.connect(('127.0.0.1', 5051))
while True:
    c.send(b'hello')
    data = c.recv(1024)
    print(data.decode('utf-8'))
    time.sleep(2)