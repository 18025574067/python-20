class Test(object):
    def __init__(self):
        print("-------init-----方法")

    def run(self):
        print("------正在疯跑-----")

    def __call__(self, *args, **kwargs):
        print("-----call----")


# 创建对象
test = Test()
# test.run()
# 当对象名(), 此时会调用类的__call__方法
test()


