a = float(input('Начальное значение аргумента: '))
h = float(input('Шаг значений: '))
b = float(input('Конечное значение аргумента: '))
x = int((abs(b - a)) / abs(h) + 1)
U = []
C = [0] * x
for i in range(x):
    C[i] = a
    a += h
for i in range(0, x):
    r = C[i]**2 - 25
    U.append(r)
ymax = max(U)
ymin = min(U)
g = int((ymax + ymin)/2)
zn = int(68 * -ymin /(ymax - ymin))
print('{:^16.1f}{:^20.1f}{:^14.1f}{:^19.1f}{:^16.1f}'\
   .format(ymin, (g + ymin)/2, g,\
   (g + ymax)/2, ymax), sep = '')
print('{:^4s}'.format('a'), '\t', '\u251c' + '\u2500' * 19 +\
    '\u253c' + '\u2500' * 19 + '\u253c' + '\u2500' * 19 +\
    '\u253c' + '\u2500' * 19 + '\u2524' + '\u03b2', sep = '')
for i in range(x):
    f = int(68 * (U[i] - ymin) / (ymax - ymin))
    print('{:>5.2f}'.format(C[i]), sep = '', end = '')
    if ymax < 0 or ymin > 0:
        print('\t', ' ' * f, '*', sep = '')
    else:
        if zn > f:
            print('\t', ' ' * f, '*', ' ' * (zn - f - 1), '\u2502', sep = '')
        elif zn < f:
            print('\t', ' ' * zn, '\u2502', ' '* (f - zn), '*', sep = '')
        else:
            print('\t', ' ' * zn, '*', sep = '')