class Foo(object):

    # get_bar方法
    # @property
    def get_bar(self):
        return "laotie"
    # property对象
    # property(第一个参数，第二个参数，第三个参数，第四个参数)
    # 第一个参数，当我们 foo.BAR 自动调用第一个参数的方法
    # 第二个参数，当我们 foo.BAR = 100, 自动调用第二个参数的方法
    # 第三个参数，当我们 del foo.BAR, 自动调用第三个参数的方法
    # 第四个参数，当我们 foo.BAR.__doc__, 自动获取第四个参数的内容

    BAR = property(get_bar)


foo = Foo()
print(foo.BAR)
print(Foo.BAR)