"""
1、创建 work1 的生成器

2、创建 work2 的生成器

3、获取生成器，通过 next() 运行生成器

"""
import time


# 1、创建 work1 的生成器
def work1():
    while True:
        print("正在执行 work1....")
        yield
        time.sleep(0.5)


# 2、创建 work2 的生成器
def work2():
    while True:
        print("正在执行 work2.................")
        yield
        time.sleep(0.5)


# 3、获取生成器，通过 next() 运行生成器
if __name__ == '__main__':
    w1 = work1()
    w2 = work2()

    # print(w1)
    # print(w2)

    while True:
        next(w1)
        next(w2)









