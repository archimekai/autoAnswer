# coding=utf-8
# author: WEN Kai, wenkai123111 AT 126.com
# Nov/16/2016   11:27 PM

from extractFeature import *
import unittest

class testExtarctFeature(unittest.TestCase):

    def test_getCausality(self):
        para = "因为哈密瓜生长在北方，所以哈密瓜很甜。因为太阳很大，所以太阳很热。"
        getCausality(para)




