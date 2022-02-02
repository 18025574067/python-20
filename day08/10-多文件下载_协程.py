"""
1、定义要下载文件的路径
2、调用下载文件的函数，专门下载文件

文件下载函数：
1、根据url请求网络资源
2、在本地创建文件，准备保存
3、读取网络资源数据（循环）
4、把读取到的资源，写入到本地文件中
5、做异常捕获

"""
from gevent import monkey
monkey.patch_all()

import urllib.request
import gevent


def download_img(img_url, file_name):
    try:
        # 文件下载函数：
        # 1、根据url请求网络资源
        response_date = urllib.request.urlopen(img_url)

        # 2、在本地创建文件，准备保存try:
        with open(file_name, "wb") as file:
            # 3、读取网络资源数据（循环）
            while True:
                file_data = response_date.read(1024)
                # 4、把读取到的资源，写入到本地文件中
                if file_data:
                    file.write(file_data)
                else:
                    break
    # 5、做异常捕获
    except Exception as e:
        print("文件 %s 下载失败" % file_name)
    else:
        print("文件 %s 下载成功" % file_name)


def main():
    # 1、定义要下载文件的路径
    img_url1 = "https://preview.qiantucdn.com/58pic/40/57/14/24X58PICiN9Azh3iIfAet_PIC2018.png!qt324_nowater_jpg"
    img_url2 = "https://preview.qiantucdn.com/58pic/40/52/94/45K58PICmT6I2bA4xtGP4_PIC2018.png!qt324_nowater_jpg"
    img_url3 = "https://preview.qiantucdn.com/58pic/40/53/13/19j58PICED7gpESJGpvSI_PIC2018.png!qt324_nowater_jpg"
    img_url4 = "https://zonemin.bs2dl.yy.com/group16/M00/aacfb18496584236aace4feda315f552.jpg?imageview/4/0/w/320/h/240/blur/1"
    img_url5 = "https://emyfs.bs2cdn.yy.com/ZTNmM2ZkMGQtZDhlMS00YTM1LTkxNmUtNWM1NmFkYjFhMzQz.jpg?imageview/4/0/w/320/h/240/blur/1"

    # 2、调用下载文件的函数，专门下载文件
    # download_img(img_url1, "1.jpg")
    # download_img(img_url2, "2.jpg")
    # download_img(img_url3, "3.jpg")
    # download_img(img_url4, "4.jpg")
    # download_img(img_url5, "5.jpg")

    # 批量给协程 join()
    # gevent.joinall([协程列表])

    gevent.joinall([
        gevent.spawn(download_img, img_url1, "1.jpg"),
        gevent.spawn(download_img, img_url2, "2.jpg"),
        gevent.spawn(download_img, img_url3, "3.jpg"),
        gevent.spawn(download_img, img_url4, "4.jpg"),
        gevent.spawn(download_img, img_url5, "5.jpg")
    ])


if __name__ == '__main__':
    main()



