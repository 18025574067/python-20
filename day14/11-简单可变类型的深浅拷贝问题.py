# 可变：变量创建完成后，内存可以改变
# 列表，字典
import copy


def test():
    """可变类型的浅拷贝，也会产生新的空间，能够保证各自的独立性"""
    list1 = [1, 3, 5]
    print("list1 =", list1, id(list1))

    # 拷贝：
    # 1、导入模块
    # 2、调用方法：

    # list3 = list1
    # list3.append(7)
    # print("list3 =", list3, id(list3))

    # 浅拷贝：copy(变量), 会产生副本
    list2 = copy.copy(list1)
    print("list2 =", list2, id(list2))

    # 修改list1
    list1.append(7)
    print("list1 =", list1, id(list1))
    print("list2 =", list2, id(list2))


def test1():
    list1 = [1, 3, 5]
    print("list1 =", list1, id(list1))

    # 深拷贝：deepcopy(变量), 会产生副本
    list2 = copy.deepcopy(list1)
    print("list2 =", list2, id(list2))

    # 修改list2
    list2.append(7)
    print("list2 =", list2, id(list2))
    print("list1 =", list1, id(list1))

    # 总结：简单可变类型的深拷贝，会产生新的空间，能够保证数据的独立性


test()
