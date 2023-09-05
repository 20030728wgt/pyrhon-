import socket
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 5002))
server.listen(5)
print('建立成功端口为5002的服务端，等待客户端连接')
while True:
    conn, addr = server.accept()
    print('连接的客户端ip和端口', addr)
    while True:
        try:
            cmd = conn.recv(1024)
        except:
            break

        obj = subprocess.Popen(cmd.decode('utf_8'),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE
                               )
        out_res = obj.stdout.read()
        err_res = obj.stderr.read()
        data_size = len(out_res) + len(err_res)  # 数据总长度
        header = bytes(str(data_size), 'utf-8').zfill(4)
        conn.send(header)
        conn.send(out_res)
        conn.send(err_res)
        conn.close()
