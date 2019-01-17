#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time: 2019/1/8 16:15


"""
%prog

    this is test file for function printu.
"""
import sys
from bioway.apps.base import printu

def test_printu():
    print("Test")


if __name__ == "__main__":
    printu(__doc__)
    test_printu()