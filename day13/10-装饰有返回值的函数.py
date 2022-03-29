"""
目标：给login()增加验证功能
而且不能修改源代码

"""


def function_out(func):
    def function_in(num):
        # func = login
        print("------开始验证------")
        # func() = login()
        return func(num)
    return function_in


@function_out
def login(num):
    print("开始登录！")
    return num + 10


result = login(8)
print(result)




