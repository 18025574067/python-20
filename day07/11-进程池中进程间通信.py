"""
思路：
1、准备两个进程
2、准备一个队列，一个进程向队列写入数据，然后传递到另一个进程
3、另外一个进程读取数据

"""
import time
import multiprocessing


# 1、写入到队列数据的函数
def write_queue(queue):

    # for循环，向队列写入数据
    for i in range(10):
        if queue.full():
            print("队列已满！")
            break

        # 向队列写入值
        queue.put(i)
        print("写入成功，已经写入：", i)
        time.sleep(0.5)


# 2、读取队列数据并显示的函数
def read_queue(queue):

    while True:
        # 判断队列是否为空
        if queue.qsize() == 0:
            print("队列为空！")
            break

        # 从队列读取数据
        value = queue.get()
        print("已经读取：", value)


if __name__ == '__main__':

    # 1、创建进程池
    pool = multiprocessing.Pool(2)

    # 2、创建进程池中的队列
    queue = multiprocessing.Manager().Queue(5)

    # 3、进程池间进行通信
    #   3.1 同步方式
    # pool.apply(write_queue, (queue, ))
    # pool.apply(read_queue, (queue, ))

    #   3.2 异步方式
    # apply_async()返回值ApplyResult对象，该对象有一个wait()方法
    # wait()方法类似于join(), 先让当前进程执行完毕，再继续其他进程
    result = pool.apply_async(write_queue, (queue, ))
    result.wait()

    pool.apply_async(read_queue, (queue, ))

    # close()表示不再接收新的任务
    pool.close()
    # join()表示主进程等等进程池结束再关闭
    pool.join()


