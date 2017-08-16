# -*- coding: utf-8 -*-

from flask import jsonify,request
from handle.auth import auth
from handle.models.User import User
from handle import db
import logging
from check_args import require_args
import hashlib
from handle.models.User import create_user
from base_handle import error_handle,success_handle


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


@auth.route('/register',methods=['POST'])
@require_args('name','pwd')
def register():
    name= request.values.get('name')
    pwd=request.values.get('pwd')
    md5=hashlib.md5()
    md5.update(pwd)
    uid=create_user(name,md5.hexdigest())
    if isinstance(uid,int):
        return error_handle(4000,uid)
    return success_handle(200,uid)