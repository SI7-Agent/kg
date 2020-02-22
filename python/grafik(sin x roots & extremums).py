# Автор: ст-т гр. ИУ7-25Б Руднев К.
# Программа для нахождения корней ф-ции и точек экстремума

from numpy import *
import matplotlib.pyplot as plt
import math
import pylab
from pylab import *
from scipy.optimize import *
from matplotlib import mlab
from tkinter import messagebox
from tkinter import *
from math import *
from sympy import *

root = Tk()
root.title('Рисовалка графиков')
root.resizable(width = 'false', height = 'false')
root.geometry('500x500')
# Объявление окна

lbl_intro = Label(text = 'Нахождение/уточнение корней функции f(x) = sin(x)', font = 'Times, 15')
lbl_intro.place(x = 10, y = 10)

lbl_h = Label(text = 'Введите шаг интервалов:')
lbl_h.place(x = 30, y = 50)

lbl_get_h = Entry()
lbl_get_h.place(x = 300, y = 50)

lbl_a = Label(text = 'Введите левый край отрезка:')
lbl_a.place(x = 30, y = 80)

start_dia = Entry()
start_dia.place(x = 300, y = 80)

lbl_b = Label(text = 'Введите правый край отрезка:')
lbl_b.place(x = 30, y = 110)

end_dia = Entry()
end_dia.place(x = 300, y = 110)

lbl_e = Label(text = 'Введите точность eps:')
lbl_e.place(x = 30, y = 140)

eps = Entry()
eps.place(x = 300, y = 140)

lbl_it = Label(text = 'Введите максимальное число итераций:')
lbl_it.place(x = 30, y = 170)

it = Entry()
it.place(x = 300, y = 170)

count_btn = Button(command = lambda: start_graf(lbl_get_h.get(), start_dia.get(),
            end_dia.get(), eps.get(), f, f1, it.get()), width = 15,
                   text = 'Построить график')
count_btn.place(x = 230, y = 230)
# Элементы интерфейса

num_lbl = Label(text = '№')
num_lbl.place(x = 10, y = 280)

inter_lbl = Label(text = 'Интервал')
inter_lbl.place(x = 35, y = 280)

root_equal_lbl = Label(text = 'x')
root_equal_lbl.place(x = 180, y = 280)

func_equal_lbl = Label(text = 'f(x)')
func_equal_lbl.place(x = 290, y = 280)

it_num_lbl = Label(text = 'Количество \nитераций')
it_num_lbl.place(x = 350, y = 280)

error_lbl = Label(text = 'Код \nошибки')
error_lbl.place(x = 420, y = 280)
# Интерактивные элементы интерфейса

def info():
    messagebox.showinfo('Информация о кодах',
                        '1 - корень найден, но не удается уточнить его '
                        'до заданного eps за Ваше кол-во итераций'
                        '\n2 - корень найден за границами интервала')
# Ф-ция для вывода меню кодов

menu = Menu(root)
menu1 = (menu)
menu1.add_command(label = 'Информация о кодах', command = info)
root.config(menu = menu)

# ListBoxes
def scroll(*args):
    list1.yview(*args)
    list2.yview(*args)
    list3.yview(*args)
    list4.yview(*args)
    list5.yview(*args)
    list6.yview(*args)

enter = Frame(root)

scrl = Scrollbar(enter, orient = VERTICAL, command = scroll)

list1 = Listbox(enter, height = 10, width = 3, yscrollcommand = scrl.set)
list1.pack(side = 'left')

list2 = Listbox(enter, height = 10, width = 12, yscrollcommand = scrl.set)
list2.pack(side = 'left')

list3 = Listbox(enter, height = 10, width = 24, yscrollcommand = scrl.set)
list3.pack(side = 'left')

list4 = Listbox(enter, height = 10, width = 16, yscrollcommand = scrl.set)
list4.pack(side = 'left')

list5 = Listbox(enter, height = 10, width = 9, yscrollcommand = scrl.set)
list5.pack(side = 'left')

list6 = Listbox(enter, height = 10, width = 9, yscrollcommand = scrl.set)
list6.pack(side = 'left')

scrl.pack(side = 'left', fill=Y)
enter.place(x = 10, y = 320)

#_____________________________

