#!/usr/bin/env python3
# coding=utf-8
# Author:梁枫

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from scipy.optimize import leastsq

def func(x, A, k, theta, C):
    """
    数据拟合所用的函数: A*sin(2*pi*k*x + theta)
    """
    return A*np.sin(2*np.pi*k*x+theta)+C   

def residuals(p,x,y):
    """
    实验数据y值和拟合函数之间的差，p为拟合的系数初值
    """
    A, k, theta, C =p
    return y-func(x, A, k, theta, C)

x = np.arange(0,49,3)
x0 = np.linspace(0,48,100) 
y1 = np.array([48.5,52.6,27.0,-13.8,-38.0,-29.5,-4.9,25.2,48.6,53.2,26.7,-16.1,-39.4,-29.9,-3.5,25.2,48.5])
p0 = np.array([45.75, 0.0419, 1.193, 7.851])

plsq=leastsq(residuals,p0,args=(x,y1))
print("拟合参数", plsq[0])

font=matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/truetype/arphic/uming.ttc')

plt.plot(x, y1, label=u"实验数据")
plt.plot(x0, func(x0,*plsq[0]), label=u"拟合数据")
plt.legend(prop=font)
plt.show()