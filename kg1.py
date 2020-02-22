from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import math


def draw(event):
    global f_lst, r_lst, scale, dx, dy, redraw_scale, redraw_d

    a = []
    b = []
    aa = f_lst.get(0, END)
    for x in aa:
        a.append(list(x))
    bb = r_lst.get(0, END)
    for x in bb:
        b.append(list(x))

    if a is None or b is None:
        showerror('Ошибка', 'Введите точки в формате х,у')
        return
    cnv.delete('all')

    if len(a) > 2 and len(b) > 2:
        cir1, cir2, angle, dots_a, dots_b = calc(a, b)
        if cir1 is None:
            showwarning('Упс', "Окружностей не найдено!")
        else:
            if redraw_d is False:
                dx = 50
                dy = 50
                redraw_d = True
            if distance_between_points(cir1[0], cir2[0]) <= 10 and redraw_scale is False:
                scale = 30
                redraw_scale = True

            layout()

            cnv.create_oval((cir1[0][0] - cir1[1]) * scale + dx, (cir1[0][1] + cir1[1]) * scale + dy,
                            (cir1[0][0] + cir1[1]) * scale + dx, (cir1[0][1] - cir1[1]) * scale + dy, outline = "red")

            cnv.create_oval((cir2[0][0] - cir2[1]) * scale + dx, (cir2[0][1] + cir2[1]) * scale + dy,
                            (cir2[0][0] + cir2[1]) * scale + dx, (cir2[0][1] - cir2[1]) * scale + dy, outline = "green")

            cnv.create_oval((cir1[0][0]) * scale + dx - 1.5, (cir1[0][1]) * scale + dy - 1.5,
                            (cir1[0][0]) * scale + dx + 1.5,
                            (cir1[0][1]) * scale + dy + 1.5, fill = "red")

            cnv.create_oval((cir2[0][0]) * scale + dx - 1.5, (cir2[0][1]) * scale + dy - 1.5,
                            (cir2[0][0]) * scale + dx + 1.5,
                            (cir2[0][1]) * scale + dy + 1.5, fill = "green")

            cnv.create_line(cir1[0][0] * scale + dx, cir1[0][1] * scale + dy, cir2[0][0] * scale + dx, cir2[0][1] * scale + dy)

            for i in range(len(dots_a)):
                cnv.create_oval(dots_a[i][0] * scale + dx - 1.5, (dots_a[i][1]) * scale + dy - 1.5,
                                dots_a[i][0] * scale + dx + 1.5,
                                (dots_a[i][1]) * scale + dy + 1.5, fill="red")
                cnv.create_text(dots_a[i][0] * scale + dx - 1.5, dots_a[i][1] * scale + dy - 7,
                                text="({0:.2f}; {1:.2f})".format(dots_a[i][0], dots_a[i][1]), fill="red",
                                font="Times 7")
            for i in range(len(dots_b)):
                cnv.create_oval((dots_b[i][0]) * scale + dx - 1.5, (dots_b[i][1]) * scale + dy - 1.5,
                                (dots_b[i][0]) * scale + dx + 1.5,
                                (dots_b[i][1]) * scale + dy + 1.5, fill="green")
                cnv.create_text(dots_b[i][0] * scale + dx - 1.5, dots_b[i][1] * scale + dy - 7,
                                text="({0:.2f}; {1:.2f})".format(dots_b[i][0], dots_b[i][1]), fill="green",
                                font="Times 7")

            tx.delete('1.0', END)
            tx.insert(1.0, "Окружности найдены.\n"
                           "Окружность 1: координаты центра ({0:.2f}, {1:.2f})\n"
                           "Окружность 2: координаты центра ({2:.2f}, {3:.2f})\n"
                           "Минимальный угол между осью ординат и прямой, "
                           "соединяющей центры окружностей: {4:.2f}".format(cir1[0][0], cir1[0][1], cir2[0][0],
                                                                            cir2[0][1], angle))

    elif len(a) < 3 and len(b) < 3:
        showwarning('Упс', "Недостаточно точек!")

    elif len(a) < 3:
        showwarning('Упс', "Недостаточно точек, чтобы построить первую окружность!")

    elif len(b) < 3:
        showwarning('Упс', "Недостаточно точек, чтобы построить вторую окружность!")


