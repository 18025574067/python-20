"""
1、导入模块
2、创建套接字
3、设置端口重用
4、绑定端口
5、设置监听，由主动变成被动
6、接收客户端连接
7、接收客户端发送的信息
8、解码信息并输出
9、关闭当前的客户端连接

"""
import socket
import threading


def recv_msg(new_client_socket, ip_port):

    while True:
        # 7、接收客户端发送的信息

        recv_date = new_client_socket.recv(1024)
        if recv_date:
            # 8、解码信息并输出
            recv_text = recv_date.decode("GBK")
            print("收到来自[%s]的信息：%s" % (str(ip_port), recv_text))
        else:
            break
    # 9、关闭当前的客户端连接
    new_client_socket.close()


# 1、导入模块
# 2、创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3、设置端口重用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 4、绑定端口
tcp_server_socket.bind(("", 8080))
# 5、设置监听，由主动变成被动
tcp_server_socket.listen(128)
while True:
    # 6、接收客户端连接
    new_client_socket, ip_port = tcp_server_socket.accept()
    print("欢迎新客户端！", ip_port)
    # 接收多条信息
    # recv_msg(new_client_socket, ip_port)
    # 创建线程
    thread_recvmsg = threading.Thread(target=recv_msg, args=(new_client_socket, ip_port))
    # 设置线程守护
    thread_recvmsg.setDaemon(True)
    # 启动线程
    thread_recvmsg.start()

# tcp_server_socket.close()




