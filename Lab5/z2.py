from random import randint
def fact2(n):
    if n%2==0:
        if n==2:
            return n
        else:
            return n*fact2(n-2)
    else:
        if n==1:
            return n
        else:
            return n*fact2(n-2)
numbers=[randint(1,10) for i in range(1,6)]
numbersfact=[fact2(i) for i in numbers]
print(numbers)
print(numbersfact)