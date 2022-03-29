"""
1、存在函数嵌套关系
2、内层函数引用了外层函数的临时变量
3、外层函数返回内层函数的地址

"""


def function_out(num):

    def function_in():
        # 造成错误的原因，是编译器发现了内层函数已经定义的变量num, 优先使用了内部变量
        # 如果在内层定义了和外层同名的变量，而且需要使用外层变量
        # nonlocal 不使用内层函数的变量，而是使用外层函数的变量
        nonlocal num
        print("function_in, num=", num)
        # 内部自定义变量
        num = 88

    return function_in


# 调用外层函数
ret = function_out(10)
ret()


