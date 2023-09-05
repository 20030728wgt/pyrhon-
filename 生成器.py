def func():
    print('第一次')
    yield 1
    print('第二次')
    yield 2


res = func()
print(next(res))
print(next(res))
