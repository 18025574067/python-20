class Goods(object):
    """这是一个商品的类 Goods """

    def set_price(self):
        """这是 Goods 类中一个设置价格的方法"""
        pass

    def __del__(self):
        print("__del__ 正在执行")


# 1、类名的描述信息
# 类名.__doc__
print(Goods.__doc__)


# 2、对象方法的描述信息
goods = Goods()
# 对象.方法名.__doc__
print(goods.set_price.__doc__)

# 3、获取当前模块
print(Goods.__module__)

# 4、获取对象所属的类
print(goods.__class__)

# 5、删除对象会调用 对象的__del__ 方法
del goods




