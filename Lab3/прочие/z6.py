from random import randint
lst=[randint(-5,5) for i in range(10)]
print(lst)
lstmn=set(lst)
for i in lstmn:
    print('Элемент {0} встречается в списке {1} раз(а)'.format(i, lst.count(i)))