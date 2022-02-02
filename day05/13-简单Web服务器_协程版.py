"""
TCP服务端：
1、导入模块
2、创建套接字
3、设置地址重用
4、绑定端口
5、设置监听，由主动变为被动接收
6、接受客户端连接，定义函数request_handler()
7、接受客户端浏览器发送的请求协议
8、判断请求协议是否为空
9、拼接响应报文
10、发送响应报文
11、关闭连接

"""
from gevent import monkey
monkey.patch_all()
import socket
# 导入模块
from application import app
import sys
import gevent


"""
1、在类的初始化方法中配置当前的项目
2、给类的初始化项目配置的方法
    2.1、显示所有可以发布的的游戏 菜单
    2.2、接收用户的选择
    2.3、根据用户的选择发布指定的项目（保存用户选择的游戏对应的本地目录）
3、更改Web服务器打开的文件目录
"""


class WebServer(object):
    # 初始化方法
    def __init__(self, part):
        # 6、修改类构造方法，使用提供的端口号启动Web服务
        # 2、创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 3、设置地址重用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 4、绑定端口
        tcp_server_socket.bind(("", part))
        # 5、设置监听，由主动变为被动接收
        tcp_server_socket.listen(128)
        # 定义实例属性，保存套接字对象
        self.tcp_server_socket = tcp_server_socket

        # 定义类的实例属性，porjects_dict 初始化为空
        self.porjects_dict = dict()

        # 定义实例属性，保存在发布的游戏路径
        self.current_dir = ""

        # 初始化字典值
        self.porjects_dict["2048"] = "2048"
        self.porjects_dict["保卫萝卜"] = "tafang"
        self.porjects_dict["植物大战僵尸-普通版"] = "zwdzjs-v1"
        self.porjects_dict["植物大战僵尸-破解版"] = "zwdzjs-v2"
        self.porjects_dict["读心术"] = "dxs"

        # 调用初始化项目的方法
        self.init_porjects()

    # 定义一个初始化项目的方法
    def init_porjects(self):
        # 2.1、显示所有可以发布的的游戏, 菜单
        # list(self.porjects_dict.keys())取出字典的key, 转换成列表
        key_list = list(self.porjects_dict.keys())
        # 遍历显示所有的key
        # enumerate(key_list)
        # [(0, "植物大战僵尸-v1"), (1, "2048"), ...]
        for index, game_name in enumerate(key_list):
            print("%d.%s" % (index, game_name))
        # 2.2、接收用户的选择
        sel_no = int(input("请选择要发布的游戏项目：\n"))
        # 2.3、根据用户的选择发布指定的项目（保存用户选择的游戏对应的本地目录）
        # 根据用户的选择，得到游戏的名称
        key = key_list[sel_no]
        # 根据字典的key 得到项目具体的路径
        self.current_dir = self.porjects_dict[key]

    def start(self):
        """启动Web服务器"""
        print("Web服务器启动成功......等待客户端连接......")
        # 6、接受客户端连接
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print("新客户端来了：%s" % str(ip_port))
            # 调用函数，处理请求并响应
            # self.request_handler(new_client_socket, ip_port)
            # 使用gevent分派任务
            gevent.spawn(self.request_handler, new_client_socket, ip_port)
            # g1.joiin

    def request_handler(self, new_client_socket, ip_port):
        """接收信息，并且做出响应"""
        # 7、接受客户端浏览器发送的请求协议
        request_date = new_client_socket.recv(1028)
        # print(request_date)
        # 8、判断请求协议是否为空
        if not request_date:
            print("%s客户端己断开" % str(ip_port))
            new_client_socket.close()
            return
        # 使用application文件夹中的app模块中的application()函数来处理
        response_date = app.application(self.current_dir, request_date, ip_port)
        # 10、发送响应报文
        new_client_socket.send(response_date)
        # 关闭当前连接
        new_client_socket.close()


def main():
    """主函数"""
    """
    1、导入sys模块
    2、通过 sys.argv 获取参数列表
    3、判断参数列表长度是否为2, 如果长度不等于2给出提示，Web服务启动失败
    4、取出第二个参数，判断是否为数字，如果不是一个数字，给出提示，启动失败
    5、接收启动参数端口号
    6、修改类构造方法，使用提供的端口号启动Web服务
    """
    # 1、导入sys模块
    # 2、通过 sys.argv 获取参数列表
    params_list = sys.argv
    # print(params_list)
    # 3、判断参数列表长度是否为2, 如果长度不等于2给出提示，Web服务启动失败
    if len(params_list) != 2:
        print("启动失败，参数格式错误！正确格式为：python3 xxx.py 端口号")
        return
    # 4、取出第二个参数，判断是否为数字，如果不是一个数字，给出提示，启动失败
    if not params_list[1].isdigit():
        print("启动失败，端口号必须是纯数字！")
        return
    # 5、接收启动参数端口号
    part = int(params_list[1])

    # 创建WebServer对象
    ws = WebServer(part)
    # 调用start()方法
    ws.start()


if __name__ == '__main__':
    main()
