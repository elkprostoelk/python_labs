from math import sqrt
def IsSquare(k):
    if sqrt(k)==int(sqrt(k)):
        return True
    else:
        return False
numb=[5, 7, 4, 25, 625, 1, 16, 76, 18, 125]
k=0
for i in range(len(numb)):
    if IsSquare(numb[i]):
        k+=1
print('Квадратов:', k)