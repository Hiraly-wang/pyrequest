# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 22:41
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : add_event_test.py
# @Software: PyCharm

import unittest
import requests
import os,sys

parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data

'''添加发布会'''
class AddEventTest(unittest.TestCase):

    def setUp(self):
        self.base_url='httP://127.0.0.1:8000/api/add_event/'

    def tearDown(self):
        print(self.result)

    '''所有参数为空'''
    def test_add_event_all_null(self):
        payload={'eid':'','name':'','limit':'','address':'','start_time':''}
        r=requests.post(self.base_url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],'10021')
        self.assertEqual(self.result['message'],'parameter error')


    '''ID已经存在'''
    def test_add_event_eid_exits(self):
        payload = {'eid': 1, 'name': '一加四发布会', 'limit': 2000, 'address': '深圳宝林', 'start_time': '2019'}
        r=requests.post(self.base_url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],'10022')
        self.assertEqual(self.result['message'],'event id is already exits')

    '''发布会名字已经存在'''
    def test_add_event_name_exits(self):
        payload = {'eid': 8, 'name': '红米Pro发布会', 'limit': 2000, 'address': '深圳宝林', 'start_time': '2019'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], '10023')
        self.assertEqual(self.result['message'], 'event name is already exits')

    '''日期时间格式错误'''

    def test_add_event_date_type_error(self):
        payload = {'eid': 8, 'name': 'apple', 'limit': 2000, 'address': '深圳宝林', 'start_time': '2019'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], '10024')
        self.assertIn('start_time format error.',self.result['message'])

    '''添加成功'''

    def test_add_event_success(self):
        payload = {'eid': 6, 'name': 'apple', 'limit': 2000, 'address': '深圳宝林', 'start_time': '2019-12-12 12:12:12'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], '200')
        self.assertEqual(self.result['message'],'add event success')

    if __name__ == '__main__':
        test_data.init_data()
        unittest.main()