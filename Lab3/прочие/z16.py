from random import randint
game1=('Камень','Ножницы','Бумага')
game2=('камень','ножницы','бумагу')
a=randint(0,2)
b=randint(0,2)
print('1:',game1[a])
print('2:',game1[b])
if a==b:
    print('Ничья!') #кк, нн, бб
else:
    if a==0:
        if b==1:
            print(game1[0],'бъет',game2[1]) #кн
        else:
            print(game1[2], 'бъет', game2[0]) #кб
    elif a==1:
        if b==0:
            print(game1[0], 'бъет', game2[1]) #нк
        else:
            print(game1[1], 'бъют', game2[2]) #нб
    else:
        if b==0:
            print(game1[2], 'бъет', game2[0]) #бк
        else:
            print(game1[1], 'бъют', game2[2]) #бн