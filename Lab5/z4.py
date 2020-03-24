k=0
def fib1(n):
    global k
    k+=1
    if n==1 or n==2:
        return 1
    else:
        return fib1(n-1)+fib1(n-2)
n=int(input('N='))
fibon=[fib1(i) for i in range(1,n+1)]
print(fibon)
print('Число вызовов функции fib1:',k)
