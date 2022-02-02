"""
1. 导入模块
2. 创建套接字
3. 绑定端口
4. 接收数据
5. 解码数据
6. 输出显示
7. 关闭套接字
"""


# 1. 导入模块
import socket
# 2. 创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3. 绑定端口
# ip地址尽可能写为“”--空，当计算机有多个网卡，都可以接收数据
# addr = ("192.168.124.9", 8081)
addr = ("", 8081)
udp_socket.bind(addr)
# 4. 接收数据
# a, b = (1, 2)
recv_date, ip_port = udp_socket.recvfrom(1024)
# 5. 解码数据
# 6. 输出显示
print("接收到：%s 的信息：%s" % (str(ip_port), recv_date.decode()))
# 7. 关闭套接字
udp_socket.close()


