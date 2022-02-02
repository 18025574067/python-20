"""
1、创建一个生成器：
    目标：实现斐波那契数列
    1）定义变量保存第一列和第二列的值
    2）定义变量保存当前生成的位置

    3）循环生成数据，条件 （当前的列数 < 总列数）
    4）保存 a 的值
    5）修改 a / b 的值
    6）返回 a 的值 yield

2、定义变量保存生成器
next(生成器)得到下一个元素值

"""


# 1、创建一个生成器：
def fabnacci(n):
    #     目标：实现斐波那契数列
    #     1）定义变量保存第一列和第二列的值
    a = 1
    b = 1
    #     2）定义变量保存当前生成的位置
    current_index = 0
    print("--------------1111--------------")
    #
    #     3）循环生成数据，条件 （当前的列数 < 总列数）
    while current_index < n:
        #     4）保存 a 的值
        data = a
        #     5）修改 a / b 的值
        a, b = b, a+b
        # 列数 + 1
        current_index += 1
        #     6）返回 a 的值 yield
        # 1）充当 return 作用
        # 2）保存程序的运行状态，并且暂停程序运行
        # 3）当 next()的时候，继续唤醒程序从yield向下执行
        print("--------------22222--------------")
        xxx = yield data
        print("--------------333333--------------")
        if xxx == 1:
            # 生成器能使用 return, 让生成器结束
            return "哈哈，我是return ! 我能让生成器结束"


if __name__ == '__main__':

    # 2、定义变量保存生成器
    fab = fabnacci(5)

    # next(生成器)得到下一个元素值
    value = next(fab)
    print("第1列：", value)

    try:
        value = next(fab)
        print("第2列：", value)

        # 生成器.send(1), 传递参数给生成器
        value = fab.send(1)
        print("第3列：", value)

    except Exception as e:
        print(e)
