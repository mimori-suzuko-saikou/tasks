#!/usr/bin/env python
# coding=utf-8
# Author:梁枫

address_book={}
def print_menu():
    print(
    '====通讯录管理系统====\n'
    '1.新增联系人\n'
    '2.删除联系人\n'
    '3.查询联系人\n'
    '4.显示所有联系人\n'
    '5.退出\n'
    )

def menu_options(option):
    if option == 1:
        name=input('要增加的姓名:')
        tel=int(input('电话号码:'))
        address_append(name,tel)
    elif option == 2:
        list_allname()
        name=input('要删除的姓名:')
        address_delete(name)
    elif option == 3:
        name=input('要查找的姓名:')
        address_search(name)
    elif option == 4:
        list_allname()
    elif option == 5:
        exit(0)
    else:
        print('没有这个选项')

def address_append(name,tel):
    if address_book.get(name) == None:
        address_book[name]=[tel]
    else:
        address_book[name].append(tel)

def list_allname():
    for name,tel in address_book.items():
        if len(tel) == 1:
            print('姓名:',name,' 电话:',tel[0],sep='')
        else:
            print('姓名:',name,sep='')
            for i in range(len(tel)):
                print('  电话',i+1,':',tel[i],sep='')

def address_search(name):
    tel=address_book.get(name)
    if tel == None:
        print('找不到'+name)
    else:
        if len(tel) == 1:
            print('姓名:',name,' 电话:',tel[0],sep='')
        else:
            print('姓名:',name)
            for i in range(len(tel)):
                print('  电话',i+1,':',tel[i],sep='')
def address_delete(name):
    tel=address_book.get(name)
    if tel != None:
        if len(tel) == 1:    
            del address_book[name]
        else:
            print(name+'的电话有:')
            for i in range(len(tel)):
                print(i+1,tel[i],sep=':')
            pos=int(input('要删除哪个?'))
            while pos > len(tel) and pos <= 0:
                pos=int(input('输入错误，请重新输入:'))
            tel.pop(pos-1)
            address_book[name]=tel
        print('已删除')
    else:    
        print('没有这个人')

def main():
    print_menu()
    option=int(input('你要做什么？'))
    menu_options(option)
    print('\n')
    main()

main()