def layout():
    cnv.create_line(dx, dy, dx, 10 * scale + dy, width = 1, arrow = LAST)
    cnv.create_text(dx, 10 * scale + dy + 6, text = 'Y', font = "Times 12")
    cnv.create_line(dx, dy, 10 * scale + dx, dy, width = 1, arrow = LAST)
    cnv.create_text(10 * scale + dx + 3, dy, text = 'X', font = "Times 12")
    cnv.create_text(dx - 10, dy - 10, text = '0', font = "Times 12")
    for i in range (1, 11, 1):
        cnv.create_text(dx - 10 + i * scale, dy - 10, text = '{0}'.format(i), font = "Times 12")

    for i in range (1, 11, 1):
        cnv.create_text(dx - 12, dy - 10 + i * scale, text = '{0}'.format(i), font = "Times 12")


def redraw_max(event):
    global scale, cnv
    scale += 1
    cnv.delete('all')
    draw(event)


def redraw_min(event):
    global scale, cnv
    if scale > 0:
        scale -= 1
    cnv.delete('all')
    draw(event)


def to_right(event):
    global dx, cnv
    dx += 10
    cnv.delete('all')
    draw(event)


def to_left(event):
    global dx, cnv
    dx -= 10
    cnv.delete('all')
    draw(event)


def to_top(event):
    global dy, cnv
    dy -= 10
    cnv.delete('all')
    draw(event)


def to_bottom(event):
    global dy, cnv
    dy += 10
    cnv.delete('all')
    draw(event)


def str_to_float(a):
    if a == '':
        return None
    a = a.split(' ')
    for i in range(len(a)):
        try:
            a[i] = float(a[i])
        except ValueError:
            showwarning('Упс', "Уберите лишние пробелы или добавьте еще одну координату!")
            return None
    return a


def distance_between_points(xy1, xy2):
    x_1 = xy1[0]
    x_2 = xy2[0]
    y_1 = xy1[1]
    y_2 = xy2[1]
    dis = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    return dis


def calc(a, b):
    global scale
    circle1 = None
    circle2 = None
    min_angle = 91
    min_used_dots_a = None
    min_used_dots_b = None

    for i in range(len(a) - 2):
        for j in range(i + 1, len(a) - 1):
            for k in range(j + 1, len(a)):
                res = find_cir(a[i], a[j], a[k])

                if res is None:
                    continue
                else:
                    centre_a = res[0]
                    rad_a = res[1]

                for l in range(len(b) - 2):
                    for m in range(l + 1, len(b) - 1):
                        for n in range(m + 1, len(b)):
                            res = find_cir(b[l], b[m], b[n])

                            if res is None:
                                continue
                            else:
                                centre_b = res[0]
                                rad_b = res[1]

                            if distance_between_points([centre_a[0], centre_a[1]], [centre_b[0], centre_b[1]]) == 0:
                                continue
                            else:
                                cos_angle = abs((centre_a[1] - centre_b[1])/distance_between_points([centre_a[0], centre_a[1]], [centre_b[0], centre_b[1]]))
                                cos_angle = int(math.acos(cos_angle) * 180 / math.pi)

                                if cos_angle < min_angle:
                                    min_angle = cos_angle
                                    circle1 = [centre_a, rad_a]
                                    circle2 = [centre_b, rad_b]
                                    min_used_dots_a = [a[i], a[j], a[k]]
                                    min_used_dots_b = [b[l], b[m], b[n]]

    return circle1, circle2, min_angle, min_used_dots_a, min_used_dots_b


