from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.colorchooser import *
from math import *

def str_to_float(a):
    if a == '':
        return None
    a = a.split(' ')
    while "" in a:
        a.remove("")
    for i in range(len(a)):
        try:
            a[i] = float(a[i])
        except ValueError:
            return None
    if (len(a) > 1):
        return None
    return a

def printf(event):
    global algorythm, cnv, ent_x1, ent_x2, ent_y1, ent_y2

    x1 = ent_x1.get()
    x1 = str_to_float(x1)
    y1 = ent_y1.get()
    y1 = str_to_float(y1)
    x2 = ent_x2.get()
    x2 = str_to_float(x2)
    y2 = ent_y2.get()
    y2 = str_to_float(y2)

    if x1 != None and y1 != None and x2 != None and y2 != None:
        choice = algorythm.get()
        cnv.configure(bg = bg_color)

        if choice == options[0]:
            DDA([x1[0], y1[0]], [x2[0], y2[0]])
        elif choice == options[1]:
            brez_int([x1[0], y1[0]], [x2[0], y2[0]])
        elif choice == options[2]:
            brez([x1[0], y1[0]], [x2[0], y2[0]])
        elif choice == options[3]:
            brez_stair([x1[0], y1[0]], [x2[0], y2[0]])
        elif choice == options[4]:
            wu([x1[0], y1[0]], [x2[0], y2[0]])
        elif choice == options[5]:
            cnv.create_line(x1[0], y1[0], x2[0], y2[0], fill = line_color)
    else:
        showerror("Error", "Координаты отрезка не заданы или заданы неверно")

def get_intens(color, intens):
    grad = []
    (r1, g1, b1) = cnv.winfo_rgb(color)
    (r2, g2, b2) = cnv.winfo_rgb(bg_color)

    r_rat = float(r2 - r1) / intens
    g_rat = float(g2 - g1) / intens
    b_rat = float(b2 - b1) / intens

    for i in range (intens):
        nr = int(r1 + (r_rat * i))
        ng = int(g1 + (g_rat * i))
        nb = int(b1 + (b_rat * i))
        grad.append("#%4.4x%4.4x%4.4x" % (nr, ng, nb))

    grad.reverse()
    return grad

def sign(x):
    if x == 0:
        return 0
    else:
        return x / abs(x)

def DDA(p1, p2):
    if p1 == p2:
        draw_point(p1[0], p1[1], line_color)
        return

    dX = abs(p1[0] - p2[0])
    dY = abs(p1[1] - p2[1])

    length = max(dX, dY)

    dX = (p2[0] - p1[0]) / length
    dY = (p2[1] - p1[1]) / length

    x = p1[0]
    y = p1[1]

    while length > 1:
        draw_point(x, y, line_color)
        x += dX
        y += dY
        length -= 1

def brez(p1, p2):
    if p1 == p2:
        draw_point(p1[0], p1[1], line_color)
        return

    x = p1[0]
    y = p1[1]
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    sx = sign(dx)
    sy = sign(dy)

    dx = abs(dx)
    dy = abs(dy)

    change = False

    if dy > dx:
        dx, dy = dy, dx
        change = True

    m = dy / dx
    e = m - 0.5

    i = 1
    while i <= dx:
        draw_point(x, y, line_color)

        if e >= 0:
            if change is False:
                y += sy
            else:
                x += sx
            e -= 1

        if e < 0:
            if change is False:
                x += sx
            else:
                y += sy
            e += m

        i += 1

def brez_int(p1, p2):
    if p1 == p2:
        draw_point(p1[0], p1[1], line_color)
        return

    x = p1[0]
    y = p1[1]
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    sx = sign(dx)
    sy = sign(dy)

    dx = abs(dx)
    dy = abs(dy)

    change = False

    if dy > dx:
        dx, dy = dy, dx
        change = True

    e = 2 * dy - dx

    i = 1
    while i <= dx:
        draw_point(x, y, line_color)

        if e >= 0:
            if change is False:
                y += sy
            else:
                x += sx
            e -= 2 * dx

        if e < 0:
            if change is False:
                x += sx
            else:
                y += sy
            e += 2 * dy

        i += 1

