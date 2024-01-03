import pytest

# def setup_function():
#     print('开始')
#
#
# def teardown_function():
#     print('结束')


"""
setup_module/teardown_module 模块级
setup_function/teardown_function 用例级（函数级）
setup_class/teardown_class 类级
setup_method/teardown_method 方法级


@pytest.fixture(autouse=True) 夹具
"""


@pytest.fixture(autouse=True)
def func():
    print('开始')


def test_one():
    a = 2
    b = 2
    assert a == b


def test_two():
    s = 2
    f = 1
    assert s == f


if __name__ == '__main__':
    pytest.main()
