"""
1. 导入模块
2. 创建套接字
3. 发送数据
4. 接收数据（二进制）
5. 解码并显示接收到的数据
6. 关闭套接字
"""

# 1. 导入模块
import socket
# 2. 创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3. 发送数据
udp_socket.sendto("你好！".encode(), ("192.168.124.9", 8080))
# 4. 接收数据（二进制）
# recv_date（1024）的作用：
# 1）从套接字接收1024个字节
# 2）此方法会阻塞程序的结束
# 如果对方电脑发送了数据，则解除了阻塞
# 如果未发送数据，会一直等待
recv_date = udp_socket.recvfrom(1024)
# print(recv_date)
# (b'hello', ('192.168.124.9', 8080))
# 接收到的数据是一个元组：1)接收到的数据的二进制，2）发送方的IP地址和端口号
# recv_date[0]:接收到的数据的二进制
# recv_date[1]：发送方的IP地址和端口号
# print(recv_date[0])
# 5. 解码数据，并得到字符串
recv_test = recv_date[0].decode("UTF-8")
# 6. 显示接收到的数据
# print(recv_test)
print("来自：", recv_date[1], "的消息：", recv_test)
# 7. 关闭套接字
udp_socket.close()



