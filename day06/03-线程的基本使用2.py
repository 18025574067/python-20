"""
1、导入模块 -- threading
2、创建子线程对象 使用threading.Thread()类创建对象（子线程对象）
3、指定子线程执行的分支
4、启动子线程，子线程.start()方法
"""


import time
# 1、导入模块 - - threading
import threading


# 定义函数
def say_sorry():
    print("老婆，我错了！！！")
    time.sleep(0.5)


# 调用函数
if __name__ == '__main__':

    for i in range(5):

        # 2、创建子线程对象，使用threading.Thread()类创建对象（子线程对象）
        # 3、指定子线程执行的分支
        # threading.Thread(target=函数名)
        thread_obj = threading.Thread(target=say_sorry)
        # 4、启动子线程，子线程.start()方法
        # 线程对象只有调用 start() 子线程才会执行
        thread_obj.start()

    print("xxxxxxx")
