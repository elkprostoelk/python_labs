def poluchit_nominal(a):
    if a==6:
        return 'Шестерка'
    elif a==7:
        return 'Семерка'
    elif a==8:
        return 'Восьмерка'
    elif a==9:
        return 'Девятка'
    elif a==10:
        return 'Десятка'
    elif a==11:
        return 'Валет'
    elif a==12:
        return 'Дама'
    elif a==13:
        return 'Король'
    elif a==14:
        return 'Туз'
    else:
        return 'Error'
def poluchit_mast(a):
    if a==1:
        return ' пик'
    elif a==2:
        return ' треф'
    elif a==3:
        return ' бубнов'
    elif a==4:
        return ' черв'
    else:
        return ' error'
N=int(input('Введите номинал карты: '))
M=int(input('Введите масть: '))
print(poluchit_nominal(N)+poluchit_mast(M))
