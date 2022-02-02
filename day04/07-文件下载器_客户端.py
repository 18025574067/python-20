"""
目标：
    /home/hyb/PycharmProjects/python20/day04/1.txt
下载到：
    /home/hyb/桌面/1.txt

1、导入模块
2、创建套接字
3、建立和服务器连接
4、接收用户输入的文件名
5、发送文件名到服务端
6、创建文件, 准备接收数据
7、接收服务端的数据，保存到本地（循环）
8、关闭套接字

"""

# 1、导入模块
import socket
# 2、创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3、建立和服务器连接
tcp_client_socket.connect(("192.168.124.9", 8080))
# 4、接收用户输入的文件名
file_name = input("请输入要下载的文件名：\n")
# 5、发送文件名到服务端
tcp_client_socket.send(file_name.encode())
# 6、准备文件接收服务端返回的文件数据
with open("/home/hyb/桌面/" + file_name, "wb") as file:
    # 7、保存文件数据
    while True:
        file_date = tcp_client_socket.recv(1024)
        # 判断数据是否为空
        if file_date:
            file.write(file_date)
        else:
            # print("下载完成！")
            break
# 8、关闭套接字
tcp_client_socket.close()
