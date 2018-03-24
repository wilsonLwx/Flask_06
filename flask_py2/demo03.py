# -*- coding:utf-8 -*-

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI '] = 'mysql://root:mysql@127.0.0.1/flask_py2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False

app.debug = True
manager = Manager(app)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
