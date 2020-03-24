try:
    f=open('collection.txt','r')
except FileNotFoundError:
    print('Файл не обнаружен')
except IsADirectoryError:
    print('Объект по указанному пути является директорией')
else:
    col=[int(i) for i in f.read().split(' ')]
    f.close()
    n=[1,]
    k=0
    for i in range(len(col)-1):
        if col[i]==col[i+1]:
            n[k]+=1
        else:
            n.append(1)
            k+=1
    print(col)
    print(n)