import threading

from Test.requests_util import RequestUtil
from Test.yaml_util import read_yaml


def delete1():
    while len(r):
        url = read_yaml('url') + "?id={0}".format(r[-1]['id'])
        rel = RequestUtil().send_all_request(method='get', url=url, headers=read_yaml('headers')).json()
        if rel['code'] == 200:
            del r[-1]
            print(r[-1]['title'], '1删除成功')


if __name__ == '__main__':

    url = 'http://api.drumbeatdev.com/message-v3/export_record/query'
    res = RequestUtil().send_all_request(method='post', url=url, headers=read_yaml('headers'), json=read_yaml('json')).json()
    r = res['data']['rows']
    t = threading.Thread(target=delete1)
    t.start()
    while len(r):
        url = read_yaml('url') + "?id={0}".format(r[0]['id'])
        rel = RequestUtil().send_all_request(method='get', url=url, headers=read_yaml('headers')).json()
        if rel['code'] == 200:
            del r[0]
            print(r[0]['title'], '5删除成功')
