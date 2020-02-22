a = []
l = int(input('Размерность матрицы: '))
for i in range(l):
    a0 = []
    for i in range(l):
        s = input('Элемент матрицы: ')
        a0.append(s)
    a.append(a0)
for i in range(l):
    print(a[i])
print()
for i in range(l):
    a[i][i], a[i][l - 1 - i] = a[i][l - 1 - i], a[i][i]
for i in range(l):
    print(a[i])