a=int(input('Введите двузначное число: '))
suma=0
dob=1
while a != 0:
    suma += a % 10
    dob *= a % 10
    a //= 10
print('Сумма цифр: {0} Произведение цифр: {1}'.format(suma,dob))