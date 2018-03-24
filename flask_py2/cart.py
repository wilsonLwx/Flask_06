# -*- coding:utf-8 -*-
from flask import Blueprint

# 导入蓝图模块 创建蓝图对象
admin = Blueprint('cart', __name__)


# 使用蓝图对象实现路由定义
@admin.route('/cart_list')
def cart_list():
    return 'cart_list'


@admin.route('/cart_detail')
def cart_detail():
    return 'cart_detail'
