"""
生成器 -- 是一个特殊的迭代器（保存位置 + 返回下一个值）

next(迭代器) 得到下一个值
next(生成器) 也能够得到下一个值

生成器创建方式：
1）使用列表推导式
2）函数中使用 yield

"""

# 列表推导式
data_list1 = [x*2 for x in range(10)]
for value in data_list1:
    print(value, end=" ")

print("")

# 生成器的创建一：
date_list2 = (x*2 for x in range(10))
print(date_list2)

# 通过 next() 获取下一个值
value = next(date_list2)
print("----->", value)

value = next(date_list2)
print("----->", value)

value = next(date_list2)
print("----->", value)

print("******************************************************")


def test():
    return 10


m = test()
print("m = ", m)


def test1():
    yield 10


# n 是一个生成器对象
n = test1()
print(n)

value = next(n)
print("-------->", value)

