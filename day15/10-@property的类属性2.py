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
    def get_price(self):
        return self.org_price * self.discount

    # 3、设置价格方法
    def set_price(self, val):
        if val > 0:
            self.org_price = val

    # 4、删除价格方法
    def del_price(self):
        print("执行了 delete 方法")

    # property(第一个参数，第二个参数，第三个参数，第四个参数)
    # 第一个参数，当我们 foo.BAR 自动调用第一个参数的方法
    # 第二个参数，当我们 foo.BAR = 100, 自动调用第二个参数的方法
    # 第三个参数，当我们 del foo.BAR, 自动调用第三个参数的方法
    # 第四个参数，当我们 Foo.BAR.__doc__, 自动获取第四个参数的内容

    BAR = property(get_price, set_price, del_price, "BAR 是一个 property 对象")


if __name__ == '__main__':

    # 创建对象
    goods = Goods()
    # 获取价格
    #     goods.BAR ==== goods.get_price()
    print(goods.BAR)
    # 设置价格
    #      goods.BAR = 500 ==== goods.set_price(500)
    goods.BAR = 500
    print(goods.BAR)
    # 删除价格
    #   del goods.BAR ==== @del_property delete
    del goods.BAR
    # 获取对象描述
    #     Goods.BAR.__doc__ ====  Goods.__doc__
    print(Goods.BAR.__doc__)








