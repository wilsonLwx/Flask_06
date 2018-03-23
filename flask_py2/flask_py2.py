# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, flash
# 解决编码问题

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

app.secret_key = 'my_keys'


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    # 判断请求方式
    if request.method == 'POST':
        # 获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        # 校验数据
        if not all([username, password, password2]):
            flash('params error')

        elif password != password2:
            flash('password error')

        else:
            return 'success'
    # 返回页面
    return render_template('wtf.html')


if __name__ == '__main__':
    app.run(debug=True)
