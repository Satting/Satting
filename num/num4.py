# from requests_util import RequestUtil
from yaml_util import read_yaml_testcase

date = read_yaml_testcase("num.yaml")
print(date)
# currentTime = time.localtime()
# date_time = str(time.strftime("%Y-%m-%d %H:%M:%S", currentTime))
# json = read_yaml('json')
# json['push_time'] = date_time
# print(json)
