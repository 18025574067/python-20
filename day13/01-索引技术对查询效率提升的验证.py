"""
目标：插入100000条数据到python_index_db库的test_index表
操作步骤：
1、导入模块
2、创建连接对象
3、创建游标对象
4、for 循环插入100000条数据
5、提交数据
6、关闭游标对象
7、关闭连接对象



"""
import pymysql

# 1、导入模块
# 2、创建连接对象
conn = pymysql.connect(host="localhost", user="root", password="hyb123", database="python_index_db")
# 3、创建游标对象
cur = conn.cursor()
# 4、for 循环插入100000条数据
for i in range(100000):
    cur.execute("insert into test_index(title) values('he-%s')" % i)
# 5、提交数据
conn.commit()
# 6、关闭游标对象
cur.close()
# 7、关闭连接对象
conn.close()


