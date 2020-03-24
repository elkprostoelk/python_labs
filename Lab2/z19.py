def fib(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fib(a-1)+fib(a-2)
n=int(input('N='))
k=0
while n>=fib(k):
    if n==fib(k):
        print('это число Фибоначчи')
    k+=1
k-=1
if n!=fib(k):
    print('это не число Фибоначчи')