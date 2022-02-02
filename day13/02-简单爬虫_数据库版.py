"""
思路：
1、定义函数，负责保存数据  add_film()
    1) 定义SQL，准备插入数据
    2) 执行SQL语句
    3) 提交插入

2、定义函数，检测数据库中是否有相同数据  film_exist()
    1) 定义SQL根据影片名和地址查询
    2) 执行查询，并获取查询的记录数
    3) 如果获取数 > 0, return True
    4) 如果获取数 = 0, return False

3、创建连接对象
4、创建游标对象
5、关闭操作

"""
import urllib.request
import re
import pymysql


def add_film(film_name, film_link):
    """保存影片信息到数据库中"""
    # 1) 定义SQL，准备插入数据
    sql = "insert into movie_link values(null, %s, %s)"
    # 2) 执行SQL语句
    ret = cur.execute(sql, [film_name, film_link])
    # 如果插入成功，提示用户
    if ret:
        print("影片[%s]保存成功" % film_name)


def film_exist(film_name, film_link):
    """检测数据是否已经存在"""
    # 1) 定义SQL根据影片名和地址查询
    sql = "select id from movie_link where film_name=%s and film_link=%s limit 1"
    # 2) 执行查询，并获取查询的记录数
    ret = cur.execute(sql, [film_name, film_link])
    # 3) 如果获取数 > 0,return True
    if ret:
        return True
    # 4) 如果获取数 = 0,return False
    else:
        return False


def get_movie_links():
    """获取列表页的影片地址信息"""
    # 1、定义列表的地址
    film_list_url = "https://www.ygdy8.net/html/gndy/dyzz/list_23_3.html"

    # 2、打开url, 获取数据
    response_list = urllib.request.urlopen(film_list_url)
    # 2.1 通过read()读取网络资源数据
    response_list_date = response_list.read()

    # 3、解码获取到的数据
    # response_list_text = response_list_date.decode("GBK", 'ignore')
    response_list_text = response_list_date.decode("GBK", errors='ignore')

    # 4、使用正则得到所有内容页的地址
    # print(response_list_text)
    # 4.1 使用findall() 根据正则查找所有影片对应的内容页地址
    # <a href="/html/gndy/dyzz/20210818/61737.html" class="ulink">2021年科幻动画《蝙蝠侠：漫长的万圣节(下)》BD中英双字</a>
    url_list = re.findall(r"<a href=\"(.*)\" class=\"ulink\">(.*)</a>", response_list_text)
    # 4.2 保存地址
    # url_list = [('/html/... ...', 'xxx.电影'), ('/html/... ...', 'xxx.电影')]
    # print(url_list)

    # 定义一个字典，用于保存影片信息
    films_dict = dict()

    # 4.3 循环遍历 url_list
    i = 1
    for content_url, film_name in url_list:

        # 拼接内容页地址
        content_url = "https://www.ygdy8.net/" + content_url
        # print("影片名称：%s, 内容页地址：%s" % (film_name, content_url))
        # 4.4 打开内容页地址
        response_content = urllib.request.urlopen(content_url)
        # 4.5 接收内容页信息
        # 4.6 读取网络资源
        # try:
        #     response_content_data = response_content.read()
        response_content_data = response_content.read()
        # except Exception as e:
        #     response_content_data = e.partial
        # 4.7 解码得到内容页内容
        # response_content_text = response_content_data.decode("GBK", 'ignore')
        response_content_text = response_content_data.decode("GBK", errors='ignore')
        # 4.8 取出下载地址
        # print(response_content_text)
        result = re.search(r"<img border=\"0\" src=\"(.*?)\"|<img border=\"0\" style=\"MAX-WIDTH: 400px\" alt=\"\" src=\"(.*?)\"", response_content_text)
        # <img border=\"0\" style=\"MAX-WIDTH: 400px\" alt=\"\" src=\"(.*?)\"
        # <img border="0" style="MAX-WIDTH: 400px" alt="" src="https://img9.doubanio.com/view/photo/l_ratio_poster/public/p2558022335.jpg"
        # print(result.group(1))
        # 字典
        # {“xxx影片”: "xxx地址"}
        films_dict[film_name] = result.group(1)
        print("已经获取第 %d 张电影封面" % i)

        i += 1

    return films_dict


def main():
    """主函数"""
    films_dict = get_movie_links()
    # print(films_dict)

    # 把字典遍历输出
    for film_name, film_link in films_dict.items():
        # print("%s | %s" % (film_name, film_link))
        # 判断数据是否存在，如果存在就不再插入
        if film_exist(film_name, film_link):
            print("保存失败！[%s]" % film_name)
            continue
        add_film(film_name, film_link)


if __name__ == '__main__':

    # 3、创建连接对象
    conn = pymysql.connect(host="localhost", user="root", password="mysql", database="movie_db")
    # 4、创建游标对象
    cur = conn.cursor()
    # 调用爬取数据的主函数
    main()
    # 提交插入数据
    conn.commit()
    # 5、关闭操作
    cur.close()
    conn.close()













