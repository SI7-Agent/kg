from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import math

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

def draw(event):
    global dx, dy, cir, hyp, shtr

    cnv.delete("all")
    for i in range(0, dots_for_cir - 1, 1):
        cnv.create_line(cir[i][0], cir[i][1], cir[i + 1][0], cir[i + 1][1])
    cnv.create_line(cir[-2][0], cir[-2][1], cir[0][0], cir[0][1])

    for i in range(1, dots_for_hyp, 1):
        cnv.create_line(hyp[i - 1][0], hyp[i - 1][1], hyp[i][0], hyp[i][1])

    for i in range(0, len(shtr), 1):
        cnv.create_line(shtr[i][0][0], shtr[i][0][1], shtr[i][1][0], shtr[i][1][1])

    cnv.create_oval(cir[-1][0], cir[-1][1], cir[-1][0] + 1, cir[-1][1] + 1, width = 2)

def rotate(event):
    global status, dx, dy, scale_count_x, scale_count_y, angle, shtr

    a = fld_x_rotate.get()
    a = str_to_float(a)
    b = fld_y_rotate.get()
    b = str_to_float(b)
    c = fld_angle_rotate.get()
    c = str_to_float(c)

    if a != None and b != None and c != None:
        scale_count_x = 1
        scale_count_y = 1
        angle = 2 * math.pi + math.radians(c[0])

        for i in range(0, dots_for_cir + 1, 1):
            x1_orig = cir[i][0]
            y1_orig = cir[i][1]

            cir[i][0] = a[0] + (x1_orig - a[0]) * math.cos(math.radians(c[0])) + (y1_orig - b[0]) * math.sin(math.radians(c[0]))
            cir[i][1] = b[0] - (x1_orig - a[0]) * math.sin(math.radians(c[0])) + (y1_orig - b[0]) * math.cos(math.radians(c[0]))

        for i in range(0, dots_for_hyp, 1):
            x2_orig = hyp[i][0]
            y2_orig = hyp[i][1]

            hyp[i][0] = a[0] + (x2_orig - a[0]) * math.cos(math.radians(c[0])) + (y2_orig - b[0]) * math.sin(math.radians(c[0]))
            hyp[i][1] = b[0] - (x2_orig - a[0]) * math.sin(math.radians(c[0])) + (y2_orig - b[0]) * math.cos(math.radians(c[0]))

        for i in range(0, len(shtr), 1):
            x2_orig = shtr[i][0][0]
            y2_orig = shtr[i][0][1]
            x3_orig = shtr[i][1][0]
            y3_orig = shtr[i][1][1]

            shtr[i][0][0] = a[0] + (x2_orig - a[0]) * math.cos(math.radians(c[0])) + (y2_orig - b[0]) * math.sin(math.radians(c[0]))
            shtr[i][0][1] = b[0] - (x2_orig - a[0]) * math.sin(math.radians(c[0])) + (y2_orig - b[0]) * math.cos(math.radians(c[0]))
            shtr[i][1][0] = a[0] + (x3_orig - a[0]) * math.cos(math.radians(c[0])) + (y3_orig - b[0]) * math.sin(math.radians(c[0]))
            shtr[i][1][1] = b[0] - (x3_orig - a[0]) * math.sin(math.radians(c[0])) + (y3_orig - b[0]) * math.cos(math.radians(c[0]))
    else:
        showerror("Ошибка", "Поля параметров не заданы или заданы неверно")
        return

    status.append([0, 0, scale_count_x, scale_count_y, angle, [a[0], b[0]]])
    draw(event)

