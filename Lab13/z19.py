numbers=[34, 23, 52, 46, 42, 26, 31]
for j in range(1,len(numbers)):
    key=numbers[j]
    i=j-1
    while i>=0 and numbers[i]>key:
        numbers[i+1]=numbers[i]
        i=i-1
        numbers[i+1]=key
print(numbers)