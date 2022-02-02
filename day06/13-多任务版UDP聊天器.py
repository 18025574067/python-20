#! /usr/bin/python3.7
"""
一、功能
1、发送信息
2、接收信息
3、退出系统

二、框架的设计
1、发送信息的函数 send_msg()
2、接收信息的函数 recv_msg()
3、程序的主入口 main()
4、当程序独门运行的时候，才启动聊天器

三、实现步骤
1、发送信息 send_msg()
1)定义变量接收用户输入与输入的接收方的IP
2)定义变量接收用户输入与输入的接收方的端口
3)定义变量接收用户输入与输入的接收方的信息
4)使用socket的sendto()发送信息

2、接收信息
1)使用socket接收信息
2)解码数据
3)输出显示

3、主入口main()
1)创建套接字
2)绑定端口
3)打印菜单
4)接收用户输入的选项
5)判断用户的选择，并且调用对应的函数
6)退出系统

"""
import socket
import threading


def send_msg(udp_socket):
    """发送信息的函数"""
    # 1)定义变量接收用户输入与输入的接收方的IP
    ipaddr = input("请输入接收方的IP地址：\n")
    # 判断是否需要默认
    if len(ipaddr) == 0:
        ipaddr = "192.168.124.11"
        print("当前接收方默认IP设定为：%s" % ipaddr)
    # 2)定义变量接收用户输入与输入的接收方的端口
    part = input("请输入接收方的端口号：\n")
    if len(part) == 0:
        part = "8080"
        print("当前接收方默认设定为：%s" % part)
    # 3)定义变量接收用户输入与输入的接收方的信息
    content = input("请输入要发送的内容：\n")
    # 4)使用socket的sendto()发送信息
    udp_socket.sendto(content.encode(), (ipaddr, int(part)))
    print("发送信息成功！")


def recv_msg(udp_socket):
    """接收信息的函数"""
    while True:
        # 1)使用socket接收信息
        recv_date, ip_part = udp_socket.recvfrom(1024)
        # 2)解码数据
        recv_test = recv_date.decode()
        # 3)输出显示
        print("接收到[%s]的信息：%s" % (str(ip_part), recv_test))


def main():
    """程序的主入口"""
    # 1)创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2)绑定端口
    udp_socket.bind(("", 8081))

    # 设置子线程，用于接收信息
    thread_recvmsg = threading.Thread(target=recv_msg, args=(udp_socket, ))

    # 设置子线程守护主线程
    thread_recvmsg.setDaemon(True)

    # 启动子线程
    thread_recvmsg.start()

    # 3)打印菜单(循环)
    while True:
        print("\n\n**************************************")
        print("************* 1、发送信息 *************")
        print("************* 2、系统关闭 *************")
        print("**************************************")
        # 4)接收用户输入的选项
        sel_num = int(input("请输入选项：\n"))
        # 5)判断用户的选择，并且调用对应的函数
        if sel_num == 1:
            # print("你选择的功能是：发送信息")
            send_msg(udp_socket)

        elif sel_num == 2:
            print("系统正在退出...")
            print("系统退出完成！")
            break
    # 6)退出系统
    udp_socket.close()


if __name__ == '__main__':
    # 程序独立运行的时候，才启动聊天器
    main()

