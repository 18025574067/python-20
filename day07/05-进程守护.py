"""
1、导入模块
2、通过模块提供的Process类创建对象
3、启动进程


"""
import time
import multiprocessing


def work1():
    for i in range(10):
        print("正在打印 work1...")
        time.sleep(0.5)


if __name__ == '__main__':
    # 1、导入模块
    # 2、通过模块提供的Process类创建对象
    process_obj = multiprocessing.Process(target=work1)

    # 进程守护
    # 线程守护 setDaemon(True), 进程守护 daemon = True
    # 设置子进程 process_obj 守护主进程
    # process_obj.daemon = True

    # 3、启动进程
    process_obj.start()

    time.sleep(2)
    print("我要死～！")

    # terminate()终止子进程的执行
    process_obj.terminate()

    exit()

    print("xxxxxx")



