"""
目标：给login()增加验证功能
而且不能修改源代码

"""


def function_out(func):
    def function_in():
        # func = login
        print("------开始验证------")
        # func() = login()
        func()
    return function_in


@function_out
# @function_out 装饰了login函数
# 底层：login = function_out(login)
def login():
    print("开始登录！")


# 通过闭包调用函数
# login = function_out(login)
# login() = functin_in();

login()




