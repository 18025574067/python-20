"""
1) 一个可迭代对象可以提供一个迭代器
2）可迭代对象 ----> iter(可迭代对象) --> next(迭代器)
                     迭代器              下一个元素

迭代器特点：
1）记录遍历的位置
2）提供下一个元素的值 （配合next()）

for循环本质：
1）通过iter(可迭代对象)，获取要遍历的对象的迭代器
2）next(迭代器)获取下一个元素
3）帮我们捕获了 StopIteration 异常

"""
# date_list1 是一个可迭代对象
date_list1 = [1, 3, 5, 7, 9]

# for value in date_list1:
#     print(value)

# 获取迭代器
l1_iterator = iter(date_list1)

# 根据迭代器，获取下一个元素
value = next(l1_iterator)
print(value)                    # 1
print("--" * 20)

value = next(l1_iterator)
print(value)                    # 3
print("--" * 20)

value = next(l1_iterator)
print(value)                    # 5
print("--" * 20)

value = next(l1_iterator)
print(value)                    # 7
print("--" * 20)

value = next(l1_iterator)
print(value)                    # 9
print("--" * 20)

# value = next(l1_iterator)
# print(value)                    # ？？
# print("--" * 20)

# 自定义迭代器类，必须有两点：
# 1）必须含有 __iter__()
# 2）必须含有 __next__()


class MyIterator(object):

    def __iter__(self):
        pass

    # 当next(迭代器)的时候，会自动调用该方法
    def __next__(self):
        pass


my_iterator = MyIterator()
for value in my_iterator:
    print(value)