def scale(event):
    global dx, dy, status, cir, scale_count_y, scale_count_x, hyp, shtr

    a = fld_x_scale.get()
    a = str_to_float(a)
    b = fld_y_scale.get()
    b = str_to_float(b)
    c = fld_time_x_scale.get()
    c = str_to_float(c)
    d = fld_time_y_scale.get()
    d = str_to_float(d)

    copy_cir = []
    copy_hyp = []
    copy_shtr = []

    if a != None and b != None and c != None and d != None:
        scale_count_x = c[0]
        scale_count_y = d[0]
        angle = 2 * math.pi

        if scale_count_x == 0 or scale_count_y == 0:
            for i in range(0, len(cir), 1):
                copy_cir.append([cir[i][0], cir[i][1]])
            for i in range(0, len(hyp), 1):
                copy_hyp.append([hyp[i][0], hyp[i][1]])
            for i in range(0, len(shtr), 1):
                copy_shtr.append([[shtr[i][0][0], shtr[i][0][1]], [shtr[i][1][0], shtr[i][1][1]]])

        for i in range(0, dots_for_cir + 1, 1):
            cir[i][0] = scale_count_x * cir[i][0] + (1 - scale_count_x) * a[0]
            cir[i][1] = scale_count_y * cir[i][1] + (1 - scale_count_y) * b[0]

        for i in range(0, dots_for_hyp, 1):
            hyp[i][0] = scale_count_x * hyp[i][0] + (1 - scale_count_x) * a[0]
            hyp[i][1] = scale_count_y * hyp[i][1] + (1 - scale_count_y) * b[0]

        for i in range(0, len(shtr), 1):
            shtr[i][0][0] = scale_count_x * shtr[i][0][0] + (1 - scale_count_x) * a[0]
            shtr[i][0][1] = scale_count_y * shtr[i][0][1] + (1 - scale_count_y) * b[0]
            shtr[i][1][0] = scale_count_x * shtr[i][1][0] + (1 - scale_count_x) * a[0]
            shtr[i][1][1] = scale_count_y * shtr[i][1][1] + (1 - scale_count_y) * b[0]
    else:
        showerror("Ошибка", "Поля параметров не заданы или заданы неверно")
        return

    if copy_cir != []:
        status.append([0, 0, scale_count_x, scale_count_y, angle, [a[0], b[0]], [copy_cir, copy_hyp, copy_shtr]])
    else:
        status.append([0, 0, scale_count_x, scale_count_y, angle, [a[0], b[0]]])
    draw(event)

def move(event):
    global dx, dy, status, cir, scale_count_y, scale_count_x, cir, hyp, shtr

    a = fld_x_move.get()
    a = str_to_float(a)
    b = fld_y_move.get()
    b = str_to_float(b)

    if a != None and b != None:
        scale_count_x = 1
        scale_count_y = 1
        angle = 2 * math.pi

        for i in range(0, dots_for_cir + 1, 1):
            cir[i][0] += a[0]
            cir[i][1] += b[0]

        for i in range(0, dots_for_hyp, 1):
            hyp[i][0] += a[0]
            hyp[i][1] += b[0]

        for i in range(0, len(shtr), 1):
            shtr[i][0][0] += a[0]
            shtr[i][0][1] += b[0]

            shtr[i][1][0] += a[0]
            shtr[i][1][1] += b[0]
    else:
        showerror("Ошибка", "Поля параметров не заданы или заданы неверно")
        return

    status.append([a[0], b[0], scale_count_x, scale_count_y, angle, "flag"])
    draw(event)

