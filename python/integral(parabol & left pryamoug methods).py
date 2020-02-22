# Программа рассчитывает интеграл методами парабол и левых прямоугольников,
# двумя количествами делений. Находит наименее точный метод
# и высчитывает количество делений для точности eps.
#
# a, b - отрезок
# n1, n2, n - количества делений
# h - шаг для делений
# y - функция
# I1, I2, I3, I4 - результаты методов
# average - среднее из них

a, b = map(int, input('Введите границы отрезка через пробел: ').split(' '))
n1, n2 = map(int, input('N1, N2: ').split(' '))

def f(x):
    y = x*x*x
    return y

def parabola(n):
    s = 0
    h = (b - a) / n
    for i in range(n):
        s += f(a + i * h) + 4 * f(a + i * h + h / 2) + f(a + i * h + h)
    s *= h / 6
    return s

def leftRect(n):
    s = 0
    h = (b - a) / n
    for i in range(n):
        s += f(a + i * h)
    s *= h
    return s

I1 = parabola(n1)
I2 = parabola(n2)
I3 = leftRect(n1)
I4 = leftRect(n2)
I = [I1, I2, I3, I4]
average = sum(I) / 4
if I1 != I3 and I2 != I4:
    for i in range(len(I)):
        I[i] = abs(I[i] - average)
    netochny_method_num = (I.index(max(I)) + 2) // 2
else:
    netochny_method_num = 3

print('\n N1, N2:              |', '{}'.format(n1).center(20), '|', '{}'.format(n2).center(20) + '\n' + '-' * 69)
print(' Параболы:            |', '{:.5}'.format(I1).center(20), '|', '{:.5}'.format(I2).center(20) + '\n' + '-' * 69)
print(' Лев. прямоугольники: |', '{:.5}'.format(I3).center(20), '|', '{:.5}'.format(I4).center(20))

if netochny_method_num == 3:
    print('\nВсе методы точны.')
else:
    print('\nСамый неточный метод:', netochny_method_num)
    eps = float(input('\nВведите eps: '))
    n = 2
    if netochny_method_num == 1:
        while abs(parabola(2 * n) - parabola(n)) > eps:
            n *= 2
    elif netochny_method_num == 2:
        while abs(leftRect(2 * n) - leftRect(n)) > eps:
            n *= 2
    print(f'Точность eps при {n}')