from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
import copy

class MyWindow(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi("untitled.ui", self)

        self.bg_color = QColor(Qt.white)
        self.line_color = QColor(Qt.red)
        self.cutter_color = QColor(Qt.black)
        self.cut_line_color = QColor(Qt.green)

        self.ctrl_pressed = False
        self.lines = []
        self.cur_line = []
        self.follow_line = None

        self.cutter = None
        self.drawing_cutter = False
        self.cur_cutter = []
        self.follow_cutter = None

        self.scene = QGraphicsScene(0, 0, 1920, 1080)
        self.mainview.setScene(self.scene)
        self.pen = QPen()
        self.mainview.ensureVisible(0, 0, 0, 0)
        self.mainview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mainview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.inputs = [
            self.but_add_line,
            self.but_add_cutter,
            self.but_choose_cutter,
            self.but_cut,
            self.but_clear,
            self.inp_x1,
            self.inp_x2,
            self.inp_y1,
            self.inp_y2,
            self.inp_x_left,
            self.inp_x_right,
            self.inp_y_up,
            self.inp_y_down
        ]

        reg_ex = QRegExp("[0-9]+")
        int_validator = QRegExpValidator(reg_ex, self)
        self.inp_x1.setValidator(int_validator)
        self.inp_x2.setValidator(int_validator)
        self.inp_y1.setValidator(int_validator)
        self.inp_y2.setValidator(int_validator)
        self.inp_x_left.setValidator(int_validator)
        self.inp_x_right.setValidator(int_validator)
        self.inp_y_up.setValidator(int_validator)
        self.inp_y_down.setValidator(int_validator)

        self.but_add_line.clicked.connect(lambda: get_line(self))
        self.but_add_cutter.clicked.connect(lambda: get_cutter(self))
        self.but_choose_cutter.clicked.connect(lambda: choose_cutter(self))
        self.but_cut.clicked.connect(lambda: cut(self))
        self.but_clear.clicked.connect(lambda: clear(self))
        self.but_del_lines.clicked.connect(lambda: clear_with_cutter(self))
        self.but_del_cutter.clicked.connect(lambda: clear_with_lines(self))

        self.mainview.setMouseTracking(True)
        self.mainview.viewport().installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseMove and source is self.mainview.viewport():
            x = event.x()
            y = event.y()

            following_line(self, x, y)
            following_cutter(self, x, y)

        return QWidget.eventFilter(self, source, event)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Control:
            self.ctrl_pressed = True

    def keyReleaseEvent(self, event):
        key = event.key()
        if key == Qt.Key_Control:
            self.ctrl_pressed = False

    def mousePressEvent(self, event):
        but = event.button()
        x = event.x()
        y = event.y()
        borders = self.mainview.geometry().getCoords()
        if borders[0] <= x < borders[2] and borders[1] <= y < borders[3]:
            x -= borders[0]
            y -= borders[1]
        else:
            return

        if but == 1:
            line_on_screen(self, x, y)
            cutter_on_screen(self, x, y)

class Line:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.scene_item = None

class Cutter:
    def __init__(self):
        self.x_left = 0
        self.y_up = 0
        self.x_right = 0
        self.y_down = 0
        self.scene_item = None

def mes(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)

    msg.setWindowTitle("Внимание")
    msg.setText(text)

    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()

def add_line(self, x1, y1, x2, y2, color):
    self.pen.setColor(color)

    line = Line()

    line.x1 = x1
    line.y1 = y1
    line.x2 = x2
    line.y2 = y2
    line.scene_item = self.scene.addLine(x1, y1, x2, y2, self.pen)

    self.lines.append(line)

def add_cutter(self, x_l, y_u, x_r, y_d, color):
    self.pen.setColor(color)

    if x_l > x_r:
        x_l, x_r = x_r, x_l

    if y_u > y_d:
        y_u, y_d = y_d, y_u

    cutter = Cutter()

    cutter.x_left = x_l
    cutter.y_up = y_u
    cutter.x_right = x_r
    cutter.y_down = y_d
    cutter.scene_item = self.scene.addRect(x_l, y_u, x_r - x_l, y_d - y_u, self.pen)

    self.cutter = cutter

def del_cutter(self):
    if self.cutter:
        self.scene.removeItem(self.cutter.scene_item)
    self.cutter = None

def line_on_screen(self, x, y):
    if not self.drawing_cutter:
        if not self.ctrl_pressed or not len(self.cur_line):
            self.cur_line.append((x, y))
        else:
            prev = self.cur_line[0]

            dx = x - prev[0]
            dy = y - prev[1]

            if abs(dy) >= abs(dx):
                self.cur_line.append((prev[0], y))
            else:
                self.cur_line.append((x, prev[1]))

        if len(self.cur_line) == 2:
            c1, c2 = self.cur_line
            add_line(self, c1[0], c1[1], c2[0], c2[1], self.line_color)
            self.cur_line.clear()
            self.scene.removeItem(self.follow_line)

def cutter_on_screen(self, x, y):
    if self.drawing_cutter:
        if len(self.cur_cutter) < 2:
            self.cur_cutter.append((x, y))

        if len(self.cur_cutter) == 2:
            c1, c2 = self.cur_cutter
            add_cutter(self, c1[0], c1[1], c2[0], c2[1], self.cutter_color)
            self.cur_cutter.clear()
            self.scene.removeItem(self.follow_cutter)
            self.drawing_cutter = False

def following_line(self, x, y):
    if len(self.cur_line) == 1:
        prev = self.cur_line[0]
        self.pen.setColor(self.line_color)

        if self.follow_line:
            self.scene.removeItem(self.follow_line)

        if self.ctrl_pressed:
            dx = x - prev[0]
            dy = y - prev[1]

            if abs(dy) >= abs(dx):
                cur = (prev[0], y)
            else:
                cur = (x, prev[1])

            self.follow_line = self.scene.addLine(prev[0], prev[1], cur[0], cur[1], self.pen)
        else:
            self.follow_line = self.scene.addLine(prev[0], prev[1], x, y, self.pen)

def following_cutter(self, x, y):
    if len(self.cur_cutter) == 1:
        x_l, y_u = self.cur_cutter[0]
        x_r, y_d = x, y
        self.pen.setColor(self.cutter_color)

        if self.follow_cutter:
            self.scene.removeItem(self.follow_cutter)

        if x_l > x_r:
            x_l, x_r = x_r, x_l

        if y_u > y_d:
            y_u, y_d = y_d, y_u

        self.follow_cutter = self.scene.addRect(x_l, y_u, x_r - x_l, y_d - y_u, self.pen)

def draw_line(self, dot1, dot2, color):
    self.pen.setColor(color)
    self.scene.addLine(dot1[0], dot1[1], dot2[0], dot2[1], self.pen)

def get_line(self):
    try:
        x1 = int(self.inp_x1.text())
        y1 = int(self.inp_y1.text())
        x2 = int(self.inp_x2.text())
        y2 = int(self.inp_y2.text())
    except ValueError:
        mes("Неверные данные отрезка")
        return -1

    add_line(self, x1, y1, x2, y2, self.line_color)

def get_cutter(self):
    try:
        x_left = int(self.inp_x_left.text())
        y_up = int(self.inp_y_up.text())
        x_right = int(self.inp_x_right.text())
        y_down = int(self.inp_y_down.text())
    except ValueError:
        mes("Неверные данные отрезка")
        return -1

    del_cutter(self)
    add_cutter(self, x_left, y_up, x_right, y_down, self.cutter_color)

def choose_cutter(self):
    del_cutter(self)
    self.drawing_cutter = True

def cut(self):
    if self.cutter:
        for i in range(len(self.lines)):
            xl = self.cutter.x_left
            xr = self.cutter.x_right
            yd = self.cutter.y_down
            yu = self.cutter.y_up
            p1 = [self.lines[i].x1, self.lines[i].y1]
            p2 = [self.lines[i].x2, self.lines[i].y2]
            yu, yd = yd, yu

            visible, p1, p2 = easy_cut(xl, xr, yd, yu, p1, p2)

            if visible:
                draw_line(self, p1, p2, self.cut_line_color)

def count_S(T):
    return sum(T)

def count_P(T1, T2):
    P = 0
    for i in range(len(T1)):
        P += (T1[i] * T2[i])

    return P

def count_T(p, xl, xr, yd, yu):
    x = p[0]
    y = p[1]
    T = [0, 0, 0, 0]
    T[0] = 1 if x < xl else 0
    T[1] = 1 if x > xr else 0
    T[2] = 1 if y < yd else 0
    T[3] = 1 if y > yu else 0
    return T

def sort_cutter(arr):
    if arr[0][0] > arr[1][0]:
        arr[0], arr[1] = arr[1], arr[0]
    return arr

def easy_cut(xl, xr, yd, yu, p1, p2):
    T1 = count_T(p1, xl, xr, yd, yu)
    T2 = count_T(p2, xl, xr, yd, yu)

    FL = 0
    m = 99999  # Infinity

    S1 = count_S(T1)
    S2 = count_S(T2)

    Q = p1
    r1 = copy.deepcopy(p1)
    r2 = copy.deepcopy(p2)

    if (S1 == 0) and (S2 == 0):
        return B_shtrih(FL, r1, r2)

    P = count_P(T1, T2)
    if P != 0:
        return B(r1, r2)

    if S1 == 0:
        r1 = copy.deepcopy(p1)
        Q = copy.deepcopy(p2)
        i = 2
        return A(FL, i, Q, p1, p2, r1, r2, xl, xr, yd, yu, False)

    if S2 == 0:
        r1 = copy.deepcopy(p2)
        Q = copy.deepcopy(p1)
        i = 2
        return A(FL, i, Q, p1, p2, r1, r2, xl, xr, yd, yu, False)

    i = 0
    return A(FL, i, Q, p1, p2, r1, r2, xl, xr, yd, yu)

def B_shtrih(FL, p1, p2):
    if FL == 0:
        return True, p1, p2
    else:
        return False, p1, p2


def B(p1, p2):
    return B_shtrih(1, p1, p2)


def A_skip_1(FL, i, Q, p1, p2, r1, r2, xl, xr, yd, yu, m):
    if m == 0:
        return B(r1, r2)

    if Q[1] < yd:
        x = (yd - Q[1]) / m + Q[0]

        if xl <= x and x <= xr:
            if i == 1:
                r1[0] = x
                r1[1] = yd
            else:
                r2[0] = x
                r2[1] = yd
            return A(FL, i, Q, p1, p2, r1, r2, xl, xr, yd, yu)

    if Q[1] > yu:
        x = (yu - Q[1]) / m + Q[0]

        if xl <= x and x <= xr:
            if i == 1:
                r1[0] = x
                r1[1] = yu
            else:
                r2[0] = x
                r2[1] = yu
            return A(FL, i, Q, p1, p2, r1, r2, xl, xr, yd, yu)

    return B(r1, r2)


def A(FL, i, Q, p1, p2, r1, r2, xl, xr, yd, yu, flag=True):
    if flag:
        i += 1
        if i > 2:
            return B_shtrih(FL, r1, r2)

        Q = p1 if i == 1 else p2

    if p1[0] == p2[0]:
        return A_skip_1(FL, i, Q, p1, p2, r1, r2, xl, xr, yd, yu, 99999)

    m = (p2[1] - p1[1]) / (p2[0] - p1[0])

    if Q[0] < xl:
        y = m * (xl - Q[0]) + Q[1]

        if yd <= y and y <= yu:
            if i == 1:
                r1[0] = xl
                r1[1] = y
            else:
                r2[0] = xl
                r2[1] = y
            return A(FL, i, Q, p1, p2, r1, r2, xl, xr, yd, yu)

    if Q[0] > xr:
        y = m * (xr - Q[0]) + Q[1]

        if yd <= y and y <= yu:
            if i == 1:
                r1[0] = xr
                r1[1] = y
            else:
                r2[0] = xr
                r2[1] = y
            return A(FL, i, Q, p1, p2, r1, r2, xl, xr, yd, yu)

    return A_skip_1(FL, i, Q, p1, p2, r1, r2, xl, xr, yd, yu, m)

def clear(self):
    self.scene.clear()

    self.lines.clear()
    self.cur_line.clear()
    self.follow_line = None

    self.cutter = None
    self.cur_cutter.clear()
    self.follow_cutter = None
    self.drawing_cutter = False

def clear_with_cutter(self):
    self.scene.clear()

    self.lines.clear()
    self.cur_line.clear()
    self.follow_line = None

    if self.cutter:
        self.pen.setColor(self.cutter_color)
        self.scene.addRect(self.cutter.x_left, self.cutter.y_up, self.cutter.x_right - self.cutter.x_left, self.cutter.y_down - self.cutter.y_up, self.pen)

def clear_with_lines(self):
    self.scene.clear()

    if self.lines:
        self.pen.setColor(self.line_color)
        for i in self.lines:
            self.scene.addLine(i.x1, i.y1, i.x2, i.y2, self.pen)

    self.cutter = None
    self.cur_cutter.clear()
    self.follow_cutter = None
    self.drawing_cutter = False

if __name__ == '__main__':
    app = QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())