from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPen, QPainter, QColor, QBrush, QImage, QPixmap, QRgba64, QPalette
from PyQt5.QtCore import Qt
from math import sqrt, pi, sin, cos
import time
import pylab
import matplotlib.pyplot as plt
import matplotlib.lines as lines
from PyQt5.QtWidgets import QMessageBox
#import ui


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window2.ui", self)
        self.setWindowTitle("Рисование окружностей/эллипсов")
        self.scene = QtWidgets.QGraphicsScene(0, 0, 541, 561)
        self.cnv_view.setScene(self.scene)
        self.image = QImage(541, 561, QImage.Format_ARGB32_Premultiplied)
        self.pen = QPen()
        self.line_color = QColor(Qt.black)
        self.bg_color = QColor(Qt.white)

        self.btn_get_circle.clicked.connect(lambda: draw_circle(self))
        self.btn_get_ellipse.clicked.connect(lambda: draw_ellipse(self))
        self.btn_get_circle_spectre.clicked.connect(lambda: analize_circle(self))
        self.btn_get_ellipse_spectre.clicked.connect(lambda: analize_ellipse(self))

        self.btn_bg_color.clicked.connect(lambda: get_bg_color(self))
        self.btn_line_color.clicked.connect(lambda: get_line_color(self))
        self.btn_analisis.clicked.connect(lambda: analize_radius_circle(self))
        self.btn_delete.clicked.connect(lambda: clear_all(self))
        self.btn_exit.clicked.connect(lambda: quit())

    def update(self):
        pix = QPixmap(541, 561)
        pix.convertFromImage(self.image)
        self.scene.addPixmap(pix)

def sign(x):
    if x != 0:
        return abs(x)/x
    else:
        return 0

def canon_circle(win, x, y, radius):
    for i in range (0, int(radius) + 1, 1):
        y_new = round(sqrt(radius ** 2 - i ** 2))
        win.image.setPixel(x + i, y + y_new, win.pen.color().rgb())
        win.image.setPixel(x + i, y - y_new, win.pen.color().rgb())
        win.image.setPixel(x - i, y + y_new, win.pen.color().rgb())
        win.image.setPixel(x - i, y - y_new, win.pen.color().rgb())

    for i in range (0, int(radius) + 1, 1):
        x_new = round(sqrt(radius ** 2 - i ** 2))
        win.image.setPixel(x + x_new, y + i, win.pen.color().rgb())
        win.image.setPixel(x + x_new, y - i, win.pen.color().rgb())
        win.image.setPixel(x - x_new, y + i, win.pen.color().rgb())
        win.image.setPixel(x - x_new, y - i, win.pen.color().rgb())

def canon_ellipse(win, x, y, a, b):
    for i in range (0, int(a) + 1, 1):
        y_new = round(b * sqrt(1 - (i ** 2 / a ** 2)))
        win.image.setPixel(x + i, y + y_new, win.pen.color().rgb())
        win.image.setPixel(x + i, y - y_new, win.pen.color().rgb())
        win.image.setPixel(x - i, y + y_new, win.pen.color().rgb())
        win.image.setPixel(x - i, y - y_new, win.pen.color().rgb())

    for i in range (0, int(b) + 1, 1):
        x_new = round(a * sqrt(1 - (i ** 2 / b ** 2)))
        win.image.setPixel(x + x_new, y + i, win.pen.color().rgb())
        win.image.setPixel(x + x_new, y - i, win.pen.color().rgb())
        win.image.setPixel(x - x_new, y + i, win.pen.color().rgb())
        win.image.setPixel(x - x_new, y - i, win.pen.color().rgb())

def param_circle(win, x, y, radius):
    len = round(pi * radius / 2)
    for i in range (0, len + 1, 1):
        x_new = round(radius * cos(i / radius))
        y_new = round(radius * sin(i / radius))

        win.image.setPixel(x + x_new, y + y_new, win.pen.color().rgb())
        win.image.setPixel(x + x_new, y - y_new, win.pen.color().rgb())
        win.image.setPixel(x - x_new, y + y_new, win.pen.color().rgb())
        win.image.setPixel(x - x_new, y - y_new, win.pen.color().rgb())

def param_ellipse(win, x, y, a, b):
    len = round(pi * max(a, b) / 2)
    for i in range (0, len + 1, 1):
        x_new = round(a * cos(i / max(a, b)))
        y_new = round(b * sin(i / max(a, b)))

        win.image.setPixel(x + x_new, y + y_new, win.pen.color().rgb())
        win.image.setPixel(x + x_new, y - y_new, win.pen.color().rgb())
        win.image.setPixel(x - x_new, y + y_new, win.pen.color().rgb())
        win.image.setPixel(x - x_new, y - y_new, win.pen.color().rgb())

