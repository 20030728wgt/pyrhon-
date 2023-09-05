from functools import wraps
import time

def login(x, y):
    z = x + y
    time.sleep(3)
    print('计算结果为:', z)
    return z


def number_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('时间为:', end - start)
        return res

    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper


login = number_func(login)
res = login(2, 32)
print(res)
