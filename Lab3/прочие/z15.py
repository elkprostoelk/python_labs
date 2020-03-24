from random import randint
m=[[randint(-10,10) for j in range(3)] for i in range(3)]
for i in m:
    print(i)
maindiag=m[0][0]*m[1][1]*m[2][2]+m[0][1]*m[1][2]*m[2][0]+m[1][0]*m[2][1]*m[0][2]
sidediag=m[2][0]*m[1][1]*m[0][2]+m[1][0]*m[0][1]*m[2][2]+m[2][1]*m[1][2]*m[0][0]
print(maindiag-sidediag)