# 1、导入模块 ctype
import ctypes
import threading


# 2、加载so文件
my_lib = ctypes.cdll.LoadLibrary("./libtest.so")


# 3、创建子线程，并且启动
t1 = threading.Thread(target=my_lib.Loop)
t1.start()


# 4、主线程死循环
while True:
    pass

