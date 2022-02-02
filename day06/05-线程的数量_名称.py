import time
import threading


# 唱歌的函数
def sing():
    for i in range(5):
        print("正在唱歌...", threading.current_thread())
        time.sleep(0.5)


# 跳舞的函数
def dance():
    for i in range(5):
        print("正在跳舞..........", threading.current_thread())
        time.sleep(0.5)


# 调用
if __name__ == '__main__':

    # threading.current_thread()当前的线程对象
    print(threading.current_thread())

    # threading.enumerate()可以获取当前活跃的线程列表
    thread_list = threading.enumerate()
    print("1.当前线程数量：", len(thread_list))

    # 创建对象
    thread_sing = threading.Thread(target=sing)
    thread_dance = threading.Thread(target=dance)

    thread_list = threading.enumerate()
    print("2.当前线程数量：", len(thread_list))

    # 启动子线程
    thread_sing.start()
    thread_dance.start()

    while True:
        thread_list = threading.enumerate()
        print("3.当前线程数量：", len(thread_list))
        thread_num = len(thread_list)

        # 判断是否只剩下主线程就中止
        if thread_num <= 1:
            break
        time.sleep(0.5)

