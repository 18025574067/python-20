def test():
    print("哈哈哈，我是一个可爱的test!")


test()

ret = test
print(ret)

# id() 获取地址
print(id(ret))
print("%x" % id(ret))
print("%x" % id(test))

# 通过ret 调用函数
ret()

# 1、函数名是一个特殊的变量，保存了函数的地址
# 2、自定义一个变量可以获取函数地址
# 3、自定义变量调用函数，“变量名()”




