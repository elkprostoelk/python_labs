from math import sqrt
A=float(input('A='))
B=float(input('B='))
C=float(input('C='))
D=B**2-4*A*C
x1=(-B+sqrt(D))/(2*A)
x2=(-B-sqrt(D))/(2*A)
if x1<x2:
    print(x1,x2)
else:
    print(x2,x1)