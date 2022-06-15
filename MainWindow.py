import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
import numpy as np
import tensorflow as tf

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('숫자 이미지 분류 프로그램', self)
        label1.setAlignment(Qt.AlignCenter)

        font1 = label1.font()
        font1.setPointSize(20)

        label1.setFont(font1)

        btnOpen = QPushButton(self)
        btnOpen.setText('숫자 이미지 불러오기')
        btnOpen.clicked.connect(self.onButtonImg)

        btnDraw = QPushButton(self)
        btnDraw.setText('숫자 그리기')
        btnDraw.clicked.connect(self.onButtonDraw)

        btnQuit = QPushButton('Quit', self)
        btnQuit.clicked.connect(QCoreApplication.instance().quit)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(btnOpen)
        vbox.addWidget(btnDraw)
        vbox.addWidget(btnQuit)

        self.setLayout(vbox)
        self.setWindowTitle('숫자 이미지 분류 프로그램 220124101 강수연')
        self.setGeometry(400, 400, 400, 400)
        self.show()


    def onButtonImg(self):
        self.w = ImgLoadWindow()

    def onButtonDraw(self):
        self.drwaimg = DrawNumberWindow()


class ImgLoadWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('이미지 불러오기')
        self.pushButton = QPushButton('File Open')
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()
        self.label2 = QLabel('cv라이브러리를 이용한 숫자 이미지 분류를 구현하는 중입니다.',self)

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)
        layout.addWidget(self.label2)
        self.setLayout(layout)
        self.show()

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label.setPixmap(QtGui.QPixmap(fname[0]))
        self.label2 = QLabel('cv라이브러리를 이용한 숫자 이미지 분류를 구현하는 중입니다.', self)



class DrawNumberWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.image = QImage(QSize(400, 400), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brush_size = 30
        self.brush_color = Qt.black
        self.last_point = QPoint()
        self.loaded_model = None
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('File')

        load_model_action = QAction('Load model', self)
        load_model_action.setShortcut('Ctrl+L')
        load_model_action.triggered.connect(self.load_model)

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save)

        clear_action = QAction('Clear', self)
        clear_action.setShortcut('Ctrl+C')
        clear_action.triggered.connect(self.clear)

        filemenu.addAction(load_model_action)
        filemenu.addAction(save_action)
        filemenu.addAction(clear_action)

        self.statusbar = self.statusBar()
        self.setWindowTitle('숫자 이미지 분류 프로그램')
        self.setGeometry(300, 300, 400, 400)
        self.show()

    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = e.pos()

    def mouseMoveEvent(self, e):
        if (e.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(self.last_point, e.pos())
            self.last_point = e.pos()
            self.update()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = False

            arr = np.zeros((28, 28))
            for i in range(28):
                for j in range(28):
                    arr[j, i] = 1 - self.image.scaled(28, 28).pixelColor(i, j).getRgb()[0] / 255.0
            arr = arr.reshape(-1, 28, 28)

            if self.loaded_model:
                pred = self.loaded_model.predict(arr)[0]
                pred_num = str(np.argmax(pred))
                self.statusbar.showMessage('숫자 ' + pred_num + '입니다.')

    def load_model(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Load Model', '',"moel File(*.h5)")

        if fname:
            self.loaded_model = tf.keras.models.load_model(fname)
            self.statusbar.showMessage('Model loaded.')

    def save(self):
        fpath, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if fpath:
            self.image.scaled(28, 28).save(fpath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()
        self.statusbar.clearMessage()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = MainWindow()
    sys.exit(app.exec())