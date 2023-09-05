import socket

# 1.创建客户端对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.建立连接
sk.connect(('127.0.0.1', 5001))
# 3.传输数据
while True:
    msg = input('请输入数据>>>')
    if not msg:
        continue
    sk.send(msg.encode('utf-8'))
    data = sk.recv(1024)
    print('收到的数据为', data.decode('utf-8'))
    sk.close()
