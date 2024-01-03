import re

from Test.requests_util import RequestUtil
from Test.yaml_util import read_yaml



res = RequestUtil().send_all_request(method='get', url=read_yaml('url'), headers=read_yaml('headers'))
title = re.findall(r'<h1>(.+)</h1>', res.text)
html = re.findall(r' ="(\S+)">(.+)</a', res.text)
print(title)
