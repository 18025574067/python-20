# import module1
# # module1 -- 模块名
# # name -- module1模块中的变量
# print(module1.name)


# import app
# print(app.name)


# 查看系统的 path 环境变量
# 1）导入模块 sys
# 2) sys.path可以查看环境变量的具体内容
import sys
# print(sys.path)
for p in sys.path:
    print(p)
    # pass
print("--" * 20)
# 把自己写的模块的路径临时写到环境变量中
# sys.path.append("/home/hyb/桌面/test")
sys.path.insert(0, "/home/hyb/桌面/test")

for p in sys.path:
    print(p)

import app
print(app.name)