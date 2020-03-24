def sumnumbers(string):
    summ=0
    for i in string:
        summ+=i
    return summ
numb=[int(c) for c in input().split()]
print(sumnumbers(numb))