def restore(event):
    global scale_count_x, scale_count_y, status, angle, cir, hyp, shtr

    if len(status) > 1:
        dx = status[-1][0]
        dy = status[-1][1]

        scale_count_x = status[-1][2]
        scale_count_y = status[-1][3]
        angle = status[-1][4]

        if len(status[-1]) < 7:
            try:
                if scale_count_x != 0 and scale_count_y != 0:
                    for i in range(0, dots_for_cir + 1, 1):
                        cir[i][0] -= dx
                        cir[i][1] -= dy

                    for i in range(0, dots_for_hyp, 1):
                        hyp[i][0] -= dx
                        hyp[i][1] -= dy

                    for i in range(0, len(shtr), 1):
                        shtr[i][0][0] -= dx
                        shtr[i][0][1] -= dy

                        shtr[i][1][0] -= dx
                        shtr[i][1][1] -= dy

                    for i in range(0, dots_for_cir + 1, 1):
                        if scale_count_x != 1 or scale_count_y != 1:
                            cir[i][0] = 1 / scale_count_x * cir[i][0] + (1 - 1 / scale_count_x) * status[-1][5][0]
                            cir[i][1] = 1 / scale_count_y * cir[i][1] + (1 - 1 / scale_count_y) * status[-1][5][1]

                        x1_orig = cir[i][0]
                        y1_orig = cir[i][1]

                        cir[i][0] = status[-2][5][0] + (x1_orig - status[-2][5][0]) * math.cos(2 * math.pi - angle) + (y1_orig - status[-2][5][1]) * math.sin(2 * math.pi - angle)
                        cir[i][1] = status[-2][5][1] - (x1_orig - status[-2][5][0]) * math.sin(2 * math.pi - angle) + (y1_orig - status[-2][5][1]) * math.cos(2 * math.pi - angle)

                    for i in range(0, dots_for_hyp, 1):
                        if scale_count_x != 1 or scale_count_y != 1:
                            hyp[i][0] = 1 / scale_count_x * hyp[i][0] + (1 - 1 / scale_count_x) * status[-1][5][0]
                            hyp[i][1] = 1 / scale_count_y * hyp[i][1] + (1 - 1 / scale_count_y) * status[-1][5][1]

                        x2_orig = hyp[i][0]
                        y2_orig = hyp[i][1]

                        hyp[i][0] = status[-2][5][0] + (x2_orig - status[-2][5][0]) * math.cos(2 * math.pi - angle) + (y2_orig - status[-2][5][1]) * math.sin(2 * math.pi - angle)
                        hyp[i][1] = status[-2][5][1] - (x2_orig - status[-2][5][0]) * math.sin(2 * math.pi - angle) + (y2_orig - status[-2][5][1]) * math.cos(2 * math.pi - angle)

                    for i in range(0, len(shtr), 1):
                        if scale_count_x != 1 or scale_count_y != 1:
                            shtr[i][0][0] = 1 / scale_count_x * shtr[i][0][0] + (1 - 1 / scale_count_x) * status[-1][5][0]
                            shtr[i][0][1] = 1 / scale_count_y * shtr[i][0][1] + (1 - 1 / scale_count_y) * status[-1][5][1]
                            shtr[i][1][0] = 1 / scale_count_x * shtr[i][1][0] + (1 - 1 / scale_count_x) * status[-1][5][0]
                            shtr[i][1][1] = 1 / scale_count_y * shtr[i][1][1] + (1 - 1 / scale_count_y) * status[-1][5][1]

                        x2_orig = shtr[i][0][0]
                        y2_orig = shtr[i][0][1]
                        x3_orig = shtr[i][1][0]
                        y3_orig = shtr[i][1][1]

                        shtr[i][0][0] = status[-2][5][0] + (x2_orig - status[-2][5][0]) * math.cos(2 * math.pi - angle) + (y2_orig - status[-2][5][1]) * math.sin(2 * math.pi - angle)
                        shtr[i][0][1] = status[-2][5][1] - (x2_orig - status[-2][5][0]) * math.sin(2 * math.pi - angle) + (y2_orig - status[-2][5][1]) * math.cos(2 * math.pi - angle)
                        shtr[i][1][0] = status[-2][5][0] + (x3_orig - status[-2][5][0]) * math.cos(2 * math.pi - angle) + (y3_orig - status[-2][5][1]) * math.sin(2 * math.pi - angle)
                        shtr[i][1][1] = status[-2][5][1] - (x3_orig - status[-2][5][0]) * math.sin(2 * math.pi - angle) + (y3_orig - status[-2][5][1]) * math.cos(2 * math.pi - angle)
            except:
                if status[-2][5] != "flag":
                    cir.clear()
                    hyp.clear()
                    shtr.clear()

                    cir = [par_cir(i * 2 * math.pi / dots_for_cir) for i in range(0, dots_for_cir, 1)]
                    cir.append([(x2 + x1) / 2, (y2 + y1) / 2])

                    hyp = [hyperbola(i / 2) for i in range(5, dots_for_hyp + 5, 1)]
                    shtr = get_shtrix()
        else:
            cir = status[-1][6][0]
            hyp = status[-1][6][1]
            shtr = status[-1][6][2]

        status.pop()
        draw(event)
    else:
        showwarning("Внимание", "Достигнуто начальное положение")

