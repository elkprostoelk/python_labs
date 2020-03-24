from random import randint
numb=[randint(-10,10) for i in range(randint(3,6))]
print(numb)
maxelm=numb[0]
for i in range(len(numb)):
    if numb[i]>maxelm:
        maxelm=numb[i]
print(maxelm)
for i in range(len(numb)):
    if numb[i]!=maxelm:
        numb[i]=numb[i]/maxelm
numb.remove(maxelm)
print(numb)