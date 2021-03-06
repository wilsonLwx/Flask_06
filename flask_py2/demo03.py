# -*- coding:utf-8 -*-

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1/flask_py2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.debug = True
manager = Manager(app)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


class Role(db.Model):
    __tablename__ = 't_roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(23), unique=True)
    user = db.relationship('User', backref='role')


class User(db.Model):
    __tablename__ = 't_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(23), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('t_roles.id'))


@app.route('/')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
