"""
wu
"""
import os

import yaml


# 写入
def write_yaml(data):
    """

    :param data:
    """
    with open(os.getcwd() + './test.yaml', encoding='utf-8', mode='a+') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 读取
def read_yaml(key):
    """

    :param key:
    :return:
    """
    with open(os.getcwd() + './test.yaml', encoding='utf-8', mode='r') as f:
        value = yaml.load(f, yaml.FullLoader)
        return value[key]


# 清空
def clear_yaml():
    """
    111
    """
    with open(os.getcwd() + './test.yaml', encoding='utf-8', mode='w') as f:
        f.truncate()


# 读取测试用例
def read_yaml_testcase(yamlpath):
    """

    :param yamlpath:
    :return:
    """
    with open(os.getcwd() + './' + yamlpath, encoding='utf-8', mode='r') as f:
        value = yaml.load(f, yaml.FullLoader)
        return value


def load_yaml(self, yaml_file_name):
    file_path = os.path.join(self.BASE_PATH, "data", yaml_file_name)
    with open(os.getcwd() + './test.yaml', encoding='utf-8') as f:
        data=f.read()
        # data = yaml.safe_load(f)
    return data
