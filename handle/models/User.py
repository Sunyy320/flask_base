# -*- coding: utf-8 -*-

from handle import db
import logging

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    pwd = db.Column(db.String(32))

    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd

    def __repr__(self):
        return '<User %r>' % self.username

def create_user(name,pwd):
    user=User(username=name,pwd=pwd)
    db.session.add(user)
    try:
        db.session.commit()
    except BaseException as e:
        db.session.rollback()
        return e.message
    else:
        return user.id