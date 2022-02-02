"""
1、导入模块
2、创建套接字
3、绑定端口
4、设置监听，设置套接字由主动转换成被动
5、接受客户端的连接
6、接受客户端发送过来的文件名
7、根据文件名读取文件内容
8、把读取到的文件内容发送到客户端（循环）
9、关闭当前的客户端连接
10、关闭服务器

"""

# 1、导入模块
import socket
# 2、创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置套接字可以重用
# tcp_server_socket.setsockopt(当前套接字，属性名，属性值)
# socket.SO_REUSEADDR 地址是否可以重用， True 表示可以重用，False 表示不可重用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 3、绑定端口
tcp_server_socket.bind(("", 8080))
# 4、设置监听，设置套接字由主动转换成被动
tcp_server_socket.listen(128)
# 5、接受客户端的连接
while True:
    new_client_socket, ip_port = tcp_server_socket.accept()
    print("欢迎新客户端：", ip_port)
    # 6、接受客户端发送过来的文件名
    rect_date = new_client_socket.recv(1024)
    file_name = rect_date.decode()
    print(file_name)
    # 7、根据文件名读取文件内容
    try:
        with open(file_name, "rb") as file:
            # 8、把读取到的文件内容发送到客户端（循环）
            while True:
                file_date = file.read(1024)
                # 判断数据传送结束
                if file_date:
                    new_client_socket.send(file_date)
                else:
                    print("数据上传成功！")
                    break
    except Exception as e:
        print("文件%s不存在，下载失败!" % file_name)
    else:
        print("文件下载%s成功" % file_name)
    # 9、关闭当前的客户端连接
    new_client_socket.close()
# 10、关闭服务器
# tcp_server_socket.close()
