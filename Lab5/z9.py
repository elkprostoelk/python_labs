from random import randint
def maxelem(a,n):
    if n==2:
        return max(a[0],a[1])
    else:
        return max(maxelem(a,n-1),a[n-1])
na=randint(1,10)
nb=randint(1,10)
nc=randint(1,10)
a=[randint(-10,10) for i in range(na)]
b=[randint(-10,10) for i in range(nb)]
c=[randint(-10,10) for i in range(nc)]
print(a,maxelem(a,na))
print(b,maxelem(b,nb))
print(c,maxelem(c,nc))
