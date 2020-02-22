from PyQt5 import QtWidgets, uic, QtTest
from PyQt5.QtWidgets import QTableWidgetItem, QApplication
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap, QPainter, QFont, QPalette
from PyQt5.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QPoint, QPointF, QRect, QSize, QPropertyAnimation, QTimer, pyqtSignal
#from PyQt5.QtWidgets import QMessageBox
from math import sqrt


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window4.ui", self)
        self.scene = myScene(0, 0, 551, 571)
        self.scene.win = self
        self.view.setScene(self.scene)
        self.view.setMouseTracking(True)
        self.image = QImage(561, 581, QImage.Format_ARGB32_Premultiplied)
        self.backup_line = None
        self.backup_circle = None
        self.line_color = Qt.black
        self.fill_color = Qt.black
        self.bg_color = Qt.white
        self.image.fill(self.bg_color)

        self.btn_line_color.clicked.connect(lambda: get_line_color(self))
        self.btn_bg_color.clicked.connect(lambda: get_fill_color(self))
        self.addpoint.clicked.connect(lambda: add_point_by_btn(self))
        self.add_circle.clicked.connect(lambda: add_circle(self))
        self.choose_zatrav.clicked.connect(lambda: get_seed(self))

        self.lock.clicked.connect(lambda: lock(self))
        self.paint.clicked.connect(lambda: fill_with_seed(self))
        self.erase.clicked.connect(lambda: clean_all(self))
        self.exit.clicked.connect(lambda: quit())

        self.edges = []
        self.points = []
        self.tops = []
        self.min_y = 571
        self.max_y = 0
        self.min_x = 551
        self.max_x = 0

        self.seed = None
        self.point_now = None
        self.circle_now = None

        self.point_lock = None
        self.draw_circle = False
        self.check_color = True
        self.check_lock = False
        self.check_filled = False
        self.choosing_seed = False
        self.seed_chosen = False
        self.pen = QPen(self.line_color)

    def update(self):
        pix = QPixmap(551, 571)
        pix.convertFromImage(self.image)
        self.scene.addPixmap(pix)

class PopWindow(QtWidgets.QWidget):
    popuphidden = pyqtSignal()

    def __init__(self):
        super(PopWindow, self).__init__()
        self.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.setMinimumSize(QSize(100, 50))
        self.animation = QPropertyAnimation(self, b"windowOpacity", self)
        self.animation.finished.connect(self.hide)
        self.timer = QTimer()
        self.timer.timeout.connect(self.hideAnimation)
        self.setupUi()
        self.text = ""
        self.setPopupText(self.text)

    def setupUi(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel(self)
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)
        appearance = self.palette()
        appearance.setColor(QPalette.Normal, QPalette.Window,
                     Qt.white)
        self.setPalette(appearance)

    def setPopupText(self, text):
        self.label.setText(text)
        self.label.adjustSize()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def show(self):
        self.setWindowOpacity(0.0)
        self.animation.setDuration(1000)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        QtWidgets.QWidget.show(self)
        self.animation.start()
        self.timer.start(2500)

    def hideAnimation(self):
        self.timer.stop()
        self.animation.setDuration(1500)
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.start()

    def hide(self):
        if self.windowOpacity() == 0:
            QtWidgets.QWidget.hide(self)
            self.popuphidden.emit()

