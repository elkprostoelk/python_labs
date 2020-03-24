date1=(3,1900)
date2=(9,2020)
date3=[int(i) for i in input().split()]
print(date3)
if (date3[1]>=date1[1] and date3[1]<=date2[1]) and (date3[0]>=date1[0] and date3[0]<=date2[0]):
    print('Принадлежит диапазону')
else:
    print('Не принадлежит диапазону')