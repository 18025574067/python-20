"""
可变：变量创建完成后，内容可以再改变
不可变：变量创建，内存空间一旦分配完成，就不能再改变

a, 变量，保存数字，不可变的


"""


def test():
    a = 5
    print("a = ", a, id(a))

    # 修改变量值
    # 重新开辟一块空间存放a的值
    a = 5 + 1
    print("a = ", a, id(a))


list1 = [1, 3, 5]
print("list1", list1, id(list1))

# 给列表增加新的元素
list1.append(7)
print("list1", list1, id(list1))


# 把list1赋值给list2
list2 = list1
list2.append(9)
print("list2", list2, id(list2))
