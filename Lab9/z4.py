try:
    f=open('realnum.txt','r',encoding='windows-1251')
except FileNotFoundError:
    print('Файл не обнаружен')
except IsADirectoryError:
    print('Объект по указанному пути является директорией')
else:
    numbers=[float(i) for i in f.readlines()]
    f.close()
    print(numbers)
    for i in range(len(numbers)):
        numbers[i]=numbers[i]**2
    print(numbers)
    f=open('realnum.txt','w',encoding='windows-1251')
    for i in numbers:
        f.write(str(i)+'\n')
    f.close()