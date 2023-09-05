from multiprocessing import Process
import time


def func(name):
    print(f'{name}任务开始')
    time.sleep(5)
    print(f'{name}任务执⾏完毕')


if __name__ == '__main__':
    p = Process(target=func, args=('写讲话稿',))
    p.start()
    print('主进程')
