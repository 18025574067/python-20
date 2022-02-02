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
import socket
# 导入模块
from application import app
import sys


# ws = WebServer()
# ws.start()
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

    def start(self):
        """启动Web服务器"""
        print("Web服务器启动成功......等待客户端连接......")
        # 6、接受客户端连接
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print("新客户端来了：%s" % str(ip_port))
            # 调用函数，处理请求并响应
            self.request_handler(new_client_socket, ip_port)

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
        response_date = app.application("static", request_date, ip_port)
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
