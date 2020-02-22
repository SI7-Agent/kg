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
        #cnv.delete("all")
        choice = algorythm.get()
        cnv.configure(bg = bg_color)

        if choice == options[0]:
            canon([100, 100], 5)
        elif choice == options[1]:
            parametr([100, 100], 5)
        elif choice == options[2]:
            brez([x1[0], y1[0]], [x2[0], y2[0]])
        elif choice == options[3]:
            sred_point([100, 100], 5)
        elif choice == options[4]:
            cnv.create_oval(x1[0], y1[0], x2[0], y2[0], fill = line_color)
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

def canon(pc, radius):
    pass

def parametr(pc, radius):
    pass

def sred_point(pc, radius):
    pass

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

    if angle != None and radius != None:
        cnv.delete("all")
        choice = algorythm.get()
        cnv.configure(bg = bg_color)

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
root.geometry('1110x655')
root.wm_geometry("+%d+%d" % (0, 0))
root.grid_rowconfigure(14, weight = 1)
root.grid_columnconfigure(15, weight = 1)

line_color = '#000000'
bg_color = '#ffffff'

cnv = Canvas(root, height = 650, width = 700, bg = 'white')
cnv.grid(rowspan = 14, columnspan = 12, column = 0, row = 0, sticky = "snw")

options = ["Каноническое уравнение",
           "Параметрическое уравнение",
           "Брезенхем",
           "Алгоритм средней точки",
           "Библиотечный алгоритм"]
algorythm = ttk.Combobox(root, values = options, width = 30, state = "readonly")
algorythm.set(options[0])
algorythm.grid(column = 13, row = 0, columnspan = 3, rowspan = 1, padx = 20, sticky = "we")

lbl_xc = Label(root, text = 'X центра:')
lbl_xc.grid(column = 13, row = 0, columnspan = 1, sticky = 'we', rowspan = 3, padx = 20)
#
ent_xc = Spinbox(root, width = 26, from_ = 0, to = 700)
ent_xc.grid(column = 13, row = 1, sticky = 'we', rowspan = 2, padx = 20)
#
lbl_yc = Label(root, text = 'Y центра:')
lbl_yc.grid(column = 14, row = 0, columnspan = 1, sticky = 'we', rowspan = 3, padx = 20)
#
ent_yc = Entry(root, width = 15)
ent_yc.grid(column = 14, row = 1, sticky = 'we', rowspan = 2, padx = 25)

lbl_radius = Label(root, text = 'Радиус окружности:')
lbl_radius.grid(column = 13, row = 2, columnspan = 1, sticky = 'we', rowspan = 2, padx = 20)
#
ent_radius = Entry(root, width = 26)
ent_radius.grid(column = 13, row = 2, columnspan = 1, sticky = 'we', rowspan = 3, padx = 20)
#
lbl_axis_a = Label(root, text = 'Горизонт. полуось  эллипса:')
lbl_axis_a.grid(column = 14, row = 2, columnspan = 1, sticky = 'we', rowspan = 2, padx = 20)
#
ent_axis_a = Entry(root, width = 26)
ent_axis_a.grid(column = 14, row = 2, columnspan = 1, sticky = 'we', rowspan = 3, padx = 20)
#
lbl_axis_a = Label(root, text = 'Вертик. полуось эллипса:')
lbl_axis_a.grid(column = 14, row = 3, columnspan = 1, sticky = 'we', rowspan = 2, padx = 20)
#
ent_axis_a = Entry(root, width = 26)
ent_axis_a.grid(column = 14, row = 3, columnspan = 1, sticky = 'we', rowspan = 3, padx = 20)

btn_color = Button(root, text = 'Выбрать цвет\nокружности/эллипса', command = lambda: choice_color_line("<1>"))
btn_color.grid(column = 13, row = 4, columnspan = 1, sticky = 'we', rowspan = 3, padx = 20)
#
lbl_color = Label(root, bg = line_color, width = 15)
lbl_color.grid(column = 14, row = 4, columnspan = 1, rowspan = 3, padx = 14)
#
btn_bg_color = Button(root, text = 'Выбрать цвет фона', command = lambda: choice_color_bg("<1>"))
btn_bg_color.grid(column = 13, row = 5, columnspan = 1, sticky = 'we', rowspan = 3, padx = 20)
#
lbl_bg_color = Label(root, bg = bg_color, width = 15)
lbl_bg_color.grid(column = 14, row = 5, columnspan = 1, rowspan = 3, padx = 20)
#
btn_do_job_circle = Button(root, text = 'Построить окружность', command = lambda: printf("<1>"))
btn_do_job_circle.grid(column = 13, row = 7, columnspan = 2, sticky = 'we', rowspan = 1, padx = 20)
#
btn_do_job_ellipse = Button(root, text = 'Построить эллипс', command = lambda: printf("<1>"))
btn_do_job_ellipse.grid(column = 13, row = 7, columnspan = 2, sticky = 'we', rowspan = 3, padx = 20)
#
lbl_diametr = Label(root, text = 'Мин. радиус окружности:')
lbl_diametr.grid(column = 13, row = 8, columnspan = 1, sticky = 'we', rowspan = 3, padx = 14, pady = 5)

ent_diametr = Entry(root)
ent_diametr.grid(column = 13, row = 9, columnspan = 1, sticky = 'we', rowspan = 2, padx = 14)

lbl_step = Label(root, text = 'Шаг изменения радиуса:')
lbl_step.grid(column = 13, row = 9, columnspan = 1, sticky = 'we', rowspan = 3, padx = 14, pady = 5)

ent_step = Entry(root)
ent_step.grid(column = 13, row = 10, columnspan = 1, sticky = 'we', rowspan = 2, padx = 14)

lbl_max = Label(root, text = 'Кол-во окружностей:')
lbl_max.grid(column = 13, row = 10, columnspan = 1, sticky = 'we', rowspan = 3, padx = 14, pady = 5)


#for ellipse
lbl_diametr_a = Label(root, text = 'Мин. ось а:')
lbl_diametr_a.grid(column = 14, row = 8, columnspan = 10, sticky = 'we', rowspan = 3, padx = 1, pady = 5)

lbl_diametr_b = Label(root, text = 'Мин. ось b:')
lbl_diametr_b.grid(column = 15, row = 8, columnspan = 2, sticky = 'we', rowspan = 3, padx = 10, pady = 5)

lbl_step = Label(root, text = 'Шаг изменения радиуса:')
lbl_step.grid(column = 14, row = 9, columnspan = 1, sticky = 'we', rowspan = 3, padx = 14, pady = 5)

lbl_max = Label(root, text = 'Кол-во эллипсов:')
lbl_max.grid(column = 14, row = 9, columnspan = 1, sticky = 'we', rowspan = 4, padx = 14, pady = 5)
#for ellipse


#
# ent_angle = Entry(root)
# ent_angle.grid(column = 15, row = 9, columnspan = 1, sticky = 'we', rowspan = 1, padx = 14)
#
btn_do_sun = Button(root, text = 'Графический анализ', command = lambda: analize())
btn_do_sun.grid(column = 13, row = 12, columnspan = 2, sticky = 'we', rowspan = 1, padx = 14)

btn_clear = Button(root, text = 'Очистить холст', command = lambda: clear_cnv("<1>"))
btn_clear.grid(column = 13, row = 12, columnspan = 2, sticky = 'we', rowspan = 3, padx = 14)

btn_quit = Button(root, text = 'Выйти', command = lambda: quit("<1>"))
btn_quit.grid(column = 13, row = 13, columnspan = 2, sticky = 'we', rowspan = 1, padx = 14)

root.mainloop()