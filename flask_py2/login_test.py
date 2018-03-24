# -*- coding:utf-8 -*-

from demo07 import app
# 导入单元测试
import unittest
import json


# 自定义测试类 继承自unittest.TestCase
class LoginTestCase(unittest.TestCase):
    def setUp(self):
        # 获取测试客户端
        self.test_client = app.test_client()

    # 没有输入用户名和密码的情况
    def test_empty_username_pwd(self):
        # # 获取测试客户端
        # test_client = app.test_client()
        # 发出post请求
        response = self.test_client.post('/login', data={})
        # 获取参数
        response_data = response.data
        # 将json字符串转换成字典
        response_dict = json.loads(response_data)

        self.assertIn('errcode', response_dict, 'must have errcode')

        self.assertEqual(-2, response_dict['errcode'], 'errcode must be -2')

        # 没有输入用户名和密码的情况

    def test_username_pwd(self):
        response = self.test_client.post('/login', data={'username': 'itheima', 'password': 'python'})
        response_data = response.data
        response_dict = json.loads(response_data)

        self.assertIn('errcode', response_dict, 'must have errcode')

        self.assertEqual(0, response_dict['errcode'], 'errcode must be 0')


if __name__ == '__main__':
    unittest.main()
