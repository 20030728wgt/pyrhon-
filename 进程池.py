from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

# pool = ThreadPoolExecutor(10) # 不传参的话，默认开设的线程数量，是当前cpu的个数乘以5
pool = ProcessPoolExecutor(10)  # 不传参的话，默认开设的进程数量，是当前cpu的个数


def task(name):
    print(name)
    time.sleep(3)
    return name + 10


def call_back(res):  # res自动调用future
    print('结果', res.result())


if __name__ == '__main__':
    for i in range(10):
        pool.submit(task, i).add_done_callback(call_back)
