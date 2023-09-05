import socket

# 1.创建客户端对象
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # sock_DGRAM是udp协议
sk.bind(('127.0.0.1', 5000))
while True:
    data, addr = sk.recvfrom(1024)
    print('受到的数据', data.decode('uft-8'))
    sk.sendto(data.upper(), addr)
