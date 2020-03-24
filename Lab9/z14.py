try:
    f=open('dates.txt','r',encoding='windows-1251')
except FileNotFoundError:
    print('Файл не найден')
else:
    datesstr=f.readlines()
    f.close()
    datesint=list()
    for i in datesstr:
        datesint.append([int(j) for j in i.split('/')])
    f1=open('days.txt','w')
    f2=open('months.txt','w')
    for i in datesint:
        f1.write(str(i[0])+'\n')
        f2.write(str(i[1]) + '\n')
    f1.close()
    f2.close()