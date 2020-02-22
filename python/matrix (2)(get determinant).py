def solve(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            total += mul * solve(m, sign * matrix[0][i])
        return total

matrix = []
a = int(input('Размерность: '))
print()
for i in range(a):
    m0 = []
    for j in range(a):
        print('Число [', i+1, '][', j+1, '] матрицы: ')
        s = float(input())
        print()
        m0.append(s)
    matrix.append(m0)
for i in range(a):
    print(matrix[i])
print()
print('Детерминант матрицы равен: ', solve(matrix, 1))