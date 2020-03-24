strn=input('Введите строку: ')
strn=strn.replace(' ','')
strn=strn.lower()
strn1=strn[::-1]
if strn==strn1:
    print('Это палиндром')
else:
    print('Не палиндром')