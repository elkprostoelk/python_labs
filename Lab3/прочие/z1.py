from random import randint
def printMatrix(matr):
    print('*'*4)
    for i in range(len(matrix)):
        print(matrix[i])
    print('*' * 4)


n=int(input('N='))
matrix = [0] * n
for i in range(n):
    matrix[i] = [0] * n
for i in range(n):
    for j in range(n):
        matrix[i][j]=randint(-10,20)
printMatrix(matrix)
for i in range(0,len(matrix)):
    for j in range(0,len(matrix)):
        if i!=len(matrix)-1:
            matrix[i][j]-=matrix[len(matrix)-1][j]
printMatrix(matrix)