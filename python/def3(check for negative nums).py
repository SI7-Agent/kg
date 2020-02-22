q = input('Кол-во элементов в массиве: ')
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
a = [0] * q
for i in range(q):
    a1 = False
    print('Введите ', i + 1, '-ое', ' число: ', sep='')
    a[i] = input('Ввод числа: ')
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
print(a)
m = -1
p = -1
for i in range(q):
    if a[i] < 0.0:
        m = i
        break
for i in range(q):
    if a[i] < 0.0:
        p = i
if m == p == -1:
    print('Отрицательных чисел нет')
    quit()
s = 0
for i in range(m, q):
    if a[i] > 0:
        s += a[i]
a.insert(p, s)
a.remove(a[p+1])
print(a)

