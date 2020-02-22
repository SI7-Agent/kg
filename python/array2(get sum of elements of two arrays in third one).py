q = input('Кол-во элементов в массиве 1: ')
c1 = False
while c1 == False or (c1 == True and q < 0):
    try:
        q = int(q)
        c1 = True
        print()
    except ValueError:
        print()
        print('Error')
        c1 = False
    if c1 == False or (c1 == True and q < 0):
        q = input('Введите правильное число: ')
        c1 = False
q = int(q)
w = input('Кол-во элементов в массиве 2: ')
d1 = False
while d1 == False or (d1 == True and w < 0):
    try:
        w = int(w)
        d1 = True
    except ValueError:
        print()
        print('Error')
        d1 = False
    if d1 == False or (d1 == True and w < 0):
        w = input('Введите правильное число: ')
        d1 = False
w = int(w)
a = []
b = []
print()
f = str(input('Заполнить массивы автоматически? y/n '))
print()
if f == 'y':
    import random
    t = float(input('Введите левую границу значений массива: '))
    y = float(input('Введите правую границу значений массива: '))
    for i in range(q):
        a.append(random.uniform(t, y))
    for i in range(w):
        b.append(random.uniform(t, y))
    c = []
    if q > w:
        e = q - w
        for i in range(e):
            b.append(0)
        for i in range(q):
            c.append(a[i] + b[i])
    elif q < w:
        e = w - q
        for i in range(e):
            a.append(0)
        for i in range(w):
            c.append(a[i] + b[i])
    else:
        for i in range(q):
            c.append(a[i] + b[i])
else:
    a = [0] * q
    b = [0] * w
    for i in range(q):
        a1 = False
        print('Введите ', i + 1, '-ое', ' число для массива №1: ', sep = '')
        a[i] = input('Ввод числа для массива №1: ')
        while a1 == False:
            try:
                y = float(a[i])
                print()
                a1 = True
            except ValueError:
                print()
                print('Error')
                a1 = False
            if a1 == False:
                a[i] = input('Введите правильное число: ')
        a[i] = float(a[i])
    print()
    for i in range(w):
        b1 = False
        print('Введите ', i + 1, '-ое', ' число для массива №2: ', sep = '')
        b[i] = input('Ввод числа для массива №2: ')
        while b1 == False:
            try:
                y = float(b[i])
                b1 = True
                print()
            except ValueError:
                print()
                print('Error')
                b1 = False
            if b1 == False:
                b[i] = input('Введите правильное число: ')
        b[i] = float(b[i])
    c = []
    if q > w:
        e = q - w
        for i in range(e):
            b.append(0)
        for i in range(q):
            c.append(a[i] + b[i])
    elif q < w:
        e = w - q
        for i in range(e):
            a.append(0)
        for i in range(w):
            c.append(a[i] + b[i])
    else:
        for i in range(q):
            c.append(a[i] + b[i])
print(a)
print(b)
print(c)