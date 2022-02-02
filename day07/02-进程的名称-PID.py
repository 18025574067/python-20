"""
1、导入模块
2、通过模块提供的Process类创建对象
3、启动进程


"""
import time
import multiprocessing
import os


def work1():
    for i in range(10):
        # print("正在打印 work1...", multiprocessing.current_process())
        # 获取进程的编号
        # print("正在打印 work1...", multiprocessing.current_process().pid)
        # print("正在打印 work1...", os.getpid())
        # 获取进程的父ID
        print("正在打印 work1...", i, os.getpid(), "父ID：", os.getppid())

        time.sleep(2)


if __name__ == '__main__':

    print(multiprocessing.current_process())

    # 获取进程编号：process.pid
    # 1) multiprocessing.current_process().pid
    # print("主进程编号：", multiprocessing.current_process().pid)
    # 2)使用OS模块获取编号
    print("主进程编号：", os.getpid())

    # 1、导入模块
    # 2、通过模块提供的Process类创建对象
    # target指定子进程要执行的分支函数
    # name修改子进程的名称
    process_obj = multiprocessing.Process(target=work1, name="P1")
    # 3、启动进程
    process_obj.start()

    print("xxxxxx")