def brezenham_circle(win, x, y, radius):
    if radius == 0:
        win.image.setPixel(x, y, win.pen.color().rgb())
        return

    yk = 0

    x1 = 0
    y1 = radius
    delta = 2 * (1 - radius)

    while(y1 >= yk):
        win.image.setPixel(x + x1, y + y1, win.pen.color().rgb())
        win.image.setPixel(x - x1, y + y1, win.pen.color().rgb())
        win.image.setPixel(x + x1, y - y1, win.pen.color().rgb())
        win.image.setPixel(x - x1, y - y1, win.pen.color().rgb())

        if delta < 0:
            sigma = 2 * (delta + y1) - 1
            x1 += 1

            if sigma <= 0:
                delta += 2 * x1 + 1
            else:
                y1 -= 1
                delta += 2 * (x1 - y1 + 1)

        elif delta > 0:
            sigma = 2 * (delta - x1) - 1
            y1 -= 1

            if sigma > 0:
                delta += 1 - 2 * y1
            else:
                x1 += 1
                delta += 2 * (x1 - y1 + 1)

        else:
            x1 += 1
            y1 -= 1
            delta += 2 * (x1 - y1 + 1)

def brezenham_ellipse(win, x, y, a, b):
    if a == b == 0:
        win.image.setPixel(x, y, win.pen.color().rgb())
        return

    x1 = 0
    y1 = b
    a *= a
    b *= b
    delta = 0.5 * round(b - a * sqrt(b) * 4 + a)

    while(y1 >= 0):
        win.image.setPixel(x + x1, y + y1, win.pen.color().rgb())
        win.image.setPixel(x - x1, y + y1, win.pen.color().rgb())
        win.image.setPixel(x + x1, y - y1, win.pen.color().rgb())
        win.image.setPixel(x - x1, y - y1, win.pen.color().rgb())

        if delta < 0:
            sigma = 2 * (delta + a * y1) - a
            x1 += 1

            if sigma <= 0:
                delta += 2 * b * x1 + b
            else:
                y1 -= 1
                delta += 2 * (b * x1 - a * y1) + a + b

        elif delta > 0:
            sigma = 2 * (delta - b * x1) - b
            y1 -= 1

            if sigma > 0:
                delta += a - 2 * a * y1
            else:
                x1 += 1
                delta += 2 * (b * x1 - a * y1) + a + b

        else:
            x1 += 1
            y1 -= 1
            delta += 2 * (b * x1 - a * y1) + a + b

def middle_point_circle(win, x, y, radius):
    if radius == 0:
        win.image.setPixel(x, y, win.pen.color().rgb())
        return

    x1 = 0
    y1 = radius
    d = 1.25 - radius

    while (y1 >= x1):
        win.image.setPixel(x - x1, y + y1, win.pen.color().rgb())
        win.image.setPixel(x + x1, y - y1, win.pen.color().rgb())
        win.image.setPixel(x - x1, y - y1, win.pen.color().rgb())
        win.image.setPixel(x + x1, y + y1, win.pen.color().rgb())

        win.image.setPixel(x - y1, y + x1, win.pen.color().rgb())
        win.image.setPixel(x + y1, y - x1, win.pen.color().rgb())
        win.image.setPixel(x - y1, y - x1, win.pen.color().rgb())
        win.image.setPixel(x + y1, y + x1, win.pen.color().rgb())

        x1 += 1

        if d < 0:
            d += 2 * x1 + 1

        else:
            d += 2 * (x1 - y1) + 5
            y1 -= 1

def middle_point_ellipse(win, x, y, a, b):
    x1 = 0
    y1 = b
    p = b ** 2 - a ** 2 * b + 0.25 * a ** 2
    while 2 * (b ** 2) * x1 < 2 * a ** 2 * y1:
        win.image.setPixel(x - x1, y + y1, win.pen.color().rgb())
        win.image.setPixel(x + x1, y - y1, win.pen.color().rgb())
        win.image.setPixel(x - x1, y - y1, win.pen.color().rgb())
        win.image.setPixel(x + x1, y + y1, win.pen.color().rgb())

        x1 += 1

        if p < 0:
            p += 2 * b ** 2 * x1 + b ** 2
        else:
            y1 -= 1
            p += 2 * b ** 2 * x1 - 2 * a ** 2 * y1 + b ** 2

    p = (b * (x1 + 0.5)) ** 2 + (a * (y1 - 1)) ** 2 - (a * b) ** 2


    while y1 >= 0:
        win.image.setPixel(x - x1, y + y1, win.pen.color().rgb())
        win.image.setPixel(x + x1, y - y1, win.pen.color().rgb())
        win.image.setPixel(x - x1, y - y1, win.pen.color().rgb())
        win.image.setPixel(x + x1, y + y1, win.pen.color().rgb())

        y1 -= 1

        if p > 0:
            p -= 2 * a ** 2 * (y1 + 1)
        else:
            x1 += 1
            p += 2 * (b ** 2 * x1 - a ** 2 * y1) + a ** 2

