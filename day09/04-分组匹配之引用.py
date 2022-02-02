"""
1、导入模块
2、通过match方法，验证正则
3、判断是否验证成功
4、如果成功，获取匹配的结果

"""
import re

# 1、导入模块
# 2、通过match方法，验证正则
#                                      \1 --> \有特殊用法
#                                      \\ -->  \
# \1表示引用第一个分组
# result = re.match("<([a-zA-Z0-9]+)>.*</\\1>", "<html>test</html>")
result = re.match("<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>.*</\\2></\\1>", "<html><h1>test</h1></html>")
# 3、判断是否验证成功
if result:
    print("匹配成功！")
    # 4、如果成功，获取匹配的结果
    print("匹配结果：", result.group())
else:
    print("匹配失败！")



