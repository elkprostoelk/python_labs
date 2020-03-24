try:
    f1=open('f1.txt','r+') #encoding='windows-1251' нужно, если файл создан в кодировке ANSI
    f2=open('f2.txt','r+')
except FileNotFoundError:
    print('Файл(ы) не найден(ы)')
except (UnicodeEncodeError, UnicodeDecodeError, UnicodeTranslateError):
    print('Ошибка кодирования в Unicode')
else:
    str1=f1.read()
    str2=f2.read()
    f2.write('\n'+str1)
    f1.write('\n'+str2)
    f1.close()
    f2.close()