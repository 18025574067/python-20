"""
gevent 实现协程步骤：
1、导入模块
2、指派任务


"""
# 一般放在开头
from gevent import monkey
monkey.patch_all()

import gevent
import time


# 1、创建 work1 的生成器
def work1():
    while True:
        print("正在执行 work1....", gevent.getcurrent())
        time.sleep(0.5)
        # gevent.sleep(5)


# 2、创建 work2 的生成器
def work2():
    while True:
        print("正在执行 work2.................", gevent.getcurrent())
        time.sleep(0.5)
        # gevent.sleep(0.5)


if __name__ == '__main__':
    # 指派任务
    # gevent.spawn(函数名, 参数1, 参数2,...)
    g1 = gevent.spawn(work1)
    g2 = gevent.spawn(work2)

    # 让主线程等等协程结束再退出
    g1.join()
    # g2.join()



