try:
    fin=open('matrix1.txt','r')
except FileNotFoundError:
    print('Файл не найден')
except IsADirectoryError:
    print('Объект по указанному пути является директорией')
else:
    matrix=list()
    for i in fin.readlines():
        matrix.append([float(j) for j in i.split(' ')])
    fin.close()
    for i in matrix:
        if len(i)<len(matrix[0]):
            for j in range(len(matrix[0])-len(i)):
                i.insert(0,0.0)
    try:
        fout=open('matrix2.txt','w')
    except FileExistsError:
        print('Файл с указанным именем уже открыт')
    else:
        for i in matrix:
            for j in i:
                fout.write(str(j)+' ')
            fout.write('\n')
        fout.close()