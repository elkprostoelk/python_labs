def IsPower5(k):
    while k%5==0 and k>1:
        k=k//5
    if k==1:
        return True
    else:
        return False
numb=[5, 7, 4, 25, 3125, 3, 15, 76, 18, 125]
k=0
for i in range(len(numb)):
    if IsPower5(numb[i]):
        k+=1
print('Степеней числа 5:', k)