N1='a'
N2='a'
a='a'
b='a'
t=1
while N1.isdigit() == False:
    N1 = str(input('Введите количество шагов (вариант 1): '))
    if N1.isdigit() == False:
        print('Неверный ввод. Введите натуральное число не равное 0')
N1 = int(N1)
print()
while N2.isdigit() == False:
    N2 = str(input('Введите количество шагов (вариант 2): '))
    if N2.isdigit() == False:
        print('Неверный ввод. Введите натуральное число не равное 0')
N2 = int(N2)
print()
while t != 0:
    t = 0
    a = str(input('Введите минимальное значение х: '))
    if a[0] in '-1234567890':
        t = t
    else:
        t+=1
    for i in range(1,len(a)):
        if a[i] in '.1234567890':
            t=t
        else:
            t+=1
    if t!=0:
        print('Неверный ввод. Введите число.')
t = 1
a = int(a)
print()
while t != 0:
    t = 0
    b = str(input('Введите максимальное значение х: '))
    if b[0] in '-1234567890':
        t = t
    else:
        t+=1
    for i in range(1,len(b)):
        if b[i] in '.1234567890':
            t=t
        else:
            t+=1
    if t!=0:
        print('Неверный ввод. Введите число.')
b = int(b)
print()

def f(x):
    return x

def metodcent(f,a,b,n):
    s = 0
    h = (b - a) / n
    for i in range(n):
        s += f(a + i * h + h / 2)
    s *= h
    return s

def metodtrap(f,a,b,n):
    s = (f(a) + f(b)) / 2
    h = (b - a) / n
    for i in range(1, n):
        s += f(a + i * h)
    s *= h
    return s

I11 = metodcent(f,a,b,N1)
I12 = metodcent(f,a,b,N2)
I21 = metodtrap(f,a,b,N1)
I22= metodtrap(f,a,b,N2)

print('\n N1, N2:                |', '{}'.format(N1).center(20), '|', '{}'.format(N2).center(20) + '\n' + '-' * 69)
print(' Ср. прямоугольники:    |', '{:.5}'.format(I11).center(20), '|', '{:.5}'.format(I12).center(20) + '\n' + '-' * 69)
print(' Трапеции:              |', '{:.5}'.format(I21).center(20), '|', '{:.5}'.format(I22).center(20))
print()
eps = float(input('Введите эпсилон: '))
print()
n=1
I11 = metodcent(f,a,b,n)
I12 = metodcent(f,a,b,n*2)
I21 = metodtrap(f,a,b,n)
I22= metodtrap(f,a,b,n*2)
if abs(I11-I12) > abs(I21-I22):
    while abs(I11-I12) > eps:
        n *= 2
        I11 = metodcent(f,a,b,n)
        I12 = metodcent(f,a,b,n*2)
    print('Наименее точный метод - метод средних прямоугольников')
    print('Метод приведет к точности эпсилон при', n, 'операциях')
    print('Значение интеграла при этом: ', I12)
else:
    while abs(I21-I22)>eps:
        n *= 2
        I21 = metodtrap(f,a,b,n)
        I22 = metodtrap(f,a,b,n*2)
    print('Наименее точный метод - метод трапеции')
    print('Метод приведет к точности эпсилон при', n, 'операциях')
    print('Значение интеграла при этом:',I22)
