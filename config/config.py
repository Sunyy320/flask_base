# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = 'this is secret_key and this is must'

    @staticmethod
    def init_app(app):
        pass


# 继承
class TestConfig(BaseConfig):
    DEBUG = True


config = {
    'testing': TestConfig,

    'default': BaseConfig
}
