"""
yagmail发送邮件：
1、导入模块
2、使用yagmail的类创建对象（发件人，发件人授权码，发件的服务器）
3、使用yagmail对象发送邮件（指定收件人，邮件主题，发送的内容）
"""
# 1、导入模块
import yagmail

# 2、使用yagmail的类创建对象（发件人，发件人授权码，发件的服务器）
# 2.1 发件人:15914760322@139.com --> user="15914760322@139.com"
# 2.2 发件人授权码：password="py123456" 非密码
# 2.3 发件服务器：host="smtp.163.com"
ya_obj = yagmail.SMTP(user="hyb159147@163.com", password="MXCAWABAWPIGRIIG", host="smtp.163.com")

# 3、使用yagmail对象发送邮件（指定收件人，邮件主题，发送的内容）
content = "导入模块, 使用yagmail的类创建对象（发件人，发件人授权码，发件的服务器), 使用yagmail对象发送邮件（指定收件人，邮件主题，发送的内容）"
demo = "demo"
# sent(指定收件人，邮件主题，发送的内容)发送邮件
ya_obj.send("hyb2419805602@163.com", demo, content)
ya_obj.send("2419805602@qq.com", demo, content)
ya_obj.send("15914760322@139.com", demo, content)
ya_obj.send("18025574067@189.cn", demo, content)
ya_obj.send("hyb2419805602@icloud.com", demo, content)
ya_obj.send("3525244204@qq.com", demo, content)

