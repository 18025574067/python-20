def perse_request(request_date, ip_port):
    """解析请求的报文，返回客户端请求的资源路径"""
    # 根据客户端服务器请求的资源路径，返回请求资源
    # 1）把请求协议解码，得到请求报文的字符串
    request_text = request_date.decode()
    # 2）得到请求行
    #    （1）查找第一个\r\n 的位置
    loc = request_text.find("\r\n")
    #    （2）截取字符串，从开关截取到 第一个\r\n 的位置
    request_line = request_text[:loc]
    # print(request_line)
    # 3）把请求行进行拆分，按照空格拆分，得到列表
    request_line_list = request_line.split(" ")
    # print(request_line_list)
    # 得到请求的资源的路径
    file_path = request_line_list[1]
    print("[%s]正在请求：%s" % (str(ip_port), file_path))
    # 设置默认主页
    if file_path == "/":
        file_path = "/index.html"

    return file_path


def application(current_dir, request_date, ip_port):

    # 调用 perse_request()函数，解析请求协议，返回请求的资源路径
    file_path = perse_request(request_date, ip_port)
    # 定义变量，保存资源路径
    resource_path = current_dir + file_path
    return response_date