class myScene(QtWidgets.QGraphicsScene):
    global w
    flag = False
    prev_x = None
    prev_y = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = event.scenePos().x()
            y = event.scenePos().y()

            if w.choosing_seed:
                w.x_zatrav.setValue(x)
                w.y_zatrav.setValue(y)

                QApplication.restoreOverrideCursor()
                w.choosing_seed = False

            elif self.flag:
                if w.point_now:
                    if (abs(x - w.point_now.x()) > abs(y - w.point_now.y())):
                        y = w.point_now.y()
                    else:
                        x = w.point_now.x()

                point = QPointF(x, y)
                add_point(point)

            elif w.draw_circle:
                if not w.circle_now:
                    w.circle_now = (x, y)
                else:
                    if w.edges:
                        draw_edges(w.edges)
                    r = (abs(w.circle_now[0] - x) ** 2 + abs(w.circle_now[1] - y) ** 2) ** 0.5
                    create_circle(w, w.circle_now, r)
                    w.draw_circle = False
                    w.circle_now = None
                    w.update()
                    w.scene.removeItem(w.backup_circle)

            else:
                point = QPointF(x, y)
                add_point(point)

    def keyPressEvent(self, event):
        if event.modifiers() & Qt.ShiftModifier:
            wind = PopWindow()
            wind.setGeometry(QRect(100, 100, 400, 65))

            if self.flag == False:
                wind.setPopupText("Включен режим рисования\n"
                                  "линий параллельных осям координат")
                self.flag = True
            else:
                wind.setPopupText("Отключен режим рисования\n"
                                  "линий параллельных осям координат")
                self.flag = False

            wind.show()
            wind.move((1366 - 600) / 2, 768 - 200)

    def mouseMoveEvent(self, event):
        if w.point_now and not w.circle_now:
            x_start = w.point_now.x()
            y_start = w.point_now.y()

            x_end = event.scenePos().x()
            y_end = event.scenePos().y()

            if self.flag:
                if w.point_now:
                    if (abs(x_end - w.point_now.x()) > abs(y_end - w.point_now.y())):
                        y_end = w.point_now.y()
                    else:
                        x_end = w.point_now.x()

            if w.backup_line:
                w.scene.removeItem(w.backup_line)

            if self.prev_x and self.prev_y:
                w.backup_line = w.scene.addLine(x_start, y_start, self.prev_x, self.prev_y ,w.pen)

            self.prev_x = x_end
            self.prev_y = y_end

        if w.circle_now:
            if w.backup_line:
                w.scene.removeItem(w.backup_line)

            x_start = w.circle_now[0]
            y_start = w.circle_now[1]

            x_end = event.scenePos().x()
            y_end = event.scenePos().y()

            if w.backup_circle:
                w.scene.removeItem(w.backup_circle)

            r = (abs(x_start - x_end) ** 2 + abs(y_start - y_end) ** 2) ** 0.5
            w.backup_circle = w.scene.addEllipse(x_start - r, y_start - r, 2 * r, 2 * r, w.pen)

def create_circle(win, centre, radius):
    x, y = centre
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

def add_circle(win):
    win.draw_circle = True
    win.check_lock = True

def get_seed(win):
    QApplication.setOverrideCursor(Qt.CrossCursor)
    win.choosing_seed = True
    win.seed_chosen = True

def add_row(win):
    win.table.insertRow(win.table.rowCount())

def add_point(point):
    global w
    w.check_filled = True

    if w.max_x <= point.x():
        w.max_x = point.x()

    if w.max_y <= point.y():
        w.max_y = point.y()

    if w.min_x >= point.x():
        w.min_x = point.x()

    if w.min_y >= point.y():
        w.min_y = point.y()

    if w.point_lock is None:
        w.point_lock = point
        w.point_now = point
        add_row(w)
        i = w.table.rowCount() - 1
        item_x = QTableWidgetItem("{0}".format(point.x()))
        item_y = QTableWidgetItem("{0}".format(point.y()))
        w.table.setItem(i, 0, item_x)
        w.table.setItem(i, 1, item_y)
    else:
        w.edges.append([w.point_now.x(), w.point_now.y(),
                        point.x(), point.y()])
        w.point_now = point
        add_row(w)
        i = w.table.rowCount() - 1
        item_x = QTableWidgetItem("{0}".format(point.x()))
        item_y = QTableWidgetItem("{0}".format(point.y()))
        w.table.setItem(i, 0, item_x)
        w.table.setItem(i, 1, item_y)
        item_x = w.table.item(i - 1, 0)
        item_y = w.table.item(i - 1, 1)
        w.scene.addLine(point.x(), point.y(), float(item_x.text()), float(item_y.text()), w.pen)

    w.tops.append([point.x(), point.y()])
    w.check_lock = False

def lock(win):
    if win.point_now and len(win.edges) >= 2:
        win.edges.append([win.point_now.x(), win.point_now.y(), win.point_lock.x(), win.point_lock.y()])
        win.scene.addLine(win.point_now.x(), win.point_now.y(), win.point_lock.x(), win.point_lock.y(), w.pen)
        win.scene.removeItem(win.backup_line)
        add_row(win)
        i = win.table.rowCount() - 1
        item_x = QTableWidgetItem("###")
        item_y = QTableWidgetItem("###")
        win.table.setItem(i, 0, item_x)
        win.table.setItem(i, 1, item_y)
        win.point_now = None
        win.point_lock = None
        win.check_lock = True
    elif len(win.edges) == 0:
        QtWidgets.QMessageBox.warning(win, "Error", "Точки для замыкания не введены")
    else:
        QtWidgets.QMessageBox.warning(win, "Error", "Недостаточно данных для замыкания\nобласти и определения многоугольника")

def clean_all(win):
    win.scene.clear()
    win.edges = []
    win.points = []
    win.tops = []
    win.min_y = 571
    win.max_y = 0
    win.min_x = 551
    win.max_x = 0
    win.point_now = None
    win.point_lock = None
    win.check_lock = False
    win.check_filled = False
    win.choosing_seed = False
    win.seed_chosen = False
    win.backup_line = None
    win.image.fill(win.bg_color)
    r = win.table.rowCount()
    for i in range(r, -1, -1):
        win.table.removeRow(i)

