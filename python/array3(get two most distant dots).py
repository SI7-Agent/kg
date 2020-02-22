b = int(input('Введите кол-во точек: '))
q = [0]*b
e = [0]*b

for i in range(b):
    q[i] = float(input('x: '))
    e[i] = float(input('y: '))

from math import sqrt
def len(x1, y1, x2, y2):
        a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return a
minN1 = 0
minN2 = 1
minL = len(q[0], e[0], q[1], e[1])
maxN1 = 0
maxN2 = 1
maxL = minL
for n1 in range(b):
    for n2 in range(n1, b):
        L = len(q[n1], e[n1], q[n2], e[n2])
        if L < minL:
            minN1 = n1
            minN2 = n2
            minL = L
        elif L > maxL:
            maxN1 = n1
            maxN2 = n2
            maxL = L
print('Две самые удалённые точки: ', 'x1 = ', q[maxN1], ', y1 = ', e[maxN1], ' & x2 = ', q[maxN2], ', y2 = ', e[maxN2], sep = '')