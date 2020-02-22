from PyQt5 import QtWidgets, uic, QtTest
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap, QPainter, QFont, QPalette
from PyQt5.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QPoint, QPointF, QRect, QSize, QPropertyAnimation, QTimer, pyqtSignal
#from PyQt5.QtWidgets import QMessageBox

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window3.ui", self)
        self.scene = myScene(0, 0, 551, 571)
        self.scene.win = self
        self.view.setScene(self.scene)
        self.image = QImage(561, 581, QImage.Format_ARGB32_Premultiplied)
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
        self.point_now = None
        self.point_lock = None
        self.check_color = True
        self.check_lock = False
        self.check_filled = False
        self.pen = QPen(self.line_color)

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

    # def mouseMoveEvent(self, event):
    #     if event.buttons() == Qt.LeftButton:
    #         self.move(event.globalPos() - self.dragPosition)
    #         event.accept()

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

    def mousePressEvent(self, event):
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

def add_row(win):
    win.table.insertRow(win.table.rowCount())

def add_point(point):
    global w
    w.check_filled = True

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

    w.check_lock = False

def lock(win):
    if win.point_now and len(win.edges) >= 2:
        win.edges.append([win.point_now.x(), win.point_now.y(), win.point_lock.x(), win.point_lock.y()])
        win.scene.addLine(win.point_now.x(), win.point_now.y(), win.point_lock.x(), win.point_lock.y(), w.pen)
        win.point_now = None
        win.point_lock = None
        win.check_lock = True
    elif len(win.edges) == 0:
        QtWidgets.QMessageBox.warning(win, "Error", "Точки для замыкания не введены")
    else:
        QtWidgets.QMessageBox.warning(win, "Error", "Недостаточно данных для замыкания\nобласти и определения многоугольника")

def clean_all(win):
    win.scene.clear()
    win.table.clear()
    win.edges = []
    win.point_now = None
    win.point_lock = None
    win.check_lock = False
    win.check_filled = False
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
    QtTest.QTest.qWait(time)

def find_max_y(ed):
    x_max = None
    for i in range(len(ed)):
        if x_max is None or ed[i][0] > x_max:
            x_max = ed[i][0]

        if x_max is None or ed[i][2] > x_max:
            x_max = ed[i][2]

    return x_max

def fill_xor(win):
    if win.check_color == False:
        draw_edges(win.edges)

    if win.check_lock == True:
        pix = QPixmap()
        p = QPainter()

        delay_time = win.delay_time_ent.value()
        xm = int(find_max_y(win.edges))
        xm += 20
        for ed in win.edges:
            p.begin(win.image)
            if ed[1] == ed[3]:
                continue

            if ed[1] > ed[3]:
                ed[1], ed[3] = ed[3], ed[1]
                ed[0], ed[2] = ed[2], ed[0]

            y = ed[1]
            end_y = ed[3]
            dx = (ed[2] - ed[0]) / (ed[3] - ed[1])
            start_x = ed[0]

            while y < end_y:
                x = start_x
                while x < xm:
                    col = QColor(win.image.pixel(x, y))
                    if col == win.bg_color:
                        p.setPen(QPen(win.fill_color))
                    elif col == win.line_color:
                        x += 1
                        continue
                    elif col == win.fill_color:
                        p.setPen(QPen(win.bg_color))

                    p.drawPoint(x, y)
                    x += 1

                start_x += dx
                y += 1

                if delay_time:
                    delay(delay_time)
                    pix.convertFromImage(win.image)
                    win.scene.addPixmap(pix)

            if not delay_time:
                pix.convertFromImage(win.image)
                win.scene.addPixmap(pix)
            p.end()
            win.check_filled = False
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