from application import utils
from application import urls
from application import funs

# print(urls.route_dict)


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

    response_date = ""
    # 改进动态显示
    # 1. 判断后缀
    # 2. 让.py的显示和 .html显示的内容区别开来
    if file_path.endswith(".py"):

        # 3. 判断请求的资源名称，根据不同的路径显示不同的内容
        if file_path in urls.route_dict:
            # 根据 key值，去urls的route_dict中，获取引用
            func = urls.route_dict[file_path]
            # 根据路由字典，获取函数的引用，执行该函数，返回执行的结果，保存到response_body中
            response_body = func()
            # 调用utils模块的create_http_response函数，拼接响应协议
            response_date = utils.create_http_response("200 OK", response_body.encode())

        else:
            response_body = "Sorry! Page Not Find! 404"
            # 调用utils模块的create_http_response函数，拼接响应协议
            response_date = utils.create_http_response("404 Not Find", response_body.encode())

    else:
        # 异常捕获
        try:
            # with open读取文件
            with open(resource_path, "rb") as file:
                # 把读取的内容返回给客户端
                response_body = file.read()
            # 调用utils模块的create_http_response函数，拼接响应协议
            response_date = utils.create_http_response("200 OK", response_body)

        except Exception as e:
            # 把响应行修改为 404
            response_line = "HTTP/1.1 404 Not Find\r\n"
            # 响应内容显示错误内容
            response_body = "Error! %s" % str(e)
            # 响应内容转换为字节码
            response_body = response_body.encode()
            response_date = utils.create_http_response("404 Not Find", response_body)

    return response_date
