# -*- coding: utf-8 -*-

from flask import jsonify
from handle.auth import auth
from handle.models.User import User


@auth.route('/', methods=['GET'])
def index():
    # 返回json数据
    jsonRes = dict(errcode='1', errmgs='操作失败')
    res = jsonify(jsonRes)
    return res


@auth.route('/testdb', methods=['GET'])
def test():
    user = User.query.filter_by(username='syy').first()
    if user is None:
        return '查无此人'
    else:
        return 'name=' + user.username + 'pwd=' + user.pwd
        # return '123'
