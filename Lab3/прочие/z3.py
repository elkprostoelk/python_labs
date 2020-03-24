from random import randint
def sumMainDiag():
    sum=0
    for i in range(n):
        sum+=matrix[i][i]
    return sum
def sumSideDiag():
    sum=0
    for i in range(n):
        sum+=matrix[n-1-i][i]
    return sum
n=int(input('N='))
matrix = [0] * n
for i in range(n):
    matrix[i] = [0] * n
for i in range(n):
    for j in range(n):
        matrix[i][j]=randint(-10,20)
print(matrix)
print('По главной диагонали:',sumMainDiag())
print('По побочной диагонали:',sumSideDiag())
