address_book=[]
def print_menu():
    print(
    '====通讯录管理系统====\n'
    '1.增加姓名和手机\n'
    '2.删除姓名\n'
    '3.修改手机\n'
    '4.查询所有用户\n'
    '5.根据姓名查找手机号\n'
    )

def menu_options(option):
    if option == 1:
        name=input('要增加的姓名')
        tel=int(input('电话号码'))
        address_append(name,tel)
    elif option == 2:
        list_allname()
        name=input('要删除的姓名')
        address_delete(name)
    elif option == 3:
        list_allname()
        print('\n')
        name=input('要修改谁的手机')
        tel=int(input('电话号码'))
        address_change(name,tel)
    elif option == 4:
        list_allname()
    elif option == 5:
        name=input('要查找的姓名')
        i=address_search(name)
        if i != None:
            print(name+'的电话是'+str(address_book[i][1]))
        else:
            print('找不到'+name)
    else:
        return 1

def address_append(name,tel):
    address_book.append([name,tel])

def list_allname():
    for i in range(len(address_book)):
        print('姓名:'+str(address_book[i][0])+' 电话:'+str(address_book[i][1]),end='\n')

def address_search(name):
    for i in range(len(address_book)):
        if name in address_book[i]:
            return i
        else:
            return None

def address_delete(name):
    address_book.pop(address_search(name))

def address_change(name,tel):
    if address_search(name) != None:
        address_book[address_search(name)][1]=tel
    else:
        print('没有这个人')
        
def main():
    print_menu()
    option=int(input('你要做什么？'))
    if not menu_options(option):
        print('\n')
        return main()

main()
