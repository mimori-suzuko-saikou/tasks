#!/usr/bin/env python3
# coding=utf-8
# Author:梁枫

import pandas

No=(1,2,3,4,5)
Name=('mayi','jack','tom','rain','hanmeimei')
Age=(18,21,25,19,23)
Score=(99,89,95,80,81)

chart={'No.':No,'Name':Name,'Age':Age,'Score':Score}

data=pandas.DataFrame(chart)
data.to_csv('test.csv',index=False)