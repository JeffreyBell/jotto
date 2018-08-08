#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:26:22 2018

@author: najmabachelani
"""


import jotto
import unittest

class JottoTests(unittest.TestCase) :
    def testJottocore (self):
        a = "aaaaa"
        b = "aabbb"
        self.assertEqual(jotto.jotto_score(a,b), 2)


if __name__ == '__main__':
    unittest.main()