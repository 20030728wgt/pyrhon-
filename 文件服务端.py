
import socket
import json
import os
from multiprocessing import process

def send_file(sock):
    data_size = os.path.getsize('服务端文件.txt')
    path_name = '服务端文件.txt'
    header = {
        'file_name': path_name,
        'file_size': data_size,
    }
    header_json = json.dumps(header)
    header_bytes = header_json.encode('utf-8')
    header_h = bytes(str(len(header_bytes)), 'utf-8').zfill(4)
    sock.send(header_h)
    sock.send(header_bytes)
    print('头文件传输完毕')

    with open('服务端文件.txt', mode='rb') as f:
        for line in f:
            sock.send(line)
        print('已将所有文件传输完毕')

def task(conn):
        while True:
            try:
                content = conn.recv(1024)
            except:
                break
            if content.decode('utf-8') == 'get':
                print('开始传输文件>>>')
                send_file(conn)
        conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8080))
server.listen(5)
print('建立连接')


if __name__ == '__main__':
    while True:
        conn, addr = server.accept()
        print('已接收客户端>>>')
        p = process(target = task,args = (conn,))
        p.start()

# while True:
#     conn, addr = server.accept()
#     print('已接收客户端>>>')
#     while True:
#         try:
#             content = conn.recv(1024)
#         except:
#             break
#         if content.decode('utf-8') == 'get':
#             print('开始传输文件>>>')
#             send_file(conn)
#     conn.close()
