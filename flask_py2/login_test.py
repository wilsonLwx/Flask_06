# -*- coding:utf-8 -*-

from demo07 import app
# 导入单元测试
import unittest


# 自定义测试类 继承自unittest.TestCase
class LoginTestCase(unittest.TestCase):
    # 没有输入用户名和密码的情况
    def test_empty_username_pwd(self):
        # 获取测试客户端
        test_client = app.test_client()
        # 发出post请求
        response = test_client.post('/login',data={})
        # 获取参数
        response_data = response.data