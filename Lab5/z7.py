from random import randint
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a=randint(10,100)
b=randint(10,100)
c=randint(10,100)
d=randint(10,100)
print(a,b,c,d)
print(gcd(a,b))
print(gcd(a,c))
print(gcd(a,d))