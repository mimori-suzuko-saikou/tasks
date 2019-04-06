#!/usr/bin/env python3
# coding=utf-8
# Author:梁枫

import pandas
import numpy
import os

path=input('请输入aapl.csv的路径')

if 'aapl.csv' in os.listdir(path):
    aapl=pandas.read_csv(path+'/aapl.csv')
    Vol=aapl['Volume']
    print('Volume的平均值是:',numpy.average(Vol))
else:
    print('找不到aapl.csv')