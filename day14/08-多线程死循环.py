# 多线程
import threading


def test():
    while True:
        pass


t1 = threading.Thread(target=test)
t1.start()


# 主线程死循环
while True:
    pass

