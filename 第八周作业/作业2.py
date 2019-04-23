#!/usr/bin/env python3
# coding=utf-8
# Author:梁枫

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from scipy.optimize import curve_fit 

font = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/truetype/arphic/uming.ttc')

#把一年数据复制三次进行拟合
tempmax = np.array([17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]*3)
tempmin = np.array([-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]*3)
month = np.array([i for i in range(1,37)])

def func(time,A,k,theta,C):
    '''
    温度T对于时间t的函数:周期为k，omiga=2pi/k
    T=A*sin(omiga*time+theta)+C
    '''
    return A*np.sin(2*np.pi/k*time+theta)+C

p0=(10,12,-2,27)
p1=(25,12,-2,-40)
popt1,pcov=curve_fit(func,month,tempmax,p0=p0)
popt2,pcov=curve_fit(func,month,tempmin,p0=p0)
print(popt1,popt2)

x=np.linspace(1,36,100)

plt.plot(month,tempmax,label='最高温')
plt.plot(x,func(x,*popt1),label='最高温拟合')
plt.plot(month,tempmin,label='最低温')
plt.plot(x,func(x,*popt2),label='最低温拟合')
plt.legend(prop=font)
plt.show()