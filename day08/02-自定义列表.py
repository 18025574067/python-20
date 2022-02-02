"""
1、MyList类
1）初始化方法
2）__iter__（）方法，对外提供迭代器
3）additem()方法，用来添加数据

2、自定义迭代器，MyListIterator类
1）初始化方法
2）迭代器方法 __iter__()
3) 获取下一个数据方法，next()

目标：
mylist = MyList()
for value in mylist:
    print(value)



"""


# 1、MyList类
class MyList(object):
    # 1）初始化方法
    def __init__(self):
        # 定义实例属性，保存数据
        self.items = []

    # 2）__iter__（）方法，对外提供迭代器
    def __iter__(self):
        # 实例化MyListIterator()
        mylist_iterator = MyListIterator(self.items)
        # 返回迭代器
        return mylist_iterator

    # 3）additem()方法，用来添加数据
    def additem(self, data):
        # 追加保存内容
        self.items.append(data)
        print(self.items)


# 2、自定义迭代器，MyListIterator类
class MyListIterator(object):
    # 1）初始化方法
    def __init__(self, items):
        # 定义实例属性，保存MyList()传递过来的items
        self.itmes = items

        # 记录迭代器迭代的位置
        self.current_index = 0

    # 2）迭代器方法 __iter__()
    def __iter__(self):
        pass

    # 3) 获取下一个数据方法，next()
    # 当next()时候，就会自动调用 __next__()方法
    def __next__(self):
        # 1、判断当前的下标是否越界
        if self.current_index < len(self.itmes):
            #    1）根据下标获取当前下标的元素值
            data = self.itmes[self.current_index]
            #    2）下标位置+1
            self.current_index += 1
            #    3）返回下标对应的数据
            return data

        # 2、如果越界，直接抛出异常
        else:
            # raise 主动抛出异常
            # StopIteration 停止迭代
            raise StopIteration


if __name__ == '__main__':
    # 创建自定义列表对象
    mylist = MyList()
    mylist.additem("小明")
    mylist.additem("小红")
    mylist.additem("猪八戒")
    mylist.additem("xxxxxxxxx")

    # 遍历的本质
    # 1、iter(mylist)获取mylist对象的迭代器 --> MyList() --> __iter__()
    # 2、next(迭代器)获取下一个值
    # 3、捕获异常
    # for value in mylist:
    #     print("name: ", value)

    mylist_iterator = iter(mylist)
    value = next(mylist_iterator)
    print(value)

    value = next(mylist_iterator)
    print(value)

    value = next(mylist_iterator)
    print(value)

    value = next(mylist_iterator)
    print(value)

    # value = next(mylist_iterator)
    # print(value)
