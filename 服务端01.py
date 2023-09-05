import socket

# 1.创建客户端对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # sock_steam是tcp协议
# 2.建立连接
sk.bind(('127.0.0.1', 5001))
# 3.建立监听请求
sk.listen(5)  # 半连接池可以接5个请求
print('建立成功端口为5000的服务端，等待客户端连接')
# 4.取出连接请求开始服务
while True:
    conn, addr = sk.accept()
    print('连接的客户端ip和端口', addr)
    # 5.数据传输
    try:
        data = conn.recv(1024)
    except:
        break
    data = data.decode('utf-8')
    print('受到的数据', data)
    conn.send(data.upper().encode('utf-8'))
    # 6.结束服务
    conn.close()
