"""
类：Goods
方法：
    1、初始化方法
    2、获取价格方法
    3、设置价格方法
    4、删除价格方法

"""


class Goods(object):

    # 1、初始化方法
    def __init__(self):
        # 初始化一个原价
        self.org_price = 1000
        # 初始化折扣
        self.discount = 0.7

    # 2、获取价格方法
    @property
    def price(self):
        return self.org_price * self.discount

    # 3、设置价格方法
    @price.setter
    def price(self, val):
        if val > 0:
            self.org_price = val

    # 4、删除价格方法
    @price.deleter
    def price(self):
        print("执行了 delete 方法")


# 创建对象
goods = Goods()
# 获取价格
# goods.price == goods.price()
print(goods.price)

# goods.price == goods.price(500)
goods.price = 500
print(goods.price)

# del goods.price == @price.delete 装饰的方法
del goods.price





