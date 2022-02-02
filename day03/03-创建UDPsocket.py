"""
1.导入模块 socket
2.创建套接字，使用IPv4 UDP 方式
3.数据的传递
4.关闭套接字
"""


# 1.导入模块 socket
import socket
# 2.创建套接字，使用IPv4 UDP 方式
# socket.socket(协议类型，传输方式)
# 参数一：
# socket.AF_INET使用IPv4
# socket.AF_INET6使用IPv6
# 参数二:
# socket.SOCK_DGRAM使用UDP传输方式(无连接)
# socket.SOCK_STREAM使用TCP传输方式(有连接)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3.数据的传递
# 4.关闭套接字
udp_socket.close()


