"""
1、导入模块
2、通过match方法，验证正则
3、判断是否验证成功
4、如果成功，获取匹配的结果

"""
import re

# 1、导入模块
# 2、通过match方法，验证正则
# re.match("正则表达式", "要验证/检测的字符串")
# match如果匹配成功，返回结果match.object对象
# match如果匹配失败，返回结果None
#                 "正则字符串"           "要检测的内容"
result = re.match("\w{4,20}@163\.com$", "hello@163.com")
# 3、判断是否验证成功
if result:
    print("匹配成功！")
    # 4、如果成功，获取匹配的结果
    print("匹配结果：", result.group())
else:
    print("匹配失败！")



