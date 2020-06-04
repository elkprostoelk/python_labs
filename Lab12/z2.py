n = int(input('Введите размерность доски\n'))
wave_one = 1
wave_two = 2
x1 = int(input('Введите координату х начальной точки\n'))
y1 = int(input('Введите координату y начальной точки\n'))
x2 = int(input('Введите координату х конечной точки\n'))
y2 = int(input('Введите координату y конечной точки\n'))
way = []
num_way=0
global num_of_wave
num_of_wave = 0
global matrix
matrix = [[' '] * n for i in range(n)]


def check_matrix(matrix: list):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == ' ':
                return True
    return False


def check_coordinates(a, b, var):
    if a <= n and b <= n and a >= 0 and b >= 0:
        matrix[b][a] = var
    else:
        print('Эти координаты не подходят')


def print_waves(matrix):
    print('   ', end='')
    for i in range(n):
        print(i, '|', end='')
    print('\n')
    print('   ', end='')
    for i in range(n):
        print('=', ' ', end='')
    print('\n')
    for i in range(n):
        for j in range(n + 2):
            if j == 0:
                print(i, end='')
                continue
            if j == 1:
                print('||', end='')
                continue
            if j > 1:
                print(matrix[i][j - 2], "|", end='')
        print('\n')


def wave(x0, y0):
    theEnd = True

    def step(x0, y0, wave_one, wave_two):
        x1 = x0 + wave_one
        y1 = y0 + wave_two
        x2 = x0 + wave_two
        y2 = y0 + wave_one

        def check(a, b):
            def check(a):
                if a <= n - 1 and a >= 0:
                    return True

            if check(a):
                if check(b):
                    if matrix[a][b] != 'end':
                        if matrix[a][b] == ' ':
                            global num_of_wave
                            matrix[a][b] = num_of_wave + 1
                    else:
                        nonlocal theEnd
                        theEnd = False

        check(x1, y1)
        check(x2, y2)
    step(x0, y0, wave_one, wave_two)
    step(x0, y0, -wave_one, wave_two)
    step(x0, y0, wave_one, -wave_two)
    step(x0, y0, -wave_one, -wave_two)
    return theEnd


def algorithm_build_waves():
    theEnd = True
    while theEnd:
        for i in range(n):
            for j in range(n):
                global num_of_wave
                if matrix[i][j] == num_of_wave:
                    theEnd = wave(i, j)
                    theEnd = (theEnd == check_matrix(matrix))
                    if theEnd != True:
                        break
            if theEnd != True:
                break
        num_of_wave += 1

def algorithm_li(x0, y0, num):
    def step(x0, y0, wave_one, wave_two):
        x1 = x0 + wave_one
        y1 = y0 + wave_two
        x2 = x0 + wave_two
        y2 = y0 + wave_one

        def check(a, b):
            def check(a):
                if a <= n - 1 and a >= 0:
                    return True

            if check(a):
                if check(b):
                    return True
            return False

        global num_way
        if check(x1, y1):
            if matrix[x1][y1] == 0:
                way.append([x1, y1])
                num_way += 1
                return True
            if matrix[x1][y1] == num:
                if algorithm_li(x1, y1, num - 1):
                    num_way += 1
                    way.append([x1, y1, num])
                    return True
        if check(x2, y2):
            if matrix[x2][y2] == 0:
                num_way += 1
                way.append([x2, y2, num])
                return True
            if matrix[x2][y2] == num:
                if algorithm_li(x2, y2, num - 1):
                    num_way += 1
                    way.append([x2, y2, num])
                    return True
        return False

    if step(x0, y0, wave_one, wave_two):
        return True
    if step(x0, y0, -wave_one, wave_two):
        return True
    if step(x0, y0, wave_one, -wave_two):
        return True
    if step(x0, y0, -wave_one, -wave_two):
        return True
    return False


check_coordinates(x1, y1, 0)
check_coordinates(x2, y2, 'e')
algorithm_build_waves()
print_waves(matrix)
algorithm_li(x2, y2, num_of_wave - 1)
way.append([x2, y2])
print('Количество ходов:',num_way)
print('Первые координаты - начало, остальные - конечные')
print(way)