#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time: 2019/1/12 20:41

from pygal.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code]
