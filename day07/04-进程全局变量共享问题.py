import time
import multiprocessing

# 定义全局变量
g_num = 10


# work1() 对全局变量累加
def work1():
    global g_num
    for i in range(10):
        g_num += 1

    print("-----------work1-------------", g_num)


# work2() 读取全局变量，如果能读取，说明能共享，如果不能读到，说明不能共享！
def work2():
    print("--------------work2-------------", g_num)


if __name__ == '__main__':

    p1 = multiprocessing.Process(target=work1)
    p1.start()

    p2 = multiprocessing.Process(target=work2())
    p2.start()

    time.sleep(3)

    print("--------------main-------------", g_num)