def find_cir(p1, p2, p3):  # поиск окружности по трем точкам
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    if x1 == x2 == x3:  # три точки лежат на одной прямой
        return None
    if x2 == x1:  # случай, когда одна хорда вертикальная, ее коэф = int
        x2, x3 = x3, x2
        y2, y3 = y3, y2
    elif x2 == x3:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    ma = (y2 - y1) / (x2 - x1)  # наклонный коэф 1-ой хорды
    mb = (y3 - y2) / (x3 - x2)  # накл коэф 2-ой хорды
    if ma != mb:  # прямые совпадают
        x_centre = (ma * mb * (y1 - y3) + mb * (x1 + x2) - ma * (x2 + x3)) / (2 * (mb - ma))
        if ma == 0:
            y_centre = (-1 / mb) * (x_centre - (x2 + x3) / 2) + ((y2 + y3) / 2)
        else:
            y_centre = (-1 / ma) * (x_centre - (x1 + x2) / 2) + ((y1 + y2) / 2)
        radius = distance_between_points([x_centre, y_centre], [x1, y1])
        return [[x_centre, y_centre], radius]
    else:
        return None


def quit_win(event):
    root.destroy()
    navigation.destroy()
    r.destroy()


def insert_lst_f(event):
    global f_lst, ent_f
    p = ent_f.get()
    p = str_to_float(p)
    if p is None:
        return
    if len(p) != 2:
        showwarning('Упс', "У точки должно быть всего две координаты!")
        return
    aa = f_lst.get(0, END)
    for i in aa:
        n = list(i)
        if n[0] == p[0] and n[1] == p[1]:
            showwarning('Упс', "Точка уже введена!")
            return
    f_lst.insert(END, p)
    ent_f.delete(0, END)


def insert_lst_s(event):
    global r_lst, ent_s
    p = ent_s.get()
    p = str_to_float(p)
    if p is None:
        return
    if len(p) != 2:
        showwarning('Упс', "У точки должно быть всего две координаты!")
        return
    aa = r_lst.get(0, END)
    for i in aa:
        n = list(i)
        if n[0] == p[0] and n[1] == p[1]:
            showwarning('Упс', "Точка уже введена!")
            return
    r_lst.insert(END, p)
    ent_s.delete(0, END)


def del_point_red(event):
    global f_lst
    f_lst.delete(ACTIVE)


def del_point_green(event):
    global r_lst
    r_lst.delete(ACTIVE)


def ch_point_red(event):
    global f_lst
    p = ent_f.get()
    p = str_to_float(p)
    if p is None:
        return
    if len(p) > 2 or len(p) < 2:
        showwarning('Упс', "У точки должно быть всего две координаты!")
        return
    index = f_lst.curselection()
    f_lst.delete(ACTIVE)
    f_lst.insert(index, p)
    ent_f.delete(0, END)


def ch_point_green(event):
    global r_lst
    p = ent_s.get()
    p = str_to_float(p)
    if p is None:
        return
    if len(p) > 2 or len(p) < 2:
        showwarning('Упс', "У точки должно быть всего две координаты!")
        return
    index = r_lst.curselection()
    r_lst.delete(ACTIVE)
    r_lst.insert(index, p)
    ent_s.delete(0, END)

def clear_boxes(event):
    global f_lst
    global r_lst
    while f_lst.size() != 0:
        f_lst.delete(0)

    while r_lst.size() != 0:
        r_lst.delete(0)


root = Tk()
root.title("Поле точек")
r = Tk()
r.title("Инструменты")
navigation = Tk()
navigation.title("Навигация")
root.resizable(width=False, height=False)
r.resizable(width=False, height=False)
navigation.resizable(width=False, height=False)
root.geometry('700x600')
r.wm_geometry("+%d+%d" % (10, 10))
root.wm_geometry("+%d+%d" % (650, 10))
navigation.wm_geometry("+%d+%d" % (150, 400))

scale = 9
dx = 10
dy = 10
redraw_scale = False
redraw_d = False
scale_p = ttk.Button(navigation)
scale_p['text'] = "Увеличить"
scale_m = ttk.Button(navigation)
scale_m['text'] = 'Уменьшить'
right = ttk.Button(navigation)
right['text'] = '〉'
left = ttk.Button(navigation)
left['text'] = '〈'
bottom = ttk.Button(navigation)
bottom['text'] = '﹀'
top = ttk.Button(navigation)
top['text'] = '︿'

