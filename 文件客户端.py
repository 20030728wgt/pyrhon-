import socket
import json


def receive_file(sock):
    header_size = int(sock.recv(4).decode('utf-8'))
    if not header_size:  # 处理连接断开的情况
        print('连接已断开')
        sock.close()
        return

    header_json = sock.recv(header_size).decode('utf-8')
    header = json.loads(header_json)
    file_name = header['file_name']
    file_size = header['file_size']

    with open('客户端文件.txt', 'wt') as f:
        received_size = 0
        while received_size < file_size:
            data = sock.recv(1024)
            if not data:  # 处理连接断开的情况
                print('连接已断开')
                sock.close()
                return
            f.write(data.decode('utf-8'))
            received_size += len(data)
        print('文件传输完毕')


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

while True:
    res = input('请输入文件命令>>>').strip()
    if not res:
        continue
    client.send(res.encode('utf-8'))
    if res == 'get':
        receive_file(client)