def info(event):
    showinfo("Справка", "Для поворота введите координаты точки, относительно которой производится поворот. А также угол (в градусах), на который следует повернуть\n\n"
                        "Для масштабирования введите координаты центра масштабирования. А также коэффициент масштабирования по обеим осям\n\n"
                        "Для переноса введите величину смещения по обеим осям\n\n"
                        "\nПримечание: все преобразования производятся с текущим изображением")

def quit(event):
    try:
        root.destroy()
        r.destroy()
    except:
        r.destroy()

root = Tk()
root.title("Отображение")
r = Tk()
r.title("Инструменты")
r.rowconfigure(14)
r.columnconfigure(5)
root.resizable(width = False, height = False)
r.resizable(width = False, height = False)
root.geometry('700x700')
r.wm_geometry("+%d+%d" % (10, 10))
root.wm_geometry("+%d+%d" % (650, 10))

dx = 0
dy = 0
x1 = 250
y1 = 250
x2 = 450
y2 = 450
angle = 2 * math.pi
radius = abs(x2 - x1)/2
const_hyp = -500
dots_for_cir = 700
dots_for_hyp = 301

def par_cir(t):
    global x1, x2, y1, y2, radius
    x = radius * math.cos(t) + (x2 + x1)/2
    y = radius * math.sin(t) + (y2 + y1)/2
    return [x, y]

cir = [par_cir(i * 2 * math.pi / dots_for_cir) for i in range (0, dots_for_cir, 1)]
cir.append([(x2 + x1)/2, (y2 + y1)/2])

def hyperbola(x):
    global const_hyp, x1, x2, y1, y2
    x3 = x + (x1 + x2) / 2
    y3 = const_hyp / x + (y1 + y2) / 2
    return [x3, y3]

hyp = [hyperbola(i / 2) for i in range (5, dots_for_hyp + 5, 1)]

scale_count_x = 1
scale_count_y = 1
status = [[dx, dy, scale_count_x, scale_count_y, angle, [None, None]]]

cnv = Canvas(root, height = 700, width = 700, bg = 'white')

def get_shtrix():
    global cnv, cir, hyp, x1, y1, x2, y2, radius

    pts = []
    pts_tmp = []

    for i in range(0, len(hyp), 1):
        circle_hyp_point = ((hyp[i][0] - (x2 + x1) / 2) ** 2 + (hyp[i][1] - (y2 + y1) / 2) ** 2)

        if circle_hyp_point < radius ** 2:
            y_test = -(math.sqrt(radius ** 2 - (hyp[i][0] - (x2 + x1) / 2) ** 2)) + (y2 + y1) / 2
            coord_beg = [hyp[i][0], y_test]

            x = coord_beg[0]
            try:
                y_test = const_hyp / (x - (x1 + x2) / 2) + (y1 + y2) / 2
            except ZeroDivisionError:
                y_test = (y1 + y2) / 2
            coord_end = [x, y_test]

            pts_tmp.append([coord_beg, coord_end])

    for i in range(0, len(pts_tmp), 20):
        pts.append(pts_tmp[i])

    return pts

shtr = get_shtrix()
draw("<1>")
cnv.pack()

