from Test.yaml_util import read_yaml_testcase

date = read_yaml_testcase(r"num.yaml")
print(date)
print(date['a'])