def all_root(a, b, eps, f, f1, f2, it, l5):
    i = 0
    if f(a) == 0:
        a1 = tuple((a, 1))
        return a1

    elif f(b) == 0:
        b1 = tuple((b, 1))
        return b1

    elif f(a)*f(b)>0:
        if f(a)*f2(a)>=0:
            x0 = a

        else:
            x0 = b

        xn = 0
        x00 = 0

        if float(f1(x0)) == 0:
            x0 = eps

        else:
            xn = float(x0)-float(f(x0))/float(f1(x0))
            x00 = xn

        while abs(x0 - xn) > float(eps) and i < 101:
            x0 = float(xn)
            xn = float(x0) - float(f(x0))/float(f1(x00))
            i += 1

        if a <= xn <= b:
            if i >= it:
                a1 = tuple(('error1', 'f'))
                return a1

            elif a > xn or b < xn:
                a1 = tuple(('error2', 'f'))
                return a1

            else:
                a1 = tuple((xn, i))
                return a1

        else:
            a1 = tuple(('error3', 'f'))
            return a1
    else:
        i = 0
        if f(a)*f2(a)>=0:
            x0 = a

        else:
            x0 = b

        xn = 0
        x00 = 0

        if float(f1(x0)) == 0:
            x0 = eps

        else:
            xn = float(x0)-float(f(x0))/float(f1(x0))
            x00 = xn

        while abs(x0 - xn) > float(eps) and i < it+1:
            x0 = float(xn)
            xn = float(x0) - float(f(x0))/float(f1(x00))
            i += 1

        if i >= it:
            a1 = tuple(('error1', 'f'))
            return a1

        elif a > xn or b < xn:
            a1 = tuple(('error2', 'f'))
            return a1

        else:
            a1 = tuple((xn, i))
            return a1
# Ф-ция нахождения корня

start_btn = Button(command = lambda: count(lbl_get_h.get(),
                start_dia.get(), end_dia.get(),
                eps.get(), f, f1, f2, list1, list2, list3,
                list4, list5, list6, it.get()), width = 15, text = 'Найти корни')
start_btn.place(x = 100, y = 230)
# Кнопка для расчитывания корней

def count(h, a, b, eps, f, f1, f2, l1, l2, l3, l4, l5, l6, it):
    l1.delete(0, END)
    l2.delete(0, END)
    l3.delete(0, END)
    l4.delete(0, END)
    l5.delete(0, END)
    l6.delete(0, END)

    try:
        h = float(h)

    except:
        messagebox.showerror('', 'Ошибка в задании шага')
        return 0

    try:
        a = float(a)
        b = float(b)

        if a > b:
            messagebox.showerror('', 'Ошибка в задании интервала')
            return 0

    except:
        messagebox.showerror('', 'Ошибка в задании интервала')
        return 0

    try:
        eps = float(eps)

        if eps > 1:
            messagebox.showerror('', 'Ошибка в задании eps')
            return 0

    except:
        messagebox.showerror('', 'Ошибка в задании eps')
        return 0

    try:
        it = int(it)

        if it <= 0:
            messagebox.showerror('', 'Ошибка в задании числа итераций')
            return 0

    except:
        messagebox.showerror('', 'Ошибка в задании числа итераций')
        return 0

    h, a, b, eps = map(float, (h, a, b, eps))
    i = 0

    if a*b > 0:
        i = abs(int((abs(b) - abs(a))/h))

    elif a*b <= 0:
        i = int((abs(b) + abs(a))/h)
    count = 1
    left = a
    right = left + h
    mas = []

    for j in range(i):
        interval = '[ ' + str('{:.1f}'.format(left)) + ' ; ' + str('{:.1f}'.format(right)) + ' ]'

        a1 = all_root(left, right, eps, f, f1, f2, it, l5)

        if a1[0] == 'error1':
             l1.insert(END, count)
             l2.insert(END, str(interval))
             l3.insert(END, '----')
             l4.insert(END, '----')
             l5.insert(END, '----')
             l6.insert(END, '1')
             count += 1

        elif a1[0] == 'error2':
            l1.insert(END, count)
            l2.insert(END, str(interval))
            l3.insert(END, '----')
            l4.insert(END, '----')
            l5.insert(END, '----')
            l6.insert(END, '2')
            count += 1

        elif a1[0] == 'error3':
            pass

        else:
            xn = a1[0]

            if xn not in mas:
                mas.append(xn)
                y = f(xn)

                if xn == 0.0:
                    y = 0
                l1.insert(END, count)
                l2.insert(END, str(interval))
                l3.insert(END, '{:.5f}'.format(xn))
                l4.insert(END, '{:.0e}'.format(y))
                l5.insert(END, str(a1[1]))
                l6.insert(END, '')
                count += 1
        left = right
        right = left + h

    if b - h < left < b:
        right = b
        interval = '[ ' + str('{:.1f}'.format(left)) + ' ; ' + str('{:.1f}'.format(right)) + ' ]'

        a1 = all_root(left, right, eps, f, f1, f2, it, l5)

        if a1[0] == 'error1':
            l1.insert(END, count)
            l2.insert(END, str(interval))
            l3.insert(END, '----')
            l4.insert(END, '----')
            l5.insert(END, '----')
            l6.insert(END, '1')
            count += 1

        elif a1[0] == 'error2':
            l1.insert(END, count)
            l2.insert(END, str(interval))
            l3.insert(END, '----')
            l4.insert(END, '----')
            l5.insert(END, '----')
            l6.insert(END, '2')
            count += 1

        elif a1[0] == 'error3':
            pass

        else:
            xn = a1[0]

            if xn not in mas:
                mas.append(xn)
                y = f(xn)

                if xn == 0.0:
                    y = 0
                l1.insert(END, count)
                l2.insert(END, str(interval))
                l3.insert(END, '{:.5f}'.format(xn))
                l4.insert(END, '{:.0e}'.format(y))
                l5.insert(END, str(a1[1]))
                l6.insert(END, '')
