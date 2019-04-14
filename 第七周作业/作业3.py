#!/usr/bin/env python3
# coding=utf-8
# Author:梁枫

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
import tkinter.filedialog

def loadcsv(file):
    tmp = np.loadtxt(file,dtype=str,delimiter=',',encoding='GBK')       #GBK编码
    data = np.concatenate((tmp[:,[0,3]],tmp[:,5:-1]),1)
    return data

tkinter.Tk().withdraw()
fd=tkinter.filedialog.askopenfilename(filetypes=[('csv格式','.csv')],initialdir='./',title='请选择要打开的csv文件')
font=matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/truetype/arphic/uming.ttc')         #导入中文字体
data=loadcsv(fd)
title=fd.split('/')[-1].split('.')[0]

while data[0][-1]=='':                      #删除空行列
    data=np.delete(data,-1,axis=1)
while data[-1][0]=='':
    data=np.delete(data,-1,axis=0)

data=np.delete(data,np.where(data=='上平均')[1],axis=1)           #排除上学期平均

def calculate_avg(array):
    array=array.take(array.nonzero())
    avg=np.average(array)
    return float(avg)

avgs_list=[]
for i in range (1,data.shape[0]):
    avgs_list.append(calculate_avg(data[i,2:].astype(float)))

hist,bins=np.histogram(avgs_list,bins=[0,10,20,30,40,50,60,70,80,90,100])
bins=bins[:-1]

for x,y in zip(bins,hist):
    plt.text(x,y+0.1,y,ha='center')
plt.xticks(bins,['0+','10+','20+','30+','40+','50+','60+','70+','80+','90+'])
plt.ylabel('人数',fontproperties=font)
plt.bar(bins,hist,width=8,align='center',color='b')
plt.title(title,fontproperties=font)
plt.show()