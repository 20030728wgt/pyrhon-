import socket
import selectors


def accept(sever):
    conn, addr = sever.accept()
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn):
    try:
        data = conn.recv(1024)
        # if not data:
        #     conn.close()
        #     sel.unregister(conn)
        #     return
        conn.send(data.upper())
    except ConnectionError:
        conn.close()
        sel.unregister(conn)


sever = socket.socket()
sever.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sever.bind(('127.0.0.1', 8080))
sever.listen(5)
sever.setblocking(False)

sel = selectors.DefaultSelector()
sel.register(sever, selectors.EVENT_READ, accept)
while True:
    rlist = sel.select()
    for key, mask in rlist:
        callback = key.data  # data为可读函数
        callback(key.fileobj)  # fileobj是可读对象
