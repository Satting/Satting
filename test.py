import json
import os.path
from hashlib import sha1

import requests
from fake_useragent import UserAgent


class BaiduSpider:

    def __init__(self):
        # 初始化一下 头部 把刚刚变动的数据改成大括号 便于后面传参
        self.url = 'https://image.baidu.com/search/albumsdata?pn={}&rn=30&tn=albumsdetail&word=%E5%AE%A0%E7%89%A9%E5%9B%BE%E7%89%87&album_tab=%E5%8A%A8%E7%89%A9&album_id=688&ic=0&curPageNum={}'
        self.headers = {
            'User-Agent': UserAgent().random
        }

    def sha1(self, href):
        # 进行sha1的加密
        s = sha1()
        s.update(href.encode())
        return s.hexdigest()

    def parse_html(self, url):
        img_html = requests.get(url=url, headers=self.headers).text
        # 我们这里需要把数据转换成json格式的数据
        img_json = json.loads(img_html)

        for href in img_json['albumdata']['linkData']:
            img_href = href['thumbnailUrl']
            # 调用下载图片的函数 需要把图片的链接传参过去
            self.img_info(img_href)

    def img_info(self, href):
        # 二级页面请求 下载图片
        html = requests.get(url=href, headers=self.headers).content
        # 进行一个sha1的加密
        sha1_r = self.sha1(href)
        # 创建一个保存图片的路径
        file = './img/'
        # 完整保存图片的链接
        filename = file + sha1_r + '.jpg'
        # 判断有没有这个保存图片的路径  没有则创建
        if not os.path.exists(file):
            os.mkdir(file)
        # 进行图片保存
        with open(filename, 'wb') as f:
            f.write(html)
            print(filename)

    def crawl(self):
        page = 185 // 30 if 185 % 30 == 0 else 185 // 30 + 1
        for number in range(page):
            pn = number * 30
            self.parse_html(self.url.format(pn, number))


if __name__ == '__main__':
    baidu = BaiduSpider()
    baidu.crawl()
