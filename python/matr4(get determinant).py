
def base(matrix):
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
def print_matrix(m):
    for x in m:
        print(x)
    print()
def solve(matrix, mat0):
    width = len(matrix)
    if width == 1:
        return matrix[0][0]
    elif width == 2:
        print(mat0)
        print_matrix(matrix)
        return mat0 * base(matrix)
    else:
        sign = -1
        total = 0
        for i in range(width):
            m1 = []
            for j in range(1, width):
                m2 = []
                for k in range(width):
                    if k != i:
                        m2.append(matrix[j][k])
                m1.append(m2)
            sign *= -1     
            total += solve(m1, sign * matrix[0][i])
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
