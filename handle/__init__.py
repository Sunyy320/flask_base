# -*- coding: utf-8 -*-

from flask import Flask
from config.config import config


# db= SQLAlchemy()
def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # 注册蓝本，相当于模块
    from handle.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')

    return  app