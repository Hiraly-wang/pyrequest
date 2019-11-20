# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 23:08
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : run_test.py
# @Software: PyCharm

import os,sys
sys.path.append('./db_fixture')
sys.path.append('./interface')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data