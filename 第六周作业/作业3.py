#!/usr/bin/env python3
# coding=utf-8
# Author:梁枫

import pandas
import numpy
import tkinter.filedialog

fd=tkinter.filedialog.askopenfilename(filetypes=[('aapl.csv','aapl.csv')],initialdir='./')

if type(fd)==str:
    aapl=pandas.read_csv(fd)
    Vol=aapl['Volume']
    print('Volume的平均值是:',numpy.average(Vol))