txt_x_rotate = ttk.Label(r, text = "X")
txt_x_rotate.grid(row = 0, column = 0, sticky = "e")
txt_y_rotate = ttk.Label(r, text = "Y")
txt_y_rotate.grid(row = 0, column = 3, sticky = "e")
fld_x_rotate = ttk.Entry(r)
fld_x_rotate.grid(row = 0, column = 1, sticky = "w")
fld_y_rotate = ttk.Entry(r)
fld_y_rotate.grid(row = 0, column = 4, sticky = "w")
txt_angle_rotate = ttk.Label(r, text = "Угол поворота (градусы)")
txt_angle_rotate.grid(row = 1, column = 0, sticky = "e", columnspan = 2)
fld_angle_rotate = ttk.Entry(r)
fld_angle_rotate.grid(row = 1, column = 3)
btn_rotate = ttk.Button(r, text = "Повернуть")
btn_rotate.grid(sticky = "we", columnspan = 5, row = 2)
btn_rotate.bind("<1>", rotate)

clr1 = ttk.Label(r, text = "")
clr1.grid(sticky = "we", columnspan = 3, row = 3)

txt_x_scale = ttk.Label(r, text = "Xc")
txt_x_scale.grid(row = 4, column = 0, sticky = "e")
txt_y_scale = ttk.Label(r, text = "Yc")
txt_y_scale.grid(row = 4, column = 3, sticky = "e")
fld_x_scale = ttk.Entry(r)
fld_x_scale.grid(row = 4, column = 1, sticky = "w")
fld_y_scale = ttk.Entry(r)
fld_y_scale.grid(row = 4, column = 4, sticky = "w")
txt_time_x_scale = ttk.Label(r, text = "kX")
txt_time_x_scale.grid(row = 5, column = 0, sticky = "e")
txt_time_y_scale = ttk.Label(r, text = "kY")
txt_time_y_scale.grid(row = 5, column = 3, sticky = "e")
fld_time_x_scale = ttk.Entry(r)
fld_time_x_scale.grid(row = 5, column = 1, sticky = "w")
fld_time_y_scale = ttk.Entry(r)
fld_time_y_scale.grid(row = 5, column = 4, sticky = "w")
btn_scale = ttk.Button(r, text = "Масштабировать")
btn_scale.grid(sticky = "we", columnspan = 5, row = 6)
btn_scale.bind("<1>", scale)

clr2 = ttk.Label(r, text = "")
clr2.grid(sticky = "we", columnspan = 3, row = 7)

txt_x_move = ttk.Label(r, text = "dX")
txt_x_move.grid(row = 8, column = 0, sticky = "e")
txt_y_move = ttk.Label(r, text = "dY")
txt_y_move.grid(row = 8, column = 3, sticky = "e")
fld_x_move = ttk.Entry(r)
fld_x_move.grid(row = 8, column = 1, sticky = "w")
fld_y_move = ttk.Entry(r)
fld_y_move.grid(row = 8, column = 4, sticky = "w")
btn_move = ttk.Button(r, text = "Перенести")
btn_move.grid(sticky = "we", columnspan = 5, row = 9)
btn_move.bind("<1>", move)

clr3 = ttk.Label(r, text = "")
clr3.grid(sticky = "we", columnspan = 3, row = 10)

btn_restore = ttk.Button(r, text = "Восстановить предыдущую конфигурацию")
btn_restore.grid(sticky = "we", columnspan = 5)
btn_restore.bind("<1>", restore)
btn_info = ttk.Button(r, text = "Инфо")
btn_info.grid(sticky = "we", columnspan = 5)
btn_info.bind("<1>", info)
btn_exit = ttk.Button(r, text = "Выход")
btn_exit.grid(sticky = "we", columnspan = 5)
btn_exit.bind("<1>", quit)

cnv.create_line(350, 350, 351, 351)

root.mainloop()
r.mainloop()