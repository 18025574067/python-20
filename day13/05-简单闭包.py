
def function_out(num):
    """外层函数"""
    print("1.function, num=", num)

    def function_in(num_in):
        """内层函数"""
        print("2.-----function_in------num=", num)
        print("3.-----function_in------num_in=", num_in)

    return function_in


# function_out(10)
# 调用 function_out 获取内层函数，保存到ret函数中
ret = function_out(100)
ret(88)







