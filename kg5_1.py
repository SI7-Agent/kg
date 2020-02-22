from PyQt5 import QtWidgets, uic, QtTest
from PyQt5.QtWidgets import QTableWidgetItem, QApplication
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap, QPainter, QFont, QPalette
from PyQt5.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QPoint, QPointF, QRect, QSize, QPropertyAnimation, QTimer, pyqtSignal
#from PyQt5.QtWidgets import QMessageBox
from operator import itemgetter


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window3.ui", self)
        self.scene = myScene(0, 0, 551, 571)
        self.scene.win = self
        self.view.setScene(self.scene)
        self.view.setMouseTracking(True)
        self.image = QImage(561, 581, QImage.Format_ARGB32_Premultiplied)
        self.backup_line = None
        self.line_color = Qt.black
        self.fill_color = Qt.black
        self.bg_color = Qt.white
        self.image.fill(self.bg_color)

        self.btn_line_color.clicked.connect(lambda: get_line_color(self))
        self.btn_bg_color.clicked.connect(lambda: get_fill_color(self))
        self.addpoint.clicked.connect(lambda: add_point_by_btn(self))

        self.lock.clicked.connect(lambda: lock(self))
        self.paint.clicked.connect(lambda: fill_xor(self))
        self.erase.clicked.connect(lambda: clean_all(self))
        self.exit.clicked.connect(lambda: quit())

        self.edges = []
        self.points = []
        self.tops = []
        self.min_y = 571
        self.max_y = 0
        self.min_x = 551
        self.max_x = 0

        self.point_now = None
        self.point_lock = None
        self.check_color = True
        self.check_lock = False
        self.check_filled = False
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

            if self.flag:
                if w.point_now:
                    if (abs(x - w.point_now.x()) > abs(y - w.point_now.y())):
                        y = w.point_now.y()
                    else:
                        x = w.point_now.x()

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
        if w.point_now:
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

def get_intersections(edges):
    intersections = []

    for i in range(len(edges)):
        x1 = edges[i][0]
        y1 = edges[i][1]
        x2 = edges[i][2]
        y2 = edges[i][3]

        len_x = abs(int(x2) - int(x1))
        len_y = abs(int(y2) - int(y1))

        if len_y != 0:
            dx = ((x2 > x1) - (x2 < x1)) * len_x / len_y
            dy = ((y2 > y1) - (y2 < y1))

            x1 += dx / 2
            y1 += dy / 2

            for j in range(len_y):
                intersections.append((x1, y1))
                x1 += dx
                y1 += dy

    return intersections

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
    win.backup_line = None
    win.image.fill(win.bg_color)
    r = win.table.rowCount()
    for i in range(r, -1, -1):
        win.table.removeRow(i)

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
   # QApplication.processEvents()
    QtTest.QTest.qWait(time)

def fill_xor(win):
    if win.check_lock == True:
        qp = QPainter()
        delay_time = int(win.delay_time_ent.isChecked())

        draw_edges(win.edges)

        qp.begin(win.image)
        qp.setPen(QPen(win.fill_color))

        intersections = get_intersections(win.edges)
        intersections.sort(key = itemgetter(1, 0))

        for i in range(0, len(intersections), 2):
            qp.drawLine(intersections[i][0] + 0.5, intersections[i][1], (intersections[i + 1][0] - 0.5) + 1,
                        intersections[i][1])

            if delay_time:
                win.scene.clear()
                draw_edges(win.edges)
                delay(delay_time)
                win.update()
        qp.end()

        if not delay_time:
            win.update()

        draw_edges(win.edges)
    else:
        QtWidgets.QMessageBox.warning(win, "Error", "Область не замкнута\nМногоугольник не определен")

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