def function_out(func):
    # func = login
    def function_in(*args, **kwargs):
        print("----开始验证-----")
        print("function_in: args=", args)
        print("function_in: kwargs=", kwargs)
        # func(num) == login(num)
        func(*args, **kwargs)

    return function_in


# 登录函数
@ function_out
def login(*args, **kwargs):
    print("开始登录！")
    print("login: args=", args)
    print("login: kwargs=", kwargs)


# 装饰后 == login = function_in(login)
# function_in(10)
login(10, a=10)