def draw_circle(win):
    choice = str(win.algorythm.currentText())
    xc = win.xc_circle.value()
    yc = win.yc_circle.value()
    rad = win.radius.value()
    is_lib_met = False

    if choice == 'Каноническое уравнение':
        canon_circle(win, xc, yc, rad)
    elif choice == 'Параметрическое уравнение':
        param_circle(win, xc, yc, rad)
    elif choice == 'Брезенхем':
        brezenham_circle(win, xc, yc, rad)
    elif choice == 'Алгоритм средней точки':
        middle_point_circle(win, xc, yc, rad)
    elif choice == 'Библиотечный алгоритм':
        is_lib_met = True
        win.scene.addEllipse(xc - rad, yc - rad, rad * 2, rad * 2, win.pen)

    if not is_lib_met:
        win.update()

def draw_ellipse(win):
    choice = str(win.algorythm.currentText())
    xc = win.xc_ellipse.value()
    yc = win.yc_ellipse.value()
    a = win.a.value()
    b = win.b.value()
    is_lib_met = False

    if choice == 'Каноническое уравнение':
        canon_ellipse(win, xc, yc, a, b)
    elif choice == 'Параметрическое уравнение':
        param_ellipse(win, xc, yc, a, b)
    elif choice == 'Брезенхем':
        brezenham_ellipse(win, xc, yc, a, b)
    elif choice == 'Алгоритм средней точки':
        middle_point_ellipse(win, xc, yc, a, b)
    elif choice == 'Библиотечный алгоритм':
        is_lib_met = True
        win.scene.addEllipse(xc - a, yc - b, a * 2, b * 2, win.pen)

    if not is_lib_met:
        win.update()

def analize_circle(win):
    choice = win.algorythm.currentText()
    times = win.num_circle.value()
    rad = win.min_radius.value()
    step = win.step_radius.value()
    xc = int(win.cnv_view.width()/2)
    yc = int(win.cnv_view.height()/2)
    is_lib_met = False

    for i in range (times):
        if choice == 'Каноническое уравнение':
            canon_circle(win, xc, yc, rad)
        elif choice == 'Параметрическое уравнение':
            param_circle(win, xc, yc, rad)
        elif choice == 'Брезенхем':
            brezenham_circle(win, xc, yc, rad)
        elif choice == 'Алгоритм средней точки':
            middle_point_circle(win, xc, yc, rad)
        elif choice == 'Библиотечный алгоритм':
            is_lib_met = True
            win.scene.addEllipse(xc - rad, yc - rad, rad * 2, rad * 2, win.pen)
        rad += step

    if not is_lib_met:
        win.update()

def analize_ellipse(win):
    choice = win.algorythm.currentText()
    times = win.num_ellipse.value()
    a = win.min_a.value()
    b = win.min_b.value()
    step_a = win.step_a.value()
    step_b = win.step_b.value()
    xc = int(win.cnv_view.width()/2)
    yc = int(win.cnv_view.height()/2)
    is_lib_met = False

    for i in range (times):
        if choice == 'Каноническое уравнение':
            canon_ellipse(win, xc, yc, a, b)
        elif choice == 'Параметрическое уравнение':
            param_ellipse(win, xc, yc, a, b)
        elif choice == 'Брезенхем':
            brezenham_ellipse(win, xc, yc, a, b)
        elif choice == 'Алгоритм средней точки':
            middle_point_ellipse(win, xc, yc, a, b)
        elif choice == 'Библиотечный алгоритм':
            is_lib_met = True
            win.scene.addEllipse(xc - a, yc - b, a * 2, b * 2, win.pen)
        a += step_a
        b += step_b

    if not is_lib_met:
        win.update()

def canon_cirlce_analize(x, y, radius):
    for i in range (0, int(radius) + 1, 1):
        y_new = round(sqrt(radius ** 2 - i ** 2))

    for i in range (0, int(radius) + 1, 1):
        x_new = round(sqrt(radius ** 2 - i ** 2))

def param_circle_analize(x, y, radius):
    len = round(pi * radius / 2)
    for i in range (0, len + 1, 1):
        x_new = round(radius * cos(i / radius))
        y_new = round(radius * sin(i / radius))

