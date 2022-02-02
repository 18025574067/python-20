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
udp_socket.sendto("你好AA".encode(), ("192.168.124.9", 8080))
# 4. 接收数据（二进制）
recv_date = udp_socket.recvfrom(1024)
# 5. 解码数据，并得到字符串
# 指定解码格式encoding="UTF-8"
# errors="ignore"出现错误后，忽略错误
# errors="strict"出现错误，报错--严格模式，默认
# decode(encoding="UTF-8", errors="ignore")
recv_test = recv_date[0].decode(encoding="GBK", errors="strict")
# 6. 显示接收到的数据
print("来自：", recv_date[1], "的消息：", recv_test)
# 7. 关闭套接字
udp_socket.close()



