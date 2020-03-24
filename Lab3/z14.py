from random import randint
def reversenumb(a):
    a=str(a)
    a=a[::-1]
    a=int(a)
    return a
numbers=[randint(100,999) for i in range(5)]
maxim=numbers[0]
for i in range(1,len(numbers)):
    if numbers[i]>maxim:
        maxim=numbers[i]
print(maxim)
print(numbers)
for i in range(0,len(numbers)):
    numbers[i]=reversenumb(numbers[i])
maxim=numbers[0]
for i in range(1,len(numbers)):
    if numbers[i]>maxim:
        maxim=numbers[i]
print(maxim)
print(numbers)