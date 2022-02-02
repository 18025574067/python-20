"""
1、创建一个函数，用于拷贝文件

2、创建一个进程池，长度为3（表示进程池最多能创建3个进程）

3、利用进程池同步方式拷贝文件

4、利用进程池异步工作方式拷贝文件

"""
import time
import multiprocessing


# 1、创建一个函数，用于拷贝文件
def copy_work():
    print("正在拷贝文件.......", multiprocessing.current_process())
    time.sleep(0.5)


if __name__ == '__main__':

    # 2、创建一个进程池，长度为3（表示进程池最多能创建3个进程）
    # 创建进程池，有两步：
    # 1）导入模块
    # 2）创建进程池 multiprocessing.pool(2) 最大允许创建2个进程
    pool = multiprocessing.Pool(3)

    for i in range(10):
        # copy_work()
        # 3、利用进程池同步方式拷贝文件
        # pool.apply(函数名，(函数参数1, 参数2....))
        # pool.apply(copy_work)
        # 4、利用进程池异步工作方式拷贝文件
        # 如果使用apply_async 方式，需要做到2点
        # 1）pool.close()表示进程池不再接收新的进程
        # 2）主进程不再等待进程池执行结束再退出，需要进程池join()
        #     pool.join()让主进程等待进程池执行结束再结束
        pool.apply_async(copy_work)

    # pool.close()表示进程池不再接收新的进程
    pool.close()
    # pool.join()让主进程等待进程池执行结束再结束
    pool.join()
