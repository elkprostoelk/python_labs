n=int(input('N='))
summ=0
for i in range(1,n):
    if n%i==0:
        summ+=i
if n==summ:
    print('Число совершенное')
else:
    print('Число не совершенное')