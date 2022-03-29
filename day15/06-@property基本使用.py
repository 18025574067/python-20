class Foo(object):

    # 初始化方法
    def __init__(self, num):
        self.num = num

    # 获取值方法
    @property
    def prop(self):
        return self.num


# 创建对象
foo = Foo(100)
# 调用方法
# print(foo.prop())
# foo.prop --> foo.prop()
# @property 像使用属性一样使用方法，获取值
print(foo.prop)




