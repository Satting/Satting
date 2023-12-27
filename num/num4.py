import time

# from requests_util import RequestUtil
from yaml_util import read_yaml

currentTime = time.localtime()
date_time = str(time.strftime("%Y-%m-%d %H:%M:%S", currentTime))
json = read_yaml('json')
json['push_time'] = date_time
print(json)
