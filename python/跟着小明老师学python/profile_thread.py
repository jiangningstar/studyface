# coding=utf-8
# http://www.dongwm.com/ 小明老师的blog

# 了解python的全局解释锁（GIL）
# 在python入门之前 接触过很多人说 python的线程没多大用处，因为全局解释锁的存在  导致python的线程没有想象的那么理想。
# 因为平常工作的原因也很少用到线程，进程，协程之类的东西，其实在特定的环境下运用python的线程还是比较合适的


# python的同步机制

import time
from random import random
from threading import Thread, Semaphore

sema = Semaphore(3)  # 对公共资源设置访问次数


def foo(tid):
    with sema:
        print '{} acquire sema'.format(tid)
        wt = random() * 2
        time.sleep(wt)
    print '{} release sema'.format(tid)


threads = []

for i in range(5):
    t = Thread(target=foo, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()