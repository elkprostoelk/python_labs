a=int(input('Введите целое число: '))
defstr='число'
if a%2==0 and a!=0:
    defstr='четное '+defstr
elif a%2!=0 and a!=0:
    defstr='нечетное '+defstr
if a>0:
    defstr='положительное '+defstr
elif a==0:
    defstr='нулевое '+defstr
else:
    defstr='отрицательное '+defstr
print(defstr)