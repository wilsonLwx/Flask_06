# -*- coding:utf-8 -*-

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# 配置邮件：服务器／端口／安全套接字层／邮箱名／授权码
app.config['MAIL_SERVER'] = "smtp.163.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "15000108650@163.com"
app.config['MAIL_PASSWORD'] = "1a2b3c"
app.config['MAIL_DEFAULT_SENDER'] = 'FlaskAdmin<15000108650@163.com>'

mail = Mail(app)


@app.route('/')
def hello_world():
    return '<a href="/send_mail">发送邮件</a>'


@app.route('/send_mail')
def send_mail():
    message = Message(subject='恭喜您，喜中价值40万的小汽车一辆', recipients=['15000108650@163.com'], body='请先缴纳5000块钱税收才能领奖！')
    mail.send(message)
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)
