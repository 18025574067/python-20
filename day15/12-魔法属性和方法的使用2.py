class Goods(object):
    """这是一个商品的类 Goods """

    # 类属性
    goods_color = "白色"

    def __init__(self):
        # 实例属性
        self.org_price = 1000
        self.discount = 0.7

    def set_price(self):
        """这是 Goods 类中一个设置价格的方法"""
        pass

    def __call__(self, *args, **kwargs):
        print("__call__ 方法被调用")

    # def __str__(self):
    #     return "这是一个 __str__ 方法"

    def __del__(self):
        print("__del__ 正在执行")

    def __getitem__(self, item):
        print("key = ", item)

    def __setitem__(self, key, value):
        print("key= ", key, "value= ", value)

    def __delitem__(self, key):
        print("要删除 key ", key)


goods = Goods()
# 对象名（），会调用对象的__call__方法
# goods()
# print(对象)的时候，默认打印的是：<__main__.Goods object at 0x7f5e098457f0>
# print(goods)
# 通过__dict__获取对象信息, 返回字典
# print(goods.__dict__)
# 通过类名.__dict__获取类信息
# print(Goods.__dict__)
# goods["a"] 会调用 __getitem__ 方法
# goods["a"]
# goods["a"] = 100
# goods["a"] = 100 会调用 __setitem__方法
del goods["a"]