# Ф-ция для заполнения таблицы

def all_root_list(a, b, f, f1, f2):
    if f(a)*f(b) > 0:
        pass

    else:
        if f(a) == 0:
            return a

        elif f(b) == 0:
            return b

        else:
            if f(a) * f2(a) > 0:
                x0 = a

            else:
                x0 = b
            xn = float(x0) - float(f(x0)) / float(f1(x0))

            while abs(x0 - xn) > float(0.01):
                x0 = float(xn)
                xn = float(x0) - float(f(x0)) / float(f1(x0))
                return xn

def get_list(a, b, f, f1, f2):
    a, b = map(float, (a, b))
    list = []
    i = 0

    if a * b > 0:
        i = abs(int(abs(b) - abs(a)))

    elif a * b <= 0:
        i = int(abs(b) + abs(a))

    left = a
    right = left + 1

    for j in range(i):
        x = all_root_list(left, right, f, f1, f2)
        list.append(x)
        left = right
        right = left + 1
    return list
# Ф-ции для нахождения точек графика

def f(x):
    return sin(x)

def f1(x):
    return cos(x)

def f2(x):
    return -sin(x)
# Сама ф-ция, которую анализируем

def start_graf(h, num1, num2, eps, f, f1, it):
    try:
        h = float(h)

    except:
        messagebox.showerror('', 'Ошибка в задании шага')
        return 0

    try:
        num1 = float(num1)
        num2 = float(num2)

        if num1 > num2:
            messagebox.showerror('', 'Ошибка в задании интервала')
            return 0

    except:
        messagebox.showerror('', 'Ошибка в задании интервала')
        return 0

    try:
        eps = float(eps)

        if eps > 1:
            messagebox.showerror('', 'Ошибка в задании eps')
            return 0

    except:
        messagebox.showerror('', 'Ошибка в задании eps')
        return 0

    try:
        it = int(it)

        if it <= 0:
            messagebox.showerror('', 'Ошибка в задании числа итераций')
            return 0

    except:
        messagebox.showerror('', 'Ошибка в задании числа итераций')
        return 0

    xmin = float(num1)
    xmax = float(num2)

    list1 = get_list(num1, num2, f, f1, f2)
    list1y = [0 for i in range(len(list1))]

    def f3(x):
        return -cos(x)

    list2 = get_list(num1, num2, f1, f2, f3)
    list2y = []

    for i in range(len(list2)):
        try:
            float(list2[i])
            list2y.append(f(list2[i]))

        except:
            list2y.append(None)
            continue

    pylab.plot(list2, list2y, 'go')

    pylab.plot(list1, list1y, 'ro')

    xlist = arange(xmin, xmax, 0.01)
    ylist = [f(x) for x in xlist]

    pylab.plot(xlist, ylist)
    pylab.legend(('extremums', 'zeros', 'f(x)'))
    plt.grid(True)
    pylab.show()

    plt.title('grafik f(x)')
    plt.grid(True, linestyle='-', color='0.75')
# Постройка графика

root.mainloop()
# Конец