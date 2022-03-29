# 创建一个装饰器，一个待装饰的函数
# 定义一个文字加粗的装饰器


def makeBlod(func):
    def function_in():
        return "<b>" + func() + "</b>"
    return function_in


def makeItalic(func):
    def function_in():
        return "<i>" + func() + "</i>"
    return function_in


@ makeBlod
def test():
    return "hellloworld-1"

@ makeItalic
def test_2():
    return "hellloworld-2"


@ makeItalic
@ makeBlod
def test_3():
    return "hellloworld-3"


print(test())    # <b>hellloworld-1</b>
print(test_2())  # <i>hellloworld-2</i>
print(test_3())  # <i><b>hellloworld-3</b></i>

