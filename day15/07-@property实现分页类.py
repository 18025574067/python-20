"""
类名：Page()
方法：
    1、初始化方法
    2、获取开始位置
    3、获取结束位置
"""


class Page(object):
    # 1、初始化方法
    def __init__(self, num):
        self.current_page = num
        self.page_size = 10

    # 2、获取开始位置
    @property
    def start(self):
        # limit（当前页-1）* 每页大小，每页大小
        # 1, 10
        # 11, 20
        return (self.current_page - 1) * 10 + 1

    # 3、获取结束位置
    @property
    def end(self):
        return self.current_page * self.page_size


# 创建类的对象
page = Page(4)
# 获取开始位置
# print(page.start())
print(page.start)
# 获取结束位置
# print(page.end())
print(page.end)



