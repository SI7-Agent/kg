print('Найти объём и полную площадь поверхности правильной четырехугольной усеченной пирамиды.')
a = input('Введите длину нижнего основания: ')
# ввод длины нижнего ребра
def is_digit(a):
    if a.isdigit():
       return True
    else:
        try: 
            float(a) 
            return True 
        except ValueError: 
            return False
if is_digit(a) == True:
    a = float(a)
else:
    while is_digit(a) == False:
        a = input('Введите правильную длину нижнего основания: ')
while float(a) == 0:
    a = input('Введите правильную длину нижнего основания: ')
while float(a) < 0:
    a = input('Введите правильную длину нижнего основания: ')
a = float(a)
b = input('Введите длину верхнего основания: ')
# ввод длины верхнего ребра
def is_digit(b):
    if b.isdigit():
       return True
    else:
        try: 
            float(b) 
            return True 
        except ValueError: 
            return False
if is_digit(b) == True:
    b = float(b)
else:
    while is_digit(b) == False:
        b = input('Введите правильную длину верхнего ребра: ')
while float(b) == 0:
    b = input('Введите правильную длину нижнего основания: ')
while float(b) < 0:
    b = input('Введите правильную длину нижнего основания: ')
b = float(b)
h = input('Введите длину высоты: ')
# ввод длины высоты
def is_digit(h):
    if h.isdigit():
       return True
    else:
        try: 
            float(h) 
            return True 
        except ValueError: 
            return False
if is_digit(h) == True:
    h = float(h)
else:
    while is_digit(h) == False or float(h) < 0 or float(h) == 0:
        h = input('Введите правильную длину высоты: ')
h = float(h)
while float(h) == 0:
    h = input('Введите правильную длину нижнего основания: ')
while float(h) < 0:
    h = input('Введите правильную длину нижнего основания: ')
h = float(h)
from math import sqrt
# загрузка модуля извлечения корня
s1 = a**2
# вычисление площади нижнего основания
s2 = b**2
# вычисление площади верхнего основания
v = h/3*(s1+s2+sqrt(s1*s2))
# вычисление объёма
k = b/a
# вычисление коэффициента подобия оснований
h1 = k*h
#вычисление восстановленной высоты
a1 = a/2
# вычисление оставшегося катета
l1 = sqrt(h1**2+a1**2)
# вычисление востановленной апофемы
l = float(l1)/k
#вычисление апофемы
s3 = 2*l*(a+b)
# вычисление боковой поверхности пирамиды
print('*********************************************')
print('Полная площадь пирамиды:', ' ', round(s1+s2+s3, 4), sep='')
print('*********************************************')
print('Объём пирамиды:', ' ', round(v, 4), sep='')
print('*********************************************')
# вывод нужной информации
input('Нажмите Enter для выхода')