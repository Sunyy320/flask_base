# -*- coding: utf-8 -*-

from flask import jsonify
from handle.auth import auth


@auth.route('/', methods=['GET'])
def index():
    # 返回json数据
    jsonRes = dict(errcode='1', errmgs='操作失败')
    res = jsonify(jsonRes)
    return res
