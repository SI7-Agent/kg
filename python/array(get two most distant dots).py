# для нахождения двух наиболее удаленных друг от друга точек
# выполнил:
# a - кол-во точек
# q - массив с координатами точек
# cmax - наибольшее расстояние между точками
# imax1 - координата x точки 1 с наибольшим расстоянием
# imax2 - координата x точки 2 с наибольшим расстоянием
# smax1 - координата y точки 1 с наибольшим расстоянием
# smax2 - координата y точки 2 с наибольшим расстоянием
# s - счетчик для цикла с координатами y
# i - счетчик для цикла с координатами x
# c - текущее расстояние между точками
# f - счетчик кол-ва расстояний

a = input('Введите кол-во точек: ')
a1 = False
while a1 == False or (a1 == True and int(a) < 2):
    try:
        a = float(a)
        a1 = True
        print()
    except ValueError:
        print()
        print('Error')
        a1 = False
    if a1 == False or (a1 == True and int(a) < 0):
        a = input('Введите правильное число: ')
        a1 = False
    if a1 == True and 0 <= int(a) < 2:
        a = input('Введите хотя бы 2 точки: ')
        a1 = False
a = int(a)
q = []
for i in range(a):
    print('Координаты точки', i + 1, ': ')
    print('Введите координату x: ')
    x = input('Ввод: ')
    x1 = False
    while x1 == False:
        try:
            x = float(x)
            x1 = True
            print()
        except ValueError:
            print()
            print('Error')
            x1 = False
        if x1 == False:
            x = input('Введите правильное число: ')
    x = float(x)
    q.append(x)
    print('Введите координату y: ')
    y = input('Ввод: ')
    y1 = False
    while y1 == False:
        try:
            y = float(y)
            y1 = True
            print()
        except ValueError:
            print()
            print('Error')
            y1 = False
        if y1 == False:
            y = input('Введите правильное число: ')
    y = float(y)
    q.append(y)
print('Введеные координаты:', q)
cmax = 0
imax1 = 0
smax1 = 0
imax2 = 0
smax2 = 0
f = 0
from math import sqrt
for i in range(0, 2 * a - 3, 2):
    for s in range(i + 1, 2 * a - 2, 2):
        f += 1
        c = sqrt((q[i] - q[s + 1])**2 + (q[i + 1] - q[s + 2])**2)
        if c > cmax:
            cmax = c
            imax1 = i
            smax1 = i + 1
            imax2 = s + 1
            smax2 = s + 2
        if len(str(c)) > 20:
            print('Расстояние между точками №', f, ' : ', '{:e}'.format(c), sep = '')
        else:
            print('Расстояние между точками №', f, ' : ', '{:.6f}'.format(c), sep='')
print('Наиболее удаленные друг от друга точки: ', q[imax1],
      '; ', q[smax1], ' и ', q[imax2], '; ', q[smax2], sep = '')