"""
1、导入模块
2、通过match方法，验证正则
3、判断是否验证成功
4、如果成功，获取匹配的结果

"""
import re

# 1、导入模块
# 2、通过match方法，验证正则
# result = re.match("\w{4,20}@(163|126|qq|sina)\.com$", "hello@126.com")
result = re.match("(\d{3,4})-(\d{7,8})", "010-12345678")
# 3、判断是否验证成功
if result:
    print("匹配成功！")
    # 4、如果成功，获取匹配的结果
    print("匹配结果：", result.group())
    print("提取区号：", result.group(1))
    print("提取电话号码：", result.group(2))
else:
    print("匹配失败！")



