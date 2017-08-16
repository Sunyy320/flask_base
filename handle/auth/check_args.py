# -*- coding: utf-8 -*-

import functools
from flask import jsonify,request
from base_handle import error_handle

# 使用装饰器处理必须填写的字段
def require_args(*required_args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            for arg in required_args:
                if arg not in request.values:
                    return error_handle(4000,'参数错误')
            return func(*args,**kw)
        return wrapper
    return decorator


