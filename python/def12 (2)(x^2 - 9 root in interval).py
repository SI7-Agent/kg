from math import *

def f(x):
    return x**2 - 9

a = float(input("Левый край интервала: "))
b = float(input("Правый край интервала: "))
eps = float(input("Eps: "))
c = a
d = b

while (abs(b-a) > eps):
    if f(b) - f(a) == 0:
        a, b = b, a - f(a) * (b - a) / (eps)
    else:
        a, b = b, a - f(a) * (b - a) / (f(b) - f(a))

print("{:7s}".format("a"), "{:7s}".format("b"), "{:7s}".format("eps"), "{:7s}".format("x"))
if c > b or b > d:
    print("{:.2f}".format(c), "{:7.2f}".format(d), "{:7.0e}".format(eps), "  Корня нет/корень за границей интервала")
else:
    print("{:.2f}".format(c), "{:7.2f}".format(d), "{:7.0e}".format(eps), "{:8.4f}".format(b))