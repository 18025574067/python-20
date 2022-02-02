"""
1、导入模块
2、通过match方法，验证正则
3、判断是否验证成功
4、如果成功，获取匹配的结果

"""
import re

# 1、导入模块
# 2、通过match方法，验证正则
# 贪婪：满足正则的情况下，尽可能多的取内容
# 非贪婪：满足正则的情况下，尽可能少的取内容
# 把贪婪模式改为非贪婪模式，需要使用符号"?" 在 + * ? ()后面添加?，可以变成非贪婪
# result = re.match("aaa\d+", "aaa123456")

str1 = """
<img class="pic" data-original="https://anchorpost.msstatic.com/cdnimage/anchorpost/1018/92/9b21e1b4f1c4b0127b5dfe92aefcb5_4079_1631086022.jpg?imageview/4/0/w/338/h/190/blur/1" src="https://anchorpost.msstatic.com/cdnimage/anchorpost/1018/92/9b21e1b4f1c4b0127b5dfe92aefcb5_4079_1631086022.jpg?imageview/4/0/w/338/h/190/blur/1/format/webp" data-default-img="338x190" alt="赢城-最强王者视频厅的直播" title="赢城-最强王者视频厅的直播">
"""
str2 = """
<img class="pic" data-original="https://anchorpost.msstatic.com/cdnimage/anchorpost/1006/80/b6af6daa56e470f46090831fccb5f2_1663_1628764566.jpg?imageview/4/0/w/338/h/190/blur/1" src="https://anchorpost.msstatic.com/cdnimage/anchorpost/1006/80/b6af6daa56e470f46090831fccb5f2_1663_1628764566.jpg?imageview/4/0/w/338/h/190/blur/1/format/webp" data-default-img="338x190" alt="友联-奶一的直播" title="友联-奶一的直播">
"""
result = re.search("src=\"(.*?)\"", str1)

# 3、判断是否验证成功
if result:
    print("匹配成功！")
    # 4、如果成功，获取匹配的结果
    print("匹配结果：", result.group())
    print("地址：", result.group(1))
else:
    print("匹配失败！")



