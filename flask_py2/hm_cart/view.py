# -*- coding:utf-8 -*-
from flask import render_template
from . import admin


@admin.route('/order_info')
def order_info():
    return render_template('order_index.html')

