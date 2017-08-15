# -*- coding: utf-8 -*-

# from time import time

# import MySQLdb
# from flask import Flask, url_for, request, session, redirect, escape
from flask_script import Manager
# from config.config import config
from handle import create_app


app=create_app('testing')
# app = Flask(__name__)
# 导入配置文件
# app.config.from_object(config['testing'])
manager=Manager(app)


#
# @app.route('/db')
# def testDB():
#     # 打开数据库连接
#     db = MySQLdb.connect("localhost", "root", "root", "mytest")
#     # print(db)
#     # 使用cursor获取操作游标
#     cursor = db.cursor()
#     sql = "INSERT INTO test(name,pwd) VALUES ('%s', '%s')" % ('123456', time())
#     try:
#         cursor.execute(sql)
#         db.commit()
#         print('成功')
#     except MySQLdb.Error, e:
#         print(str(e))
#         db.rollback()
#
#     try:
#         sql = "SELECT * FROM test"
#         cursor.execute(sql)
#         data = cursor.fetchall()
#         for item in data:
#             print(item[1], item[2])
#             # print(data)
#     except MySQLdb.Error, e:
#         print(str(e))
#     db.close()
#     return '测试结束'
#
#
# # 定义方法，如果请求方法不存在，则报错
# @app.route('/index', methods=['POST', 'GET'])
# def index():
#     if request.method == 'GET':
#         return 'method is get====' + escape(session['username'])
#     return 'index page'
#
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         app.logger.info('this is a log info')
#         session['username'] = 'syy'
#         return redirect(url_for('index'))
#     return ''


if __name__=='__main__':
    manager.run()