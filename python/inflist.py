eps = float(input('Введите число eps: '))
step = int(input('Введите шаг значений: '))
x = int(input('Введите кол-во итераций: '))
q = float(input('Под знаком lg: '))
a = float(input('Число а: '))
from math import *
i = 0
n = 0
t = a**n * log(q)**n/factorial(n)
sum = t
print('\t', '\u250c', '\u2500' * 15, '\u252c', '\u2500' * 15, '\u252c', '\u2500' * 31, '\u252c', '\u2500' * 31,
      '\u2510', sep='')
print('\t', '{:s}{:^13s}{:s}{:^13s}{:s}{:^26s}{:s}{:^27s}{:s}' \
      .format('\u2502', 'N', '\u2502', 'x текущее', '\u2502', 'текущий член ряда', '\u2502',
              'текущее значение суммы', '\u2502', ), sep='')
for i in range(x+1):
    print('\t', '\u251c', '\u2500' * 15, '\u253c', '\u2500' * 15, '\u253c', '\u2500' * 31, '\u253c', '\u2500' * 31,
          '\u2524', sep='')
    print('\t', '{:s}{:^13d}{:s}{:^13.2f}{:s}{:^26.4f}{:s}{:^27.4f}{:s}' \
          .format('\u2502', i + 1, '\u2502', n, '\u2502', t, '\u2502', sum, '\u2502'), sep = '', end = '')
    n += step
    t *= a**step * log(q)**step / (factorial(n) / factorial(n - step))
    sum += t
    print()
    if abs(t) <= eps:
        break
print('\t', '\u2514', '\u2500' * 15, '\u2534', '\u2500' * 15, \
          '\u2534', '\u2500' * 31, '\u2534', '\u2500' * 31, '\u2518', sep='')
if abs(t) <= eps:
    print('Ряд сошелся на ', i+1, '-ом', ' элементе', sep = '')
    print('Сумма элементов: ', '{:.4f}'.format(sum))
else:
    print('Ряд не сходится за ', x, ' итераций')
