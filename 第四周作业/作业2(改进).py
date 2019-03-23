import os
address_book=[]
def print_menu():
    print(
    '====通讯录管理系统====\n'
    '1.增加姓名和手机\n'
    '2.删除姓名\n'
    '3.修改手机\n'
    '4.查询所有用户\n'
    '5.根据姓名查找手机号\n'
    '0.退出\n'
    )

def menu_options(option):
    if option == 0:
        exit(0)
    elif option == 1:
        out=input('输入q退出')
        if out == 'q':
            main()
        else:
            name=input('\n要增加的姓名:')
            tel=int(input('电话号码:'))
            address_append(name,tel)
            print('保存成功!')
            menu_options(1)
        
    elif option == 2:
        list_allname()
        out=input('输入q退出')
        if out == 'q':
            main()
        else:
            name=input('\n要删除的姓名:')
            address_delete(name)
            menu_options(2)
    elif option == 3:
        list_allname()
        out=input('输入q退出')
        if out == 'q':
            main()
        else:
            name=input('\n要修改谁的手机:')
            i = address_search(name)
            if len(i) == 0:
                print('没有这个人')
            elif len(i) == 1:
                tel=int(input('电话号码:'))
                address_change(i[0],tel)
            else:
                print(name+'的电话是')
                n=0
                for j in i:
                    n+=1
                    print('\n'+str(n)+':'+str(address_book[j][1]))
                pos=int(input('要修改哪个:'))-1
                tel=int(input('电话号码:'))
                address_change(i[pos],tel)
            menu_options(3)
    elif option == 4:
        list_allname()
        main()
    elif option == 5:
        out=input('输入q退出')
        if out == 'q':
            main()
        else:
            name=input('\n要查找的姓名:')
            i=address_search(name)
            if i != None:
                for j in i:
                    print(name+'的电话是'+str(address_book[j][1]))
            else:
                print('找不到'+name)
        menu_options(5)
    else:
        print('没有这个选项')
        main()

def address_append(name,tel):
    address_book.append([name,tel])

def list_allname():
    for i in range(len(address_book)):
        print('姓名:'+str(address_book[i][0])+' 电话:'+str(address_book[i][1]),end='\n')

def address_search(name):
    pos=[]
    for i in range(len(address_book)):
        if name in address_book[i]:
            pos.append(i)
        else:
            return None
    return pos

def address_delete(name):
    i=address_search(name)
    if len(i) == 0:
        print('没有这个人')
    elif len(i) == 1:
        address_book.pop(i[0])
    else:
        print(name+'的电话是')
        n=0
        for j in i:
            n+=1
            print('\n'+str(n)+':'+str(address_book[j][1]))
        pos=int(input('要删除哪个:'))-1
        address_book.pop(i[pos])

def address_change(pos,tel):
    address_book[pos][1]=tel
        
def main():
    print('\n')
    print_menu()
    option=int(input('你要做什么？'))
    if option == 1:
        print('增加姓名和手机')
    elif option == 2:
        print('删除姓名\n')
    elif option == 3:
        print('修改手机\n')
    elif option == 4:
        print('查询所有用户\n')
    elif option == 5:
        print('根据姓名查找手机号\n')
    menu_options(option)


if __name__ == "__main__":
    main()
