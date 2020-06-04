numbers=[34, 23, 52, 46, 42, 26, 31]
for i in range(0, len(numbers)):
    for j in range(len(numbers)-1,i,-1):
        if numbers[j]>numbers[j-1]:
            tmp=numbers[j]
            numbers[j]=numbers[j-1]
            numbers[j-1]=tmp
print(numbers)