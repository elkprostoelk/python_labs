from random import uniform
from math import log,floor
def dayOfWeek(a):
    if a==1:
        return 'понедельник'
    elif a==2:
        return 'вторник'
    elif a==3:
        return 'среда'
    elif a==4:
        return 'четверг'
    elif a==5:
        return 'пятница'
    elif a==6:
        return 'суббота'
    elif a==7:
        return 'воскресенье'
    else:
        return 'error'
x=uniform(-10,10)
a=uniform(1,10)
b=uniform(1,10)
y=log(x**2+a*b)
y=floor(y)
print(y,dayOfWeek(y%7))