def put_borders(self, color):
    qp = QPainter()
    qp.begin(self.image)
    qp.setPen(QPen(color))
    for i in range(553):
        qp.drawPoint(i, 0)
        qp.drawPoint(i, 572)

    for i in range(573):
        qp.drawPoint(0, i)
        qp.drawPoint(552, i)
    return

def draw_edges(edges):
    global w
    qp = QPainter()
    pix = QPixmap()

    qp.begin(w.image)
    qp.setPen(QPen(w.line_color))
    for ed in edges:
        qp.drawLine(ed[0], ed[1], ed[2], ed[3])
    pix.convertFromImage(w.image)
    w.scene.addPixmap(pix)
    qp.end()

def delay(time):
    QtTest.QTest.qWait(time)

def get_pix(self, x, y):
    return QColor(self.image.pixel(x, y))

def fill_default(self):
    stack = []
    stack.append(self.seed)
    delay_time = int(self.delay_time_ent.isChecked())

    qp = QPainter()

    qp.begin(self.image)
    qp.setPen(QPen(self.fill_color))

    while len(stack) > 0:
        x, y = stack.pop()

        x_temp = x
        qp.drawPoint(x, y)

        x += 1
        while get_pix(self, x, y) != self.line_color:
            qp.drawPoint(x, y)
            x += 1
        x_right = x - 1

        x = x_temp

        x -= 1
        while get_pix(self, x, y) != self.line_color:
            qp.drawPoint(x, y)
            x -= 1
        x_left = x + 1

        if delay_time:
            self.scene.clear()
            draw_edges(self.edges)
            delay(delay_time)
            self.update()

        for i in range(1, -2, -2):
            x = x_left
            y += i
            while x <= x_right:
                flag = False

                while get_pix(self, x, y) != self.line_color and get_pix(self, x, y) != self.fill_color and x < x_right:
                    if not flag:
                        flag = True
                    x += 1

                if flag:
                    if get_pix(self, x, y) != self.line_color and get_pix(self, x, y) != self.fill_color and x == x_right:
                        stack.append((x, y))
                    else:
                        stack.append((x - 1, y))

                x_enter = x
                while (get_pix(self, x, y) == self.line_color or get_pix(self, x, y) == self.fill_color) and x < x_right:
                    x += 1

                if x == x_enter:
                    x += 1
            y -= i

    if not delay_time:
        self.update()
    qp.end()


def fill_with_seed(self):
    if self.check_lock == True:
        x = self.x_zatrav.value()
        y = self.y_zatrav.value()

        if self.seed_chosen == False:
            QtWidgets.QMessageBox.warning(self, "Error",
                                          "Не задан затравочный пиксель")
            return

        self.seed = (x,y)
        put_borders(self, self.line_color)
        draw_edges(self.edges)
        fill_default(self)
        put_borders(self, self.bg_color)
        self.update()

    else:
        QtWidgets.QMessageBox.warning(self, "Error", "Область не замкнута\nМногоугольник не определен")

def add_point_by_btn(win):
    x = win.x.value()
    y = win.y.value()
    p = QPoint()
    p.setX(x)
    p.setY(y)
    add_point(p)

def get_line_color(win):
    if not win.check_filled:
        color = QtWidgets.QColorDialog.getColor(initial = Qt.white, title = 'Цвет границы',
                                                options = QtWidgets.QColorDialog.DontUseNativeDialog)
        if color.isValid():
            win.line_color = color
            win.pen.setColor(color)
            s = QtWidgets.QGraphicsScene(0, 0, 10, 10)
            s.setBackgroundBrush(color)
            win.cnv_line_color.setScene(s)

            if win.fill_color == win.line_color:
                win.check_color = True
            else:
                win.check_color = False
    else:
        QtWidgets.QMessageBox.about(win, "Warning", "Невозможно сменить цвет во время задания многоугольника")

def get_fill_color(win):
    color = QtWidgets.QColorDialog.getColor(initial = Qt.white, title = 'Цвет закраски',
                                                options = QtWidgets.QColorDialog.DontUseNativeDialog)
    if color.isValid():
        win.fill_color = color
        s = QtWidgets.QGraphicsScene(0, 0, 10, 10)
        s.setBackgroundBrush(color)
        win.cnv_bg_color.setScene(s)

        if win.fill_color == win.line_color:
            win.check_color = True
        else:
            win.check_color = False

def quit():
    exit()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    w.move((1366 - w.frameGeometry().width())/2, (768 - w.frameGeometry().height())/2 - 20)
    sys.exit(app.exec_())