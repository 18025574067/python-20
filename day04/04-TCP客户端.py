"""
1、导入模块
2、创建套接字 TCP
3、建立连接
4、发送数据
5、关闭套接字
"""
# 1、导入模块
import socket
# 2、创建套接字 TCP
# socket.SOCK_STREAM TCP传输方式
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3、建立连接 connect(address)
# tcp_client_socket.connect(address)
# address --> ("IP", 端口)
addr = ("192.168.124.9", 8080)
tcp_client_socket.connect(addr)
# 4、发送数据
tcp_client_socket.send("hello".encode())
# 接收数据
recv_date = tcp_client_socket.recv(1024)
print(recv_date)
# recv_date 保存的是服务端回复的信息二进制数据
# b'\xe7\xba\xa6\xe5\x90\x97\xef\xbc\x9f'
recv_test = recv_date.decode()
print("收到信息：", recv_test)
# 5、关闭套接字
tcp_client_socket.close()




