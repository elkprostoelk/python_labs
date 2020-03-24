from random import randint
def minimal(listn):
    minim=0
    for i in range(len(lst)):
        if lst[i] < lst[minim]:
            minim = i
    return minim
lst=[randint(-10,10) for i in range(randint(4,8))]
print(lst)
minim=minimal(lst)
print(minim)
while minim!=0:
    temp=lst[len(lst)-1]
    lst.remove(lst[len(lst)-1])
    lst.insert(0,temp)
    print(lst)
    minim=minimal(lst)