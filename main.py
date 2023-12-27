# 导入requests和re库
import re

import exchange as ne
import requests


# 定义一个函数，用于获取网页源码
def get_html(url):
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    # 发送请求，获取响应
    response = requests.get(url, headers=headers)
    # 设置响应编码为utf-8
    response.encoding = 'utf-8'
    # 返回网页源码
    return response.text


# 定义一个函数，用于获取小说目录信息
def get_catalog(url):
    # 调用get_html函数，获取网页源码
    html = get_html(url)
    # 使用正则表达式匹配所有章节的URL和标题
    pattern = re.compile('<dd><a href=\'(.*?)\' >(.*?)</a></dd>')
    # 返回一个列表，每个元素是一个元组，包含章节URL和标题
    return re.findall(pattern, html)


# 定义一个函数，用于获取小说内容
def get_content(url):
    # 调用get_html函数，获取网页源码
    html = get_html(url)
    # 使用正则表达式匹配小说内容
    pattern = re.compile('<div id="content">(.*?)</div>', re.S)
    # 返回一个字符串，包含小说内容
    return re.search(pattern, html).group(1)


# 定义一个函数，用于保存小说到txt文件中
def save_novel(catalog, novel_name):
    # 以追加模式打开一个txt文件，设置编码为utf-8
    with open(r'C:\\' + novel_name + '.txt', 'a', encoding='utf-8') as f:
        # 遍历目录列表，每个元素是一个元组，包含章节URL和标题
        for chapter_url, chapter_title in catalog:
            if not re.match(
                    '第'.encode('unicode-escape').decode() + '.*?' + '章'.encode('unicode-escape').decode() + '.*',
                    chapter_title):
                continue
            num_zn = re.findall('[0-9]+', chapter_title, 0)
            if num_zn and len(num_zn) > 0:
                chapter_title = re.sub(num_zn[0], ne.num_to_chinese(num_zn[0]), chapter_title, 1)
            # 目的是格式化标题 先放入列表
            title.append(chapter_title)
            # 拼接完整的章节URL
            chapter_url = 'http://www.xbiquge.la' + chapter_url
            # 调用get_content函数，获取章节内容
            chapter_content = get_content(chapter_url)
            # 去除内容中的多余空格和换行符
            chapter_content = chapter_content.replace('&nbsp;', ' ')
            chapter_content = chapter_content.replace('<br />', '')
            # 写入章节标题和内容到文件中，并换行
            f.write(chapter_title + '\n')
            f.write(chapter_content + '\n')
            # 打印提示信息
            print(chapter_title, '保存成功！')


# 定义小说主页URL和小说名字 目录页的网址复制过来，目的为了拿到所有目录
novel_url = 'http://www.xbiquge.la/53/53297/'
# 目标小说的名字
novel_name = '我捡垃圾能成宝'
title = []
# 调用get_catalog函数，获取小说目录信息
catalog = get_catalog(novel_url)
# 调用save_novel函数，保存小说到txt文件中
save_novel(catalog, novel_name)
