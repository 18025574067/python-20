"""
定义若干函数：
1. index()
2. center()
3. gettime()

装饰器路由：
1、装饰器工厂
2、待装饰的函数
3、在装饰器的内部把路径添加到字典中

"""
import time
from application import urls
import re


def route(path):
    # path: 向装饰器内部传递的参数  path   /index.py
    # 装饰器
    # 字典
    # {“index.py”：index函数的引用 }

    # 装饰器
    # 1 ---------- X
    def function_out(func):
        # 2 -------- Y
        urls.route_dict[path] = func
        # print("装饰：[%s]" % path)

        # 装饰器内层
        def function_in():
            # urls.route_dict[path] = func
            # print("装饰：[%s]" % path)
            # 3 ------------ X
            # 调用原参数并且执行
            return func()

        return function_in

    return function_out


@route("/index.py")
# 1、route("/index.py") ---    function_out的引用
# 2、function_out       ---
# 3、     index == function_out(index)
#     index() ---  function_in
def index():
    """处理 index.py 请求"""
    # 1、打开本地网页文件
    with open("templates/index.html") as file:
        # 2、读取文件内容
        content = file.read()
        # 数据库查询
        # 1）导入模块
        # 2）创建连接
        pymysql.connect
        # 3）创建游标对象
        # 4）通过游标对象进行查询
        # 5）获取查询的结果
        # 6）关闭操作
        #       游标      连接
        # 3 导入正则
        # 4、使用正则替换（%centert%） --> ("helloworld")
        content = re.sub("{%content%}", "helloworld!", content)
    # 5、返回文件内容
    return content


@route("/center.py")
def center():
    """处理 center.py 请求"""
    # 1、打开本地网页文件
    with open("templates/center.html") as file:
        # 2、读取文件内容
        content = file.read()
        # 3 导入正则
        # 4、使用正则替换（%centert%） --> ("helloworld")
        content = re.sub("{%content%}", "helloworld!", content)
    # 5、返回文件内容
    return content


@route("/gettime.py")
def gettime():
    """处理 gettime.py 请求"""
    return "This is gettime show! %s" % time.ctime()







