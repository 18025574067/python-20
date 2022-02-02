"""
1、导入模块
2、通过match方法，验证正则
3、判断是否验证成功
4、如果成功，获取匹配的结果

"""
import re

# 1、导入模块
# 2、通过match方法，验证正则
# ?P<name1> 给分组起别名，别名为name1
# ?P=name1 引用别名为name1的分组
result = re.match("<(?P<name1>[a-zA-Z0-9]+)><(?P<name2>[a-zA-Z0-9]+)>.*</(?P=name2)></(?P=name1)>", "<html><h1>test</h1></html>")
# 3、判断是否验证成功
if result:
    print("匹配成功！")
    # 4、如果成功，获取匹配的结果
    print("匹配结果：", result.group())
else:
    print("匹配失败！")



