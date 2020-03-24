string=input('Введите строку: ')
string=string.lower()
words=string.split()
words.sort()
for i in words:
    print(i)