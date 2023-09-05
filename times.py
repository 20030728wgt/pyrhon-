import time
import datetime

a = time.time()
print(a)
res = time.localtime(a)
print(res)
# 时间计算
now_time = datetime.datetime.now() + datetime.timedelta(days=7)
print(now_time.replace(microsecond=0))
