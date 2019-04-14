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
font=matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/truetype/arphic/uming.ttc')
data=loadcsv(fd)

while data[0][-1]=='':                      #删除空行列
    data=np.delete(data,-1,axis=1)
while data[-1][0]=='':
    data=np.delete(data,-1,axis=0)

data=np.delete(data,np.where(data=='上平均')[1],axis=1)           #排除上学期平均

date=data[0,2:]

plt.rcParams['figure.figsize'] = (16,9)                         #输出图片
output = tkinter.filedialog.askdirectory(initialdir='./',title='请选择输出的目录')
for i in range (1,data.shape[0]):
    No=data[i,0]
    name=data[i,1]
    score=data[i,2:].astype(float)
    plt.title(No)
    plt.xticks(fontproperties=font,fontsize=15)
    plt.plot(date,score,markersize=10,markerfacecolor='blue',marker='o',color='red',
    linewidth=2.5,linestyle='-',label='Score line')
    plt.legend(loc='lower left')
    plt.ylim(0,100)
    plt.savefig('%s/%s.png' % (output,name),dpi=72)
    plt.clf()
