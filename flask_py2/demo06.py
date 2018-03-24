# -*- coding:utf-8 -*-
def num(num1, num2):
    # 两个数都必须为整数
    # num2不能为0

    # 断言: num1是整形, 不是的话, 就抛出错误.
    # 错误的类型是AssertionError

    # assert 判断条件 如果出错了的提示信息
    assert isinstance(num1, int), 'num1 must be int'
    assert isinstance(num2, int), 'num2 must be int'
    assert num2 != 0, 'num2 not 0'

    print num1 / num2


# 这里可以随便输入内容测试, 查看断言结果
num(12, 4)
