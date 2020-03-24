def rec(n):
    if n<10:
        return n
    return int(str(n%10)+str(rec(n//10)))
chislo=int(input())
print(rec(chislo))