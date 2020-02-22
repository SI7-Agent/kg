# Nmax - максимальное количество итераций
# eps - эпсилон
# x - занчение n
# step - шаг вывода
# N - номер итерации
# p - признак схождения ряда
# h1 - член ряда
# S - сумма
# e - вертикальная линия
# f - горизонтальная линия
# q - число под ln
# a - число a

Nmax = int(input('Ввод максимального количества итераций: '))
eps = float(input('Ввод эпсилон: '))
x = float(input('Ввод значения n: '))
step = float(input('Ввод шага вывода: '))
q = float(input('Число под Ln: '))
a = float(input('Число a: '))
from math import *
print()
N = 1
p = 0
e = '\u2502'
f = '\u2500'
h1 = a**x * log(q)**x/factorial(x)
S = h1
print('\u250c', f*8,'\u252c', f*15,'\u252c', f*15,'\u252c',
      f*15,'\u2510', sep='')
print(e, '  N\t', e, '\tx\t', e, '\ttekh1\t', e, '\tS\t', e)
while abs(h1) > eps and N < Nmax:
    if N%step == 1 or step == 1:
        print('\u251c', f*8,'\u253c', f*15,'\u253c', f*15,'\u253c',
              f*15,'\u2524', sep='')
        if len(str(h1)) > 8 and len(str(S)) > 8:
            print(e, N, '\t', e, ' {:2.2f}'.format(x), '\t', e,
              ' {:2.2e}'.format(h1), '\t', e,' {:2.2e}'.format(S), '\t',e)
        elif len(str(S)) > 9:
            print(e, N, '\t', e, ' {:2.2f}'.format(x), '\t', e,
              ' {:2.3f}'.format(h1), '\t', e,' {:2.2e}'.format(S), '\t',e)
        elif len(str(h1)) > 9:
             print(e, N, '\t', e, ' {:2.2f}'.format(x), '\t', e,
              ' {:2.2e}'.format(h1), '\t', e,' {:2.3f}'.format(S), '\t',e)
        else:
            print(e, N, '\t', e, ' {:2.2f}'.format(x), '\t', e,
              ' {:2.3f}'.format(h1), '\t', e,' {:2.3f}'.format(S), '\t',e)
    N+=1
    h1 *= a**step * log(q)**step / (factorial(x) / factorial(x - step))
    S += h1
    if abs(h1) <= eps:
        p = 1
if N%step == 1 or step == 1:
        print('\u251c', f*8,'\u253c', f*15,'\u253c', f*15,'\u253c',
              f*15,'\u2524', sep='')
        if len(str(h1)) > 10 and len(str(S)) > 9:
            print(e, N, '\t', e, ' {:2.2f}'.format(x), '\t', e,
              ' {:2.2e}'.format(h1), '\t', e,' {:2.2e}'.format(S), '\t',e)
        elif len(str(S)) > 9:
            print(e, N, '\t', e, ' {:2.2f}'.format(x), '\t', e,
              ' {:2.3f}'.format(h1), '\t', e,' {:2.2e}'.format(S), '\t',e)
        elif len(str(h1)) > 9:
             print(e, N, '\t', e, ' {:2.2f}'.format(x), '\t', e,
              ' {:2.2e}'.format(h1), '\t', e,' {:2.3f}'.format(S), '\t',e)
        else:
            print(e, N, '\t', e, ' {:2.2f}'.format(x), '\t', e,
              ' {:2.5f}'.format(h1), '\t', e,' {:2.3f}'.format(S), '\t',e)
print('\u2514', f*8,'\u2534', f*15,'\u2534', f*15,'\u2534',
          f*15,'\u2518', sep='')
if p == 1:
    print ('Ряд сошёлся. Номер итерации: ',N,' Сумма равна: ',S)
else:
    print ('Ряд не сошёлся.')