def brezenham_circle_analize(x, y, radius):
    if radius == 0:
        return

    yk = 0

    x1 = 0
    y1 = radius
    delta = 2 * (1 - radius)

    while(y1 >= yk):
        if delta < 0:
            sigma = 2 * (delta + y1) - 1
            x1 += 1

            if sigma <= 0:
                delta += 2 * x1 + 1
            else:
                y1 -= 1
                delta += 2 * (x1 - y1 + 1)

        elif delta > 0:
            sigma = 2 * (delta - x1) - 1
            y1 -= 1

            if sigma > 0:
                delta += 1 - 2 * y1
            else:
                x1 += 1
                delta += 2 * (x1 - y1 + 1)

        else:
            x1 += 1
            y1 -= 1
            delta += 2 * (x1 - y1 + 1)

def middle_point_circle_analize(x, y, radius):
    if radius == 0:
        return

    x1 = 0
    y1 = radius
    d = 1.25 - radius

    while (y1 >= x1):
        x1 += 1

        if d < 0:
            d += 2 * x1 + 1

        else:
            d += 2 * (x1 - y1) + 5
            y1 -= 1

def analize_radius_circle(win):
    xc = int(win.cnv_view.width()/2)
    yc = int(win.cnv_view.height()/2)

    names = ('Canon', 'Parametr', 'Brezenham', 'Middle\nPoint', 'Lib')
    plt.figure(1)
    plt.close("all")
    plt.figure(1)
    plt.title("Radius to time analisis")
    plt.xlabel("Radius")
    plt.ylabel("Time")
    plt.grid(True)

    data_canon = []
    data_param = []
    data_brez = []
    data_middle = []
    data_lib = []

    for i in range (1, 21, 1):
        time_start = time.clock()
        canon_cirlce_analize(xc, yc, i)
        time_end = time.clock()
        data_canon.append([i, time_end - time_start])

        time_start = time.clock()
        param_circle_analize(xc, yc, i)
        time_end = time.clock()
        data_param.append([i, time_end - time_start])

        time_start = time.clock()
        brezenham_circle_analize(xc, yc, i)
        time_end = time.clock()
        data_brez.append([i, time_end - time_start])

        time_start = time.clock()
        middle_point_circle_analize(xc, yc, i)
        time_end = time.clock()
        data_middle.append([i, time_end - time_start])

        scene = QtWidgets.QGraphicsScene(0, 0, 541, 561)
        time_start = time.clock()
        scene.addEllipse(xc - i, yc - i, i * 2, i * 2, win.pen)
        time_end = time.clock()
        data_lib.append([i, time_end - time_start])

    pylab.xlim(1, 20)
    pylab.ylim(0, 0.0005)

    axes = pylab.gca()

    for i in range (len(data_canon) - 1):
        line = lines.Line2D([data_canon[i][0], data_canon[i + 1][0]], [data_canon[i][1], data_canon[i + 1][1]], color = 'k')
        axes.add_line(line)

        line = lines.Line2D([data_param[i][0], data_param[i + 1][0]], [data_param[i][1], data_param[i + 1][1]], color = 'r')
        axes.add_line(line)

        line = lines.Line2D([data_brez[i][0], data_brez[i + 1][0]], [data_brez[i][1], data_brez[i + 1][1]], color = 'g')
        axes.add_line(line)

        line = lines.Line2D([data_middle[i][0], data_middle[i + 1][0]], [data_middle[i][1], data_middle[i + 1][1]], color = 'b')
        axes.add_line(line)

        line = lines.Line2D([data_lib[i][0], data_lib[i + 1][0]], [data_lib[i][1], data_lib[i + 1][1]], color = 'm')
        axes.add_line(line)

    plt.legend(names)
    plt.show()

def clear_all(win):
    win.image = QImage(541, 561, QImage.Format_ARGB32_Premultiplied)
    win.scene.clear()

def get_line_color(win):
    color = QtWidgets.QColorDialog.getColor(initial = Qt.black, title = 'Цвет линии',
                                            options = QtWidgets.QColorDialog.DontUseNativeDialog)
    if color.isValid():
        win.line_color = color
        win.pen.setColor(color)
        s = QtWidgets.QGraphicsScene(0, 0, 10, 10)
        s.setBackgroundBrush(color)
        win.line_color_view.setScene(s)

def get_bg_color(win):
    color = QtWidgets.QColorDialog.getColor(initial = Qt.white, title = 'Цвет фона',
                                            options = QtWidgets.QColorDialog.DontUseNativeDialog)
    if color.isValid():
        win.bg_color = color
        s = QtWidgets.QGraphicsScene(0, 0, 10, 10)
        s.setBackgroundBrush(color)
        win.bg_color_view.setScene(s)
        win.scene.setBackgroundBrush(color)

def quit():
    exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())