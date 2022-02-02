"""
1、导入模块
2、创建连接对象
3、创建游标对象
4、使用游标对象执行SQL语句
5、提交
6、打印输出结果
7、关闭游标对象
8、关闭连接对象

"""
import pymysql

# 1、导入模块
# 2、创建连接对象
conn = pymysql.connect(host="localhost", user="root", password="hyb123", database="jing_dong")
# 3、创建游标对象
cur = conn.cursor()
# 4、使用游标对象执行SQL语句
# sql = "insert into goods value(null, '老王牌拖拉机', 1, 1, 9998, 1, 1)"
# sql = "delete from goods where id=27"
sql = "update goods set name='最新款老王牌拖拉机' where id=25"
ret = cur.execute(sql)
# 5、提交
conn.commit()
# 6、打印输出结果
print("影响行数：", ret)
# 7、关闭游标对象
cur.close()
# 8、关闭连接对象
conn.close()
