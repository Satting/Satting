import re

from lxml import etree

from requests_util import RequestUtil
from yaml_util import read_yaml


def dii(url, headers):
    res = RequestUtil().send_all_request(method='get', url=url, headers=headers)
    r = res.text
    title = re.findall(r'<h1>(.+)</h1>', r)
    html = re.findall(r' ="(\S+)">(.+)</a', r)
    return html, title


htmls, titles = dii(read_yaml('url'), read_yaml('headers'))
fp = open(titles[0] + '.txt', 'w', encoding='utf-8')
for i in htmls:
    res = RequestUtil().send_all_request(method='get', url='http://www.ibiquge.cc' + i[0], headers=read_yaml('headers')).text
    ht = etree.HTML(res)
    et = ht.xpath('//*[@id="content"]/text()')
    sxu = str(et).replace(r"\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0", '').replace(r"\r'", '').replace("。", '。\n\n').replace(r"\r',", '').replace(r"'\u3000\u3000", '').replace(
        r"\xa0", "").replace(r"['", '').replace(r"']", '').replace(r", '", '').replace(r"”", '').replace(r"“", '')
    fp.write(i[1] + '\n')
    fp.write(sxu + '\n')
    print(i[1], '爬取成功')
