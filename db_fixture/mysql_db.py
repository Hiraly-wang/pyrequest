# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 15:26
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : mysql_db.py
# @Software: PyCharm

import configparser as cparser
import os

from pymysql import connect, cursors
from pymysql.err import OperationalError

# ============读取db_config.ini配置==================
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + 'db_config,ini'

cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get('mysqlconf', 'host')
port = cf.get('mysqlconf', 'port')
db = cf.get('mysqlconf', 'db_name')
user = cf.get('mysqlconf', 'user')
password = cf.get('mysqlconf', 'password')


# ============封装Mysql基本操作==================

class DB:
    def __init__(self):
        try:
            # 连接数据库
            self.conn = connect(host=host,
                                port=port,
                                db=db,
                                user=user,
                                password=password,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor)
        except OperationalError as e:
            print('Mysql error %d: %s' % (e.args[0], e.args[1]))

    '''清除表数据'''

    def clear(self, table_name):
        real_sql = 'delete from ' + table_name + ';'
        with self.conn.cursor() as cursors:
            cursors.execute('set foreign_key_checks=0;')
            cursors.execute(real_sql)
        self.conn.commit()

    '''插入表数据'''

    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
            key = ','.join(table_data.keys())
            value = ','.join(table_data.values())
            real_sql = 'insert into' + table_name + '(' + key + ')values(' + value + ')'
            print(real_sql)
        with self.conn.cursor() as cursors:
            cursors.execute(real_sql)
        self.conn.commit()

    '''关闭数据库连接'''

    def close(self):
        self.close()

if __name__ == '__main__':
    db=DB()
    table_name='sign_event'
    data={'id':12,'name':'红米','address':'北京会展中心','limit':2000,'status':1,'star_time':'2019-12-1 09:00:00'}
    db.clear(table_name)
    db.insert(table_name,data)
    db.close()
