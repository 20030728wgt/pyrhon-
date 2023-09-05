import socket

# 1.创建客户端对象
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input('请输入数据>>>')
    sk.sendto(msg.encode('utf-8'), ('127.0.0.1', 5000))
    data, addr = sk.recvfrom(1024)
    print('收到的数据为', data.decode('utf-8'))

