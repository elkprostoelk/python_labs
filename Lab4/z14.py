def ispower2(a):
    if a%2!=0:
        return 'NO'
    if a==2:
        return 'YES'
    else:
        return ispower2(a//2)
n=int(input('N='))
print(ispower2(n))
