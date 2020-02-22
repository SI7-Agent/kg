#метод парабол
def f(x):
    return x*x

def parabol(f, a, b, n):
    s = 0
    h = (b - a) / n
    for i in range(n):
        s += f(a + i * h) + 4 * f(a + i * h + h / 2) + f(a + i * h + h)
    s *= h / 6
    return s

a = float(input('Один край: '))
b = float(input('Второй край: '))
n = int(input('Кол-во участков: '))

i = parabol(f,a,b,n)
print(i)