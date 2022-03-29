# 定义两个函数 func1, func2
# func2 调用 func1
# func2 有可变参数
def func1(*args, **kwargs):
    print("--" * 20)
    print(args)
    print(kwargs)


def func2(*args, **kwargs):
    print("args = ", args)
    print("kwargs = ", kwargs)

    # 调用func1
    # 此处拆包失败，导致参数传递不符合要求
    # func1(args, kwargs)  # ((10, 20, 30), {'a': 10, 'b': 20})  {}
    func1(*args, **kwargs)


if __name__ == '__main__':
    func2(10, 20, 30, a=10, b=20)




