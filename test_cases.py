#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))        #通常動作の確認

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))      #下限境界の確認

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))    #文字入力時の確認

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))    #小数入力時の確認

        def test_sample5 (self):
                self.assertEqual (-1, calc(15,1000))    #上限境界の確認

        def test_sample6 (self):
                self.assertEqual (37962, calc(38,999))  #上限境界の確認

        def test_sample7 (self):
                self.assertEqual (70, calc(1,70))       #下限境界の確認

        def test_sample8 (self):
                self.assertEqual (1200, calc(60,20))    #引数大小関係の確認

        def test_sample9 (self):
                self.assertEqual (-1, calc("5","20")) #文字列数字時の確認

        def test_sample10 (self):
                self.assertEqual (-1, calc("１０","７５")) #文字列数字(全角)時の確認

        def test_sample11 (self):
                self.assertEqual (-1, calc(-4,20))    #数字が負の時の確認
