from multiprocessing import Process, Lock
import time
import json
import random


# 查票
def search_ticket(name):
    # 读取⽂件，查询⻋票数量
    with open('data/tickets.json', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    print(f'⽤户{name}查询余票：{dic.get("tickets_num")}')


# 买票
def buy_ticket(name):
    with open('data/tickets.json', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    # 模拟⽹络延迟
    time.sleep(random.randint(1, 5))
    if dic.get('tickets_num') > 0:
        dic['tickets_num'] -= 1
        with open('data/tickets.json', 'w', encoding='utf-8') as f:
            json.dump(dic, f)
        print(f'⽤户{name}买票成功')
    else:
        print(f'余票不⾜，⽤户{name}买票失败')


def task(name, mutex):
    search_ticket(name)
    mutex.acquire()  # 抢锁
    buy_ticket(name)
    mutex.release()  # 释放锁


if __name__ == '__main__':
    mutex = Lock()
    for i in range(1, 9):
        p = Process(target=task, args=(i, mutex))
        p.start()