def brez_stair(p1, p2):
    if p1 == p2:
        draw_point(p1[0], p1[1], line_color)
        return

    x = p1[0]
    y = p1[1]
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)

    try:
        m = dy / dx
    except ZeroDivisionError:
        m = 0

    isBlack = False

    if line_color == "#000000":
        i_max = 256
        isBlack = True
    else:
        isBlack = True
        i_max = 256

    change = False

    if dy > dx:
        dx, dy = dy, dx
        change = True
        if m:
            m = 1 / m

    m *= i_max
    e = i_max / 2
    w = i_max - m

    i = 1
    while i <= dx:
        new_color = line_color
        grad_mas = get_intens(new_color, 256)

        if not isBlack:
            new_color = grad_mas[100 + int(e)]
            draw_point(x, y, new_color)
        else:
            new_color = grad_mas[255 - int(e)]
            draw_point(x, y, new_color)

        if e <= w:
            if change:
                y += sy
            else:
                x += sx
            e += m
        else:
            x += sx
            y += sy
            e -= w

        i += 1

def clev_line_wu(step, x, y, n):
    colors = get_intens(line_color, 100)
    if step == 1:
        x, y = y, x
    N = int(n * 100)
    if N > 99:
        N = 99
    cnv.create_line(x, y, x + 1, (y + 1), fill = colors[N])

def wu(p1, p2):
    xys = [int(round(p1[0])), int(round(p1[1]))]
    xye = [int(round(p2[0])), int(round(p2[1]))]

    step = abs(xye[1] - xys[1]) > abs(xye[0] - xys[0])

    if step:
        xys[0], xys[1] = xys[1], xys[0]
        xye[0], xye[1] = xye[1], xye[0]

    if xys[0] > xye[0]:
        xys[0], xye[0] = xye[0], xys[0]
        xye[1], xys[1] = xys[1], xye[1]

    clev_line_wu(step, xys[0], xys[1], 1)
    clev_line_wu(step, xye[0], xye[1], 1)

    dx = xye[0] - xys[0]
    dy = xye[1] - xys[1]

    grad = dy / dx

    y = xys[1] + grad
    x = xys[0] + 1

    while (x <= xye[0] - 1):
        clev_line_wu(step, x, int(y), 1 - (y - int(y)))
        clev_line_wu(step, x, int(y) + 1, y - int(y))

        y += grad
        x += 1

def choice_color_line(event):
    global line_color

    color0 = askcolor()
    color0 = color0[1]
    line_color = color0
    lbl_color.configure(bg = line_color)

def choice_color_bg(event):
    global bg_color

    color0 = askcolor()
    color0 = color0[1]
    bg_color = color0
    cnv.configure(bg=bg_color)
    lbl_bg_color.configure(bg = bg_color)

def draw_point(x, y, color):
    global cnv

    cnv.create_line(x, y, x + 1, y + 1, fill = color)

def clear_cnv(event):
    global cnv

    cnv.delete("all")

def quit(event):
    root.destroy()

def analize():
    global algorythm, cnv, ent_angle, ent_diametr

    radius = ent_diametr.get()
    radius = str_to_float(radius)
    angle = ent_angle.get()
    angle = str_to_float(angle)

    if angle != None and radius != None and angle[0] != 0.0:
        choice = algorythm.get()

        bx = 350
        by = 300

        for i in range(0, 360, int(angle[0])):
            ex = cos(radians(i)) * radius[0] + bx
            ey = sin(radians(i)) * radius[0] + by

            if choice == options[0]:
                DDA([bx, by], [ex, ey])
            elif choice == options[1]:
                brez_int([bx, by], [ex, ey])
            elif choice == options[2]:
                brez([bx, by], [ex, ey])
            elif choice == options[3]:
                brez_stair([bx, by], [ex, ey])
            elif choice == options[4]:
                wu([bx, by], [ex, ey])
            elif choice == options[5]:
                cnv.create_line(bx, by, ex, ey, fill = line_color)
    else:
        showerror("Error", "Параметры графического анализа не заданы или заданы неверно")

root = Tk()
root.title("Отображение")
root.resizable(width = False, height = False)
root.geometry('1030x605')
root.wm_geometry("+%d+%d" % (10, 10))
root.rowconfigure(14)
root.columnconfigure(14)

line_color = '#000000'
bg_color = '#ffffff'

cnv = Canvas(root, height = 600, width = 700, bg = 'white')
cnv.grid(rowspan = 14, columnspan = 12, column = 0, row = 0)

options = ["ЦДА",
           "Брезенхем для целых чисел",
           "Брезенхем для действительных чисел",
           "Брезенхем с устранением ступенчатости",
           "Ву",
           "Библиотечный алгоритм"]
