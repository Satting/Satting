import yaml


def read():
    f = open('../config/data.yaml', encoding='utf-8')
    data = yaml.safe_load(f)
    return data
