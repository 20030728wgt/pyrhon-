with open('../new wenjian/wen.txt', mode='rb') as f:
    f.seek(0, 2)
    while 1:
        res = f.readline()
        if res:
            print(res.decode('utf-8'))
        time.sleep(0.2)

