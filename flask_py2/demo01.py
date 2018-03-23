# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
# 解决编码问题
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_key'


# 1. 自定义表单类 --> 继承FlaskForm
class LoginForm(FlaskForm):
    # <label>用户名:</label><input type="text" name="username" placeholder="请输入用户名"><br>
    username = StringField('用户名:', validators=[DataRequired()], render_kw={'placeholder': '请输入用户名'})
    password = PasswordField('密码:', validators=[DataRequired()], render_kw={'placeholder': '请输入密码'})
    password2 = PasswordField('确认密码:', validators=[DataRequired(), EqualTo('password', '密码不一致')],
                              render_kw={'placeholder': '请确认密码'})
    submit = SubmitField('提交')


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # 在视图函数中创建该类 并传入模板
    register_form = LoginForm()

    if request.method == 'POST':
        # 调用validate_on_submit方法, 可以一次性执行完所有的验证函数的逻辑
        if register_form.validate_on_submit():
            # 进入这里就表示所有的逻辑都验证成功
            username = request.form.get('username')
            password = request.form.get('password')
            password2 = request.form.get('password2')
            return 'success'
        else:
            flash('参数有误')

    return render_template('wtf.html', form=register_form)


if __name__ == '__main__':
    app.run(debug=True)
