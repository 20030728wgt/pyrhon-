from multiprocessing import Process
import time
def func(name, n):
    print(f'{name}任务开始')
    time.sleep(n)
    print(f'{name}任务执⾏完毕')
if __name__ == '__main__':
    start = time.time()
# p1 = Process(target=func, args=('写讲话稿1', 1))
# p2 = Process(target=func, args=('写讲话稿2', 2))
# p3 = Process(target=func, args=('写讲话稿 3', 3))
# p1.start()
# p2.start()
# p3.start()
# p1.join()
# p2.join()
# p3.join()
    l = []
    for i in range(1, 4):
        p = Process(target=func, args=(f'写讲话稿{i}', i))
        p.start()
        l.append(p)
    for p in l:
        p.join()
    print('主进程')
    end = time.time()
    print(end - start)