from random import randint
n=randint(3,6)
lists=[[randint(-10,10) for j in range(n)] for i in range(n)]
print(lists)
summ=0
for i in range(n):
    for j in range(n):
        summ+=lists[i][j]
        if i==0:
            maxl=summ
    print(summ)
    if summ>maxl:
        maxl=summ
        maxlist=lists[i]
    summ=0
print('Списком с максимальной суммой {0} является список {1}'.format(maxl,maxlist))
