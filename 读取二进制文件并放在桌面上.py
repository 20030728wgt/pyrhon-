with open(r'E:\桌面\wgt python\new wenjian\wen.txt', mode='rb') as f:
    for line in f:
        print(line.decode('UTF-8').strip('\n'))
with open(r'E:\桌面\wgt python\new wenjian\R-C.jpg', mode='rb') as f, \
        open('E:\桌面\小伙子.jpg', mode='wb') as f1:
    while 1:
        res = f.read(1024)
        if not res:
            break
        f1.write(res)
        print(res)
