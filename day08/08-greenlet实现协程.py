"""
greentlet 实现协程步骤：
1、导入模块
2、创建任务：wrok1      work2
3、创建 greenlet 对象
4、手动 switch 任务


"""
import time
from greenlet import greenlet


# 1、创建 work1 的生成器
def work1():
    while True:
        print("正在执行 work1....")
        time.sleep(0.5)
        # 切换至第二个任务
        g2.switch()


# 2、创建 work2 的生成器
def work2():
    while True:
        print("正在执行 work2.................")
        time.sleep(0.5)
        # 切换到第一个任务
        g1.switch()


if __name__ == '__main__':
    # 创建 greenlet 对象
    # greenlet(函数名)
    g1 = greenlet(work1)
    g2 = greenlet(work2)

    # 执行work1任务
    g2.switch()




