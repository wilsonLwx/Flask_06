# -*- coding:utf-8 -*-
'''
1.在目录__init__文件下导入蓝图模块 创建蓝图对象
2.在子模块中导入蓝图对象 实现路由定义
3.在app中注册蓝图
'''
from flask import Blueprint

admin = Blueprint('order', __name__, template_folder='templates', url_prefix='/order')

# 导入使用蓝图的子模块
import view
