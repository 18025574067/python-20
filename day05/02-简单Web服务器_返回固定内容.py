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


def request_handler(new_client_socket, ip_port):
    """接收信息，并且做出响应"""
    # 7、接受客户端浏览器发送的请求协议
    request_date = new_client_socket.recv(1028)
    # print(request_date)
    # 8、判断请求协议是否为空
    if not request_date:
        print("%s客户端己断开" % str(ip_port))
        new_client_socket.close()
        return
    # 9、拼接响应报文
    # 9.1 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 9.2 响应头
    response_header = "Server: Python20WS/2.1\r\n"
    # 9.3 响应空行
    response_blank = "\r\n"
    # 9.4 响应主体
    response_body = "HelloWorld!"
    response_date = response_line + response_header + response_blank + response_body
    # 10、发送响应报文
    new_client_socket.send(response_date.encode())
    # 关闭当前连接
    new_client_socket.close()


def main():
    """主函数"""
    # 1、导入模块
    # 2、创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 3、设置地址重用
    #                                   当前套接字          地址重用      值True
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 4、绑定端口
    tcp_server_socket.bind(("", 8080))
    # 5、设置监听，由主动变为被动接收
    tcp_server_socket.listen(128)
    # 6、接受客户端连接
    while True:
        new_client_socket, ip_port = tcp_server_socket.accept()
        print("新客户端来了：%s",  ip_port)
        # 调用函数，处理请求并响应
        request_handler(new_client_socket, ip_port)
    # 11、关闭连接
    # tcp_server_socket.close()


if __name__ == '__main__':
    main()
