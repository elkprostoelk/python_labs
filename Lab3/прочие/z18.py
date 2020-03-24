d=int(input('донор: '))
r=int(input('реципиент: '))
if d==r:
    print('Да')
else:
    if d==1:
        print('Да')
    elif d==2:
        if r==2 or r==4:
            print('Да')
        else:
            print('Нет')
    elif d==3:
        if r==3 or r==4:
            print('Да')
        else:
            print('Нет')
    else:
        if r==4:
            print('Да')
        else:
            print('Нет')