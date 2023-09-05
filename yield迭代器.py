def fun():
    while 1:
        y = yield
        print('这次y的值为：', y)


res = fun()
print(next(res))
print(res.send(10))
