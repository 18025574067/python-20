import time


# 定义函数
def say_sorry():
    print("老婆，我错了！！！")
    time.sleep(0.5)


# 调用函数
if __name__ == '__main__':
    for i in range(5):
        say_sorry()
