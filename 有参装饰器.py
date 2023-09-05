from functools import wraps


def name_func(name):
    def number_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            print(name)
            res = func(*args, **kwargs)
            end = time.time()
            print('时间为:', end - start)
            return res

        return wrapper

    return number_func


@name_func('李白')
def login(x, y):
    z = x + y
    time.sleep(3)
    print('计算结果为:', z)
    return z


print(login(2, 3))



