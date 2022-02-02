"""
1、创建一把互斥锁
2、在使用资源前进行资源锁定
3、资源使用结束后，要解锁资源

"""

# 看看work1线程对全局变量的修改，在work2中能否查看修改后的变化


import threading
import time


# 定义全局变量
g_num = 0


# work1
def work1():

    # 声明g_num是一个全局变量
    global g_num

    for i in range(1000000):
        # 上锁
        lock1.acquire()
        g_num += 1
        # 解锁
        lock1.release()

    print("work1.............", g_num)


# work2
def work2():

    # 声明g_num是一个全局变量
    global g_num
    for i in range(1000000):

        lock1.acquire()
        g_num += 1
        lock1.release()

    print("work2.............", g_num)  # g_num可以在多个线程中共享


# 创建两个子线程
if __name__ == '__main__':

    # 创建互斥锁
    lock1 = threading.Lock()

    # 创建2个子线程
    w1 = threading.Thread(target=work1)
    w2 = threading.Thread(target=work2)

    # 启动线程
    w1.start()
    w2.start()

    # 在t1和t2执行结束后打印g_num
    while len(threading.enumerate()) != 1:
        time.sleep(0.5)

    print("main................", g_num)


