def symetr_str(st,i,j):
    if i>=j:
        return True
    if st[i]==st[j]:
        return symetr_str(s,i+1,j-1)
    else:
        return False
s=input()
i=int(input())
j=int(input())
print(symetr_str(s,i,j))