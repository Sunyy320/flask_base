# -*- coding: utf-8 -*-
from flask import jsonify


def error_handle(code,msg='发生错误',detail=''):
    return jsonify({
        'code':code,
        'msg':msg,
        'detail':detail
    })

def success_handle(code,msg='成功',detail=''):
    return jsonify({
        'code': code,
        'msg': msg,
        'detail': detail
    })
