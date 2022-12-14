"""
自定义迭代器
1) 定义迭代器类
2）类中必须 __iter__() 方法
3）类中必须 __next__() 方法

a = b
b = a + b

目标：
# 指定生成5列的斐波那契数列
fib = Fabnacci(5)
value = next(fib)
print(value)


"""


class Fabnacci(object):

    def __init__(self, num):

        # 定义实例属性，保存生成的列数
        self.num = num

        # 定义变量保存斐波那契数列的第一列和第二列
        self.a = 1
        self.b = 1

        # 记录下标位置的实例属性
        self.current_index = 0

    # __iter__()
    def __iter__(self):
        # 返回自己
        return self

    # __next__()
    def __next__(self):
        # 判断列数是否超过生成的总列数
        if self.current_index < self.num:

            # 定义变量保存a的值
            data = self.a

            # a = b  b = a + b
            self.a, self.b = self.b, self.a + self.b

            # 当前列数 +1
            self.current_index += 1

            # 返回 a 的值
            return data

        # 如果超出范围，抛出异常
        else:
            # 主动抛出异常
            raise StopIteration


if __name__ == '__main__':
    # 创建迭代器对象
    fib_iterator = Fabnacci(100)
    # 迭代器本身就是一个迭代器
    for value in fib_iterator:
        print(value)

    # value = next(fib_iterator)
    # print(value)
    #
    # value = next(fib_iterator)
    # print(value)
    #
    # value = next(fib_iterator)
    # print(value)
    #
    # value = next(fib_iterator)
    # print(value)
    #
    # value = next(fib_iterator)
    # print(value)
    #
    # value = next(fib_iterator)
    # print(value)