# -*- coding: utf-8 -*-

from flask import jsonify
from handle.auth import auth
from handle.models.User import User
from handle import db


@auth.route('/', methods=['GET'])
def index():
    # 返回json数据
    jsonRes = dict(errcode='1', errmgs='操作失败')
    res = jsonify(jsonRes)
    return res

@auth.route('/querydb', methods=['GET'])
def test():
    user = User.query.filter_by(username='syy').first()
    if user is None:
        return '查无此人'
    else:
        return 'name=' + user.username + 'pwd=' + user.pwd

@auth.route('/insertdb', methods=['GET'])
def dbInsert():
    user = User('test', 'test')
    db.session.add(user)
    db.session.commit()
    return '122'
