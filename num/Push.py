import time

from requests_util import RequestUtil
from yaml_util import read_yaml

while True:
    res = RequestUtil().send_all_request(method='POST', url=read_yaml('url'), headers=read_yaml('headers'), json=read_yaml('json')).json()
    if res['code'] == 200:
        print('推送成功')
    time.sleep(15)
