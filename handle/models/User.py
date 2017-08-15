# -*- coding: utf-8 -*-
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

from handle import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True)
    pwd=db.Column(db.String(32))

    def __init__(self,username,pwd):
        self.username=username
        self.pwd=pwd

    def __repr__(self):
        return '<User %r>' % self.username