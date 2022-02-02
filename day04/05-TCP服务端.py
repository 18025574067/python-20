"""
1、导入模块
2、创建套接字
3、绑定IP和端口
4、开启监听（设置套接字为被动模式）
5、等待客户连接
6、收发数据
7、关闭套接字
"""

# 1、导入模块
import socket
# 2、创建套接字
tcp_service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3、绑定IP和端口
# tcp_service_socket.bind(("192.168.124.9", 8080))
tcp_service_socket.bind(("", 8080))
# 4、开启监听（设置套接字为被动模式）
# listen()作用设置tcp_service_socket套接字为被动监听模式，不能再发送数据
# 128 是最大的连接数，在 windows 128 有效，但在 linux 此数字无效
tcp_service_socket.listen(128)
# 5、等待客户连接
# accept() 程序会自动进入阻塞状态，如果客户进行连接，程序自动解除阻塞
# recv_date 数据含有两部分
# 1）返回一个新的套接字socket 对象
# 2) 客户端的IP地址和端口
# recv_date = tcp_service_socket.accept()
new_client_socket, client_ip_port = tcp_service_socket.accept()
print("新客户端 %s 来了" % str(client_ip_port))
# 6、收发数据
new_client_socket.send("aa".encode())
# recv_date 会让程序阻塞，收到信息会解除阻塞
recv_date = new_client_socket.recv(1024)
recv_text = recv_date.decode()
print("接收到[%s]的信息：%s" % (str(client_ip_port), recv_text))
# new_client_socket.close() 表示断开当前的客户端连接
new_client_socket.close()
# 7、关闭套接字
# tcp_service_socket.close() 表示程序不再接受新的客户端连接，己连接的可以继续通信
tcp_service_socket.close()



