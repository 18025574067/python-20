import threading


# 创建函数，根据下标获取元素值
def get_value(index):
    date_list = [1, 3, 5, 7, 9]
    # 上锁
    lock1.acquire()
    # 判断下标是否越界
    if index >= len(date_list):
        print("下标越界", index)
        # 释放锁
        lock1.release()
        return

    print(date_list[index])
    # 解锁
    lock1.release()


# 创建10个线程，观察资源的等待状态
if __name__ == '__main__':

    # 创建一把锁
    lock1 = threading.Lock()

    # 循环创建10个线程
    for i in range(10):
        t1 = threading.Thread(target=get_value, args=(i, ))
        t1.start()

