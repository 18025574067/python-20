import time
import threading


# 唱歌的函数
def sing(a, b, c):
    print("参数：", a, b, c)
    for i in range(5):
        print("正在唱歌...")
        time.sleep(0.5)


# 跳舞的函数
def dance():
    for i in range(5):
        print("正在跳舞..........")
        time.sleep(0.5)


# 调用
if __name__ == '__main__':
    # 创建对象
    # 在线程中，传递参数有三种方式
    # 1、使用元组传递，threading.Thread(target=sing, args=(参数1, 参数2, ...))
    # thread_sing = threading.Thread(target=sing, args=(10, 20, 100))
    # 2、使用字典传递，threading.Thread(target=sing, kwargs={"参数名": "参数值", ...})
    # thread_sing = threading.Thread(target=sing, kwargs={"a": 10, "c": 100, "b": 20})
    # 3、混合元组和字典传递，threading.Thread(target=sing, args=(参数1, 参数2, ...), kwargs={"a": 10, "c": 100, "b": 20})
    thread_sing = threading.Thread(target=sing, args=(10, ), kwargs={"b": 20, "c": 100})
    thread_dance = threading.Thread(target=dance)

    # 启动子线程
    thread_sing.start()
    thread_dance.start()
