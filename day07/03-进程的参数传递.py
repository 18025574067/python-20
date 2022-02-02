"""
1、导入模块
2、通过模块提供的Process类创建对象
3、启动进程


"""
import time
import multiprocessing


def work1(a, b, c):
    print("进程的参数：", a, b, c)
    for i in range(10):
        print("正在打印 work1...")
        time.sleep(0.5)


if __name__ == '__main__':
    # 1、导入模块
    # 2、通过模块提供的Process类创建对象

    # 进程的参数传递有3种：
    # 1）使用 args 传递元组
    # 2）使用 kwargs 传递字典
    # 3）使用 args 和 kwargs 混合方式传递
    # process_obj = multiprocessing.Process(target=work1, args=(10, 20, 30))
    # process_obj = multiprocessing.Process(target=work1, kwargs={"c": 100, "b": 20, "a": 1000})
    process_obj = multiprocessing.Process(target=work1, args=(10, ), kwargs={"c": 100, "b": 1000})
    # 3、启动进程
    process_obj.start()

    print("xxxxxx")