scrollbar1 = Scrollbar(r)
scrollbar2 = Scrollbar(r)
f_lst = Listbox(r, selectmode = SINGLE, height = 10, yscrollcommand = scrollbar1.set)
r_lst = Listbox(r, selectmode = SINGLE, height = 10, yscrollcommand = scrollbar2.set)
scrollbar1.config(command = f_lst.yview)
scrollbar2.config(command = r_lst.yview)
lab_f = Label(r, text = 'Красное можество точек', font = "Times 12")
lab_s = Label(r, text = 'Зеленое можество точек', font = "Times 12")
xy_f = Label(r, text = 'Введите красную точку  ', font = "Times 12")
xy_s = Label(r, text = 'Введите зеленую точку  ', font = "Times 12")
ent_f = Entry(r, width = 50, bd = 3)
ent_s = Entry(r, width = 50, bd = 3)

but_del_r = ttk.Button(r)
but_del_r['text'] = 'Удалить красную точку'
but_del_g = ttk.Button(r)
but_del_g['text'] = 'Удалить зеленую точку'
but_ch_r = ttk.Button(r)
but_ch_r['text'] = 'Изменить красную точку'
but_ch_g = ttk.Button(r)
but_ch_g['text'] = 'Изменить зеленую точку'
but_answ = ttk.Button(r)
but_answ['text'] = 'Отобразить ответ'
but_clear = ttk.Button(r)
but_clear['text'] = 'Очистить точки'
but_exit = ttk.Button(r)
but_exit['text'] = 'Выход'

ent_f.bind('<Return>', insert_lst_f)
ent_s.bind('<Return>', insert_lst_s)
but_del_r.bind('<Button-1>', del_point_red)
but_del_g.bind('<Button-1>', del_point_green)
but_ch_r.bind('<Button-1>', ch_point_red)
but_ch_g.bind('<Button-1>', ch_point_green)
but_clear.bind('<Button-1>', clear_boxes)

cnv = Canvas(root, height = 600, width = 700, bg = 'white')
tx = Text(root, width = 700, height = 4, font = 'Times 12')

but_answ.bind("<Button-1>", draw)
scale_p.bind('<Button-1>', redraw_max)
scale_m.bind('<Button-1>', redraw_min)
right.bind('<Button-1>', to_right)
left.bind('<Button-1>', to_left)
top.bind('<Button-1>', to_top)
bottom.bind('<Button-1>', to_bottom)
but_exit.bind('<Button-1>', quit_win)

f_lst.grid(row = 1, column = 0, padx = 10)
r_lst.grid(row = 1, column = 1, padx = 10)
lab_f.grid(row = 0, column = 0, padx = 5)
lab_s.grid(row = 0, column = 1, padx = 5)
xy_f.grid(row = 2, column = 0, pady = 5)
ent_f.grid(row = 2, column = 1, pady = 5)
xy_s.grid(row = 3, column = 0, pady = 5)
ent_s.grid(row = 3, column = 1, pady = 5)

but_del_r.grid(row = 4, column = 0, padx = 2, pady = 5)
but_del_g.grid(row = 5, column = 0, padx = 2, pady = 5)
but_answ.grid(row = 4, column = 2, padx = 2, pady = 5)
but_exit.grid(row = 5, column = 2, padx = 2, pady = 5)
but_ch_r.grid(row = 4, column = 1, padx = 2, pady = 5)
but_ch_g.grid(row = 5, column = 1, padx = 2, pady = 5)
but_clear.grid(row = 1, column = 2)

tx.pack()
cnv.pack()

scale_p.grid(row = 0, column = 0, padx = 20)
scale_m.grid(row = 1, column = 0, padx = 20, pady = 5)
right.grid(row = 0, column = 1, padx = 20)
left.grid(row = 1, column = 1, padx = 20, pady = 5)
top.grid(row = 0, column = 2, padx = 20)
bottom.grid(row = 1, column = 2, padx = 20, pady = 5)

r.mainloop()
root.mainloop()
navigation.mainloop()