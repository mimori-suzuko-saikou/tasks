#!/usr/bin/env python3
# coding=utf-8
# Author:梁枫

long_month=[1,3,5,7,8,10,12]            #有31天的月份
short_month=[4,6,9,11]                  #有30天的月份

def dates():
    date_origin=input('请输入日期1(yyyy,mm,dd):')
    date=[int(date_origin[0:4]),int(date_origin[5:7]),int(date_origin[8:])]
    return date

def days_pasted(y,m,d):
    
    days=0
    for i in range(1,m):
        if i in long_month:
            days+=31
        elif i in short_month:
            days+=30
        else:
            if leap_year(y)==True:
                days+=29
            else:
                days+=28
    days+=d
    return days

def leap_year(year):
    if year%4==0 and (year%100!=0 or year%400==0):
        return True
    else:
        return False

def leap_years_between(y1,y2):           #计算y1到y2之间的闰年数,包含y1,不包含y2
    t=0
    for year in range(y1,y2):
        if leap_year(year)==True:
            t+=1
    return t

def count_days(date1,date2):
    y1,m1,d1=date1[0],date1[1],date1[2]
    y2,m2,d2=date2[0],date2[1],date2[2]
    days=(y2-y1)*365+leap_years_between(y1,y2)-days_pasted(y1,m1,d1)+days_pasted(y2,m2,d2)
    return days
    

print('请输入日期1')
date1=dates()
print('请输入日期2')
date2=dates()
print('相差',count_days(date1,date2),'天')
