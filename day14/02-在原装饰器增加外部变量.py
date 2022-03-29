"""
装饰器写法：
1、存在闭包
2、存在待修饰的函数

"""


def test(path):
    print(path)

    def function_out(func):
        print("function_out path=", path)
        # 外层函数

        def function_in():
            print("------正在验证-------")
            func()

        # 返回内层函数的引用
        return function_in
    # 返回装饰器的引用
    return function_out


@ test("login.py")
# test("login.py")分解成两步：
# 1、test("login.py")  --> function_out引用
# 2、@ 第一步的结果 --> @function_out
# 下一步：
# login = function_out(login)
# @ function_out
def login():
    print("正在登录！")


# @ test("register.py")
# def register():
#     print("正在注册！")


login()
# register()

