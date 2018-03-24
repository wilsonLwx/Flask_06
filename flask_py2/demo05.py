# -*- coding:utf-8 -*-

from flask import Flask,template_rendered
# from cart import admin
# from hm_cart.view import admin
from hm_cart import admin

app = Flask(__name__)

# 装饰器装饰视图函数
# app.route('/cart_list')(cart_list)
# 蓝图注册
app.register_blueprint(admin)


@app.route('/')
def hello_world():
    return 'hello world'


# @app.route('/order_list')
# def order_list():
    # return template_rendered('order_index')


# @app.route('/order_info')
# def order_info():
#     return 'order_info'


#
# @app.route('/cart_list')
# def cart_list():
#     return 'cart_list'
#
#
# @app.route('/cart_detail')
# def cart_detail():
#     return 'cart_detail'


if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)
