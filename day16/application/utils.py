def create_http_response(status, response_body):
    # 9、拼接响应报文
    # 9.1 响应行
    response_line = "HTTP/1.1 %s\r\n" % status
    # 9.2 响应头
    response_header = "Server: Python20WS/2.1\r\n"
    # response_header += "Content-Type: text/html\r\n"
    # 9.3 响应空行
    response_blank = "\r\n"
    # 9.4 响应主体

    response_date = (response_line + response_header + response_blank).encode() + response_body
    return response_date


