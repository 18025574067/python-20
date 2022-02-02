"""
1. 导入模块
2. 创建套接字
3. 端口绑定
4. 发送数据
5. 关闭套接字
"""


# 1. 导入模块
import socket
# 2. 创建套接字
UDP_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3. 端口绑定
# UDP_socket.bind(address)
# addr = ("192.168.124.9", 8081)
addr = ("", 8081)
UDP_socket.bind(addr)
# 4. 发送数据
UDP_socket.sendto("晚上好！".encode(), ("192.168.124.9", 8080))
# 5. 关闭套接字
UDP_socket.close()
