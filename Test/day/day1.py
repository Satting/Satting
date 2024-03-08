import re
from queue import Queue
from threading import Lock, Thread

from lxml import etree

from Test.requests_util import RequestUtil
from Test.yaml_util import read_yaml


class biqu_pavilion(object):

    def __int__(self):
        res = RequestUtil().send_all_request(method='get', url=read_yaml('url'), headers=read_yaml('headers'))
        r = res.text
        self.q = Queue()
        self.lock = Lock()
        self.title = re.findall(r'<h1>(.+)</h1>', r)
        self.html = re.findall(r' ="(\S+)">(.+)</a', r)
        for i in self.html:
            self.q.put(i)
        self.fp = open(self.title[0] + '.txt', 'w', encoding='utf-8')

    def get_cateid(self):
        for i in self.html:
            url = self.q.get()
            res = RequestUtil().send_all_request(method='get', url='http://www.ibiquge.cc' + url[0], headers=read_yaml('headers')).text
            ht = etree.HTML(res)
            et = ht.xpath('//*[@id="content"]/text()')
            sxu = str(et).replace(r"\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0", '').replace(r"\r'", '').replace("。", '。\n\n').replace(r"\r',", '').replace(r"'\u3000\u3000", '').replace(
                r"\xa0", "").replace(r"['", '').replace(r"']", '').replace(r", '", '').replace(r"”", '').replace(r"“", '')
            self.lock.acquire()
            self.fp.write(url[1] + '\n')
            self.fp.write(sxu + '\n')
            self.lock.release()
            print(i[1], '爬取成功')

    def parse_html(self):
        for i in range(5):
            t = Thread(target=self.get_cateid())
            t.start()


if __name__ == '__main__':
    spider = biqu_pavilion()
    spider.main()
