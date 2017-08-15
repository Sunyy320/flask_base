# -*- coding: utf-8 -*-

from flask_script import Manager
from handle import create_app

app = create_app('testing')

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