algorythm = ttk.Combobox(root, values = options, width = 40, state = "readonly")
algorythm.set(options[0])
algorythm.grid(column = 14, row = 0, columnspan = 2, sticky = 'we', rowspan = 2, padx = 14)

lbl_x1 = Label(root, text = 'X начала:')
lbl_x1.grid(column = 14, row = 1, columnspan = 1, sticky = 'we', rowspan = 2, padx = 14)

ent_x1 = Spinbox(root, from_ = 0, to = 700)#Entry(root)
ent_x1.grid(column = 14, row = 2, columnspan = 1, sticky = 'we', rowspan = 1, padx = 14)

lbl_y1 = Label(root, text = 'Y начала:')
lbl_y1.grid(column = 15, row = 1, columnspan = 1, sticky = 'we', rowspan = 2, padx = 14)

ent_y1 = Spinbox(root, from_ = 0, to = 700)#Entry(root)
ent_y1.grid(column = 15, row = 2, columnspan = 1, sticky = 'we', rowspan = 1, padx = 14)

lbl_x2 = Label(root, text = 'X конца:')
lbl_x2.grid(column = 14, row = 2, columnspan = 1, sticky = 'we', rowspan = 2, padx = 14, pady = 15)

ent_x2 = Spinbox(root, from_ = 0, to = 700)#Entry(root)
ent_x2.grid(column = 14, row = 3, columnspan = 1, sticky = 'we', rowspan = 1, padx = 14)

lbl_y2 = Label(root, text = 'Y конца:')
lbl_y2.grid(column = 15, row = 2, columnspan = 1, sticky = 'we', rowspan = 2, padx = 14, pady = 5)

ent_y2 = Spinbox(root, from_ = 0, to = 700)#Entry(root)
ent_y2.grid(column = 15, row = 3, columnspan = 1, sticky = 'we', rowspan = 1, padx = 14)

btn_color = Button(root, text = 'Выбрать цвет отрезка', command = lambda: choice_color_line("<1>"))
btn_color.grid(column = 14, row = 4, columnspan = 1, sticky = 'we', rowspan = 2, padx = 14)

lbl_color = Label(root, bg = line_color, width = 15)
lbl_color.grid(column = 15, row = 4, columnspan = 1, rowspan = 2, padx = 14)

btn_bg_color = Button(root, text = 'Выбрать цвет фона', command = lambda: choice_color_bg("<1>"))
btn_bg_color.grid(column = 14, row = 5, columnspan = 1, sticky = 'we', rowspan = 2, padx = 14)

lbl_bg_color = Label(root, bg = bg_color, width = 15)
lbl_bg_color.grid(column = 15, row = 5, columnspan = 1, rowspan = 2, padx = 14)

btn_do_job = Button(root, text = 'Построить отрезок', command = lambda: printf("<1>"))
btn_do_job.grid(column = 14, row = 6, columnspan = 2, sticky = 'we', rowspan = 2, padx = 14)

lbl_diametr = Label(root, text = 'Длина луча:')
lbl_diametr.grid(column = 14, row = 7, columnspan = 1, sticky = 'we', rowspan = 2, padx = 14, pady = 5)

ent_diametr = Spinbox(root, from_ = 0, to = 350)#Entry(root)
ent_diametr.grid(column = 14, row = 8, columnspan = 1, sticky = 'we', rowspan = 1, padx = 14)

lbl_angle = Label(root, text = 'Угол между лучами:')
lbl_angle.grid(column = 15, row = 7, columnspan = 1, sticky = 'we', rowspan = 2, padx = 14, pady = 5)

ent_angle = Spinbox(root, from_ = 1, to = 360)#Entry(root)
ent_angle.grid(column = 15, row = 8, columnspan = 1, sticky = 'we', rowspan = 1, padx = 14)

btn_do_sun = Button(root, text = 'Графический анализ', command = lambda: analize())
btn_do_sun.grid(column = 14, row = 9, columnspan = 2, sticky = 'we', rowspan = 2, padx = 14)

btn_clear = Button(root, text = 'Очистить холст', command = lambda: clear_cnv("<1>"))
btn_clear.grid(column = 14, row = 10, columnspan = 2, sticky = 'we', rowspan = 2, padx = 14)

btn_quit = Button(root, text = 'Выйти', command = lambda: quit("<1>"))
btn_quit.grid(column = 14, row = 11, columnspan = 2, sticky = 'we', rowspan = 2, padx = 14)

root.mainloop()