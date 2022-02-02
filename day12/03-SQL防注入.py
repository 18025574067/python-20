"""
1、导入模块 - pymysql
2、建立连接对象 pymysql.connect()
3、创建游标对象
4、使用游标对象执行 SQL 语句
5、获取执行的结果
6、打印输出获取的结果
7、关闭游标对象
8、关闭连接对象

"""
import pymysql


# 1、导入模块
# 2、建立连接对象 pymysql.connect()
# pymysql.connect()
# host 主机
# user 用户名
# password 密码
# database 指定数据库
conn = pymysql.connect(host="localhost", user="root", password="hyb123", database="jing_dong")

# 3、创建游标对象
cur = conn.cursor()
# 4、使用游标对象执行SQL语句
# cur.execute(sql语句)，返回的是影响的行数，如果是查询语句，此处返回总记录数
# result = cur.execute("select * from goods")
input_name = input("请输入要查询的语句：\n")
# input_name = " or 1 or "
# "select * from goods where name = ' or 1 or ' order by id desc"
# 防止注入
# 1)构建参数列表，params = [input_name]
# 2)把列表传递给execute(sql, params)
params = [input_name]
sql = "select * from goods where name = %s order by id desc"
result = cur.execute(sql, params)
print("查询到: %s 条数据" % result)
# 5、获取执行的结果
# cur.fetchone()从查询的结果中取出一条数据
# result_list = cur.fetchone()
result_list = cur.fetchall()
# 6、打印输出获取的结果
for line in result_list:
    # line 一行，是一个元组
    print(line)
# print(result_list)
# 7、关闭游标对象
cur.close()
# 8、关闭连接对象
conn.close()

