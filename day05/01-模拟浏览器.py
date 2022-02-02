"""
1. 导入模块
2. 创建套接字
3. 建立连接
4. 拼接请求报文
5. 发送请求报文
6. 接收服务器的响应报文
7. 保存响应报文
8. 关闭套接字

"""
# 1. 导入模块
import socket
# 2. 创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3. 建立连接
tcp_client_socket.connect(("www.baidu.com", 80))
# 4. 拼接请求报文
# 4.1 请求行
request_line = "GET / HTTP/1.1\r\n"
# 4.2 请求头
request_header = "Host:www.baidu.com\r\n"
# 4.3 请求空行
request_blank = "\r\n"
# 整体拼接
request_date = request_line + request_header + request_blank
# 5. 发送请求报文
tcp_client_socket.send(request_date.encode())
# 6. 接收服务器的响应报文
recv_date = tcp_client_socket.recv(4096)    # 4096 == 4k
recv_test = recv_date.decode()
# print(recv_test)
# 7. 保存响应报文
# 7.1 查询\r\n\r\n的位置
loc = recv_test.find("\r\n\r\n")
# 7.2 截取字符串
html_date = recv_test[loc+4:]
print(html_date)
# 7.3 保存数据到文件
with open("index.html", "w") as file:
    file.write(html_date)
# 8. 关闭套接字
tcp_client_socket.close()









