def nsk(a,b):
    a1=a
    b1=b
    while a1!=b1:
        if a1>b1:
            a1=a1-b1
        else:
            b1=b1-a1
    return (a*b)//a1
a=int(input('A='))
b=int(input('B='))
print('НОК({0},{1})={2}'.format(a,b,nsk(a,b)))