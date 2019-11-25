# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.Qt import *
import cgitb
import time
import client

login_height = 300
login_width = 425
background_path = "./images/star.jpg"
tiancao_path = "./images/tiancao.png"
star_path = "./images/little_star.png"
darkstar_path = "./images/dark_star.png"
cgitb.enable(format = 'text')


class star(QObject):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap(star_path)
        scaledPixmap = pixmap.scaled(login_width * 0.15,login_width * 0.15)
        self.animation()
        self.pixmap_item = QGraphicsPixmapItem(scaledPixmap)
        self.pixmap_item.setTransformOriginPoint(login_width * 0.075, login_width * 0.075)  # 设置中心为旋转
        self._set_pos(QPointF(login_width * 0.07, login_height * 0.1))  # 设置图标的初始位置

    def _set_pos(self, pos):
        self.pixmap_item.setPos(pos)

    def _set_rotation(self, angle):
        self.pixmap_item.setRotation(angle.x())

    def animation(self):
        self.anim = QPropertyAnimation(self, b'pos')
        self.anim.setDuration(1000)
        self.anim.setStartValue(QPointF(login_width * 0.07, login_height * 0.1))
        self.anim.setKeyValueAt(0.5,QPointF(login_width * 0.45, login_height * 0.1))
        self.anim.setEndValue(QPointF(login_width * 0.8, login_height * 0.1))

    pos = pyqtProperty(QPointF, fset = _set_pos)
    rotation = pyqtProperty(QPointF, fset = _set_rotation)

class Ui_loginWindow(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(login_width, login_height)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setFixedSize(QtCore.QSize(login_width, login_height))
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setContentsMargins(0,0,0,0)
        self.Form = Form
        #self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        #self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QLabel(Form)
        self.header.setMinimumSize(QtCore.QSize(login_width, login_height * 0.4))
        self.header.setMaximumSize(QtCore.QSize(login_width, login_height * 0.4))
        self.header.setText("")
        #self.header.setPixmap(QtGui.QPixmap("./images/beidouqixing.png"))
        self.header.setStyleSheet('background-color:rgba(255,255,255,40)')
        self.header.setScaledContents(True)
        self.header.setObjectName("header")
        self.header.setGeometry(QRect(0,0,login_width, login_height * 0.4))
        '''
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0,0,self.header.width(),self.header.height())
        self.star = star()
        self.scene.addItem(self.star.pixmap_item)
        self.setScene(self.scene)
        '''
        #self.addItem(self.star.pixmap_item)
        
        
        
        #self.verticalLayout.addWidget(self.header)
        #spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        #self.verticalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFixedSize(QtCore.QSize(login_width, login_height * 0.6))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(0,login_height/3,login_width,login_height *0.6))
        self.id = QtWidgets.QLabel(self.frame)
        self.id.setGeometry(QtCore.QRect(login_width / 15, login_height * 0.1, login_width/5, login_height/10))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.id.setStyleSheet('color: #FFFFFF;font-weight:24;')
        self.password = QtWidgets.QLabel(self.frame)
        self.password.setGeometry(QtCore.QRect(login_width / 15, login_height * ( 2.2/10) , login_width/5, login_height/10))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.password.setStyleSheet('color: #FFFFFF;font-weight:24;')
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.id_box = QtWidgets.QLineEdit(self.frame)
        self.id_box.setGeometry(QtCore.QRect(login_width * 0.19, login_height * 0.12, login_width * 0.55, login_height * 0.07))
        self.id_box.setObjectName("id_box")
        self.id_box.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,126);font-size:16px;font-weight:bold;color:white;font-family:Comic Sans MS;")
        self.password_box = QtWidgets.QLineEdit(self.frame)
        self.password_box.setGeometry(QtCore.QRect(login_width * 0.19, login_height*0.24, login_width * 0.55, login_height * 0.07))
        self.password_box.setObjectName("password_box")
        self.password_box.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,126);font-size:16px;font-weight:bold;color:white;font-family:Comic Sans MS;")
        self.remember_pw = QtWidgets.QCheckBox(self.frame)
        self.remember_pw.setGeometry(QtCore.QRect(login_width * 0.19, login_height * 0.36, 100, 25))
        self.remember_pw.setObjectName("remember_pw")
        self.remember_pw.setStyleSheet("font-size:16px;color:white;font-weight:20px")
        self.aotu_login = QtWidgets.QCheckBox(self.frame)
        self.aotu_login.setGeometry(QtCore.QRect(login_width * 0.49, login_height * 0.36, 100, 25))
        self.aotu_login.setStyleSheet("font-size:16px;color:white;font-weight:20px")
        self.aotu_login.setObjectName("aotu_login")
        self.login_button = QtWidgets.QPushButton(self.frame)
        self.login_button.setGeometry(QtCore.QRect(login_width * 0.78, login_height * 0.12, login_width * 0.2, login_height * 0.19))
        self.login_button.setObjectName("login_button")
        self.login_button.setStyleSheet("border-radius:10px;font-family:Comic Sans MS;font-size:16px;color:white;font-weight:20px;background-color:rgba(255,255,255,126)")
        #self.verticalLayout.addWidget(self.frame)
        #spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        #self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.id.setText(_translate("Form", "账号"))
        self.password.setText(_translate("Form", "密码"))
        self.remember_pw.setText(_translate("Form", "记住密码"))
        self.aotu_login.setText(_translate("Form", "自动登录"))
        self.login_button.setText(_translate("Form", "Login"))


class LoginPage(QWidget, Ui_loginWindow):
    CLOSE = QtCore.pyqtSignal()
    

    def __init__(self, parent=None):
        super(LoginPage, self).__init__(parent)
        self.setupUi(self) # 可以在外部调用这个LoginPage的CLOSE信号
        self.CLOSE.connect(self.close)
        background_palette = QPalette()
        background_pixmap = QPixmap(background_path).scaled(self.width(),self.height())
        background_palette.setBrush(self.backgroundRole(),QBrush(background_pixmap))
        self.setPalette(background_palette)
        self.login_button.clicked.connect(self.login_anim)
        self.login_button.setCursor(Qt.OpenHandCursor)
        self.star_label = QtWidgets.QLabel(self.Form)
        self.star_label.setPixmap(QPixmap(star_path))
        self.star_label.setScaledContents(True)
        self.star_label.setObjectName("star")
        self.star_label.resize(QSize(login_width * 0.1,login_width * 0.1))
        self.star_label.setGeometry(QRect(login_width * 0.03, login_height * 0.16, login_width * 0.1, login_width * 0.1))
        #self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("border-radius:20px")
        self.close_button = QtWidgets.QPushButton(self.Form)
        self.close_button.setStyleSheet("QPushButton{border-image: url('./images/dark_star');}")
        self.close_button.setCursor(Qt.OpenHandCursor)
        self.close_button.setObjectName("close")
        self.close_button.resize(QSize(login_width * 0.1,login_width * 0.1))
        self.close_button.setGeometry(QRect(login_width * 0.88, login_height * 0.02, login_width * 0.1, login_width * 0.1))
        self.close_button.clicked.connect(self.CLOSE)


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_bigtrigger(qp)
        qp.end()

    def draw_bigtrigger(self,qp):
        pen = QPen(Qt.white, 0.3, Qt.CustomDashLine)
        qp.setPen(pen)
        qp.drawLine(login_width * 0.08, login_height * 0.21,login_width * 0.25, login_height * 0.15)
        qp.drawLine(login_width * 0.25, login_height * 0.15,login_width * 0.32, login_height * 0.18)
        qp.drawLine(login_width * 0.32, login_height * 0.18, login_width * 0.5, login_height * 0.19)
        qp.drawLine(login_width * 0.5, login_height * 0.19, login_width * 0.56, login_height * 0.29)
        qp.drawLine(login_width * 0.56, login_height * 0.29, login_width * 0.81, login_height * 0.22)
        qp.drawLine(login_width * 0.81, login_height * 0.22, login_width * 0.79, login_height * 0.13)
        

        #self.frame.setStyleSheet("background-image:url('./images/star.jpg') ")
    def login_anim(self):
        
        self.anim = QPropertyAnimation(self.star_label,b'geometry')
        self.anim.setDuration(6000)
        self.anim.setStartValue(QRect(login_width * 0.03, login_height * 0.16, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.15,QRect(login_width * 0.19, login_height * 0.09, login_width * 0.12, login_width * 0.12))
        self.anim.setKeyValueAt(0.17,QRect(login_width * 0.2, login_height * 0.1, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.19,QRect(login_width * 0.2, login_height * 0.1, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.3,QRect(login_width * 0.27, login_height * 0.13, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.32,QRect(login_width * 0.26, login_height * 0.12, login_width * 0.12, login_width * 0.12))
        self.anim.setKeyValueAt(0.34,QRect(login_width * 0.27, login_height * 0.13, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.45,QRect(login_width * 0.45, login_height * 0.14, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.47,QRect(login_width * 0.44, login_height * 0.13, login_width * 0.12, login_width * 0.12))
        self.anim.setKeyValueAt(0.49,QRect(login_width * 0.45, login_height * 0.14, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.6,QRect(login_width * 0.51, login_height * 0.24, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.62,QRect(login_width * 0.50, login_height * 0.23, login_width * 0.12, login_width * 0.12))
        self.anim.setKeyValueAt(0.64,QRect(login_width * 0.51, login_height * 0.24, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.75,QRect(login_width * 0.76, login_height * 0.17, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.77,QRect(login_width * 0.75, login_height * 0.16, login_width * 0.12, login_width * 0.12))
        self.anim.setKeyValueAt(0.79,QRect(login_width * 0.76, login_height * 0.17, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.9,QRect(login_width * 0.74, login_height * 0.08, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.94,QRect(login_width * 0.72, login_height * 0.06, login_width * 0.14, login_width * 0.14))
        self.anim.setEndValue(QRect(login_width * 0.03, login_height * 0.16, login_width * 0.1, login_width * 0.1))
        self.anim.start()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
       

'''
        sleepthread = SleepThread()
        sleepthread.signal_sleep6000.connect(client.log_in) #在这里调用log_in进行登录
        sleepthread.signal_sleep1.connect(self.login_anim)
        sleepthread.Sleep()

    def login_anim(self):
        self.anim = QPropertyAnimation(self.star_label,b'geometry')
        self.anim.setDuration(6000)
        self.anim.setStartValue(QRect(login_width * 0.03, login_height * 0.16, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.15,QRect(login_width * 0.19, login_height * 0.09, login_width * 0.12, login_width * 0.12))
        self.anim.setKeyValueAt(0.17,QRect(login_width * 0.2, login_height * 0.1, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.19,QRect(login_width * 0.2, login_height * 0.1, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.3,QRect(login_width * 0.27, login_height * 0.13, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.32,QRect(login_width * 0.26, login_height * 0.12, login_width * 0.12, login_width * 0.12))
        self.anim.setKeyValueAt(0.34,QRect(login_width * 0.27, login_height * 0.13, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.45,QRect(login_width * 0.45, login_height * 0.14, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.47,QRect(login_width * 0.44, login_height * 0.13, login_width * 0.12, login_width * 0.12))
        self.anim.setKeyValueAt(0.49,QRect(login_width * 0.45, login_height * 0.14, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.6,QRect(login_width * 0.51, login_height * 0.24, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.62,QRect(login_width * 0.50, login_height * 0.23, login_width * 0.12, login_width * 0.12))
        self.anim.setKeyValueAt(0.64,QRect(login_width * 0.51, login_height * 0.24, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.75,QRect(login_width * 0.76, login_height * 0.17, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.77,QRect(login_width * 0.75, login_height * 0.16, login_width * 0.12, login_width * 0.12))
        self.anim.setKeyValueAt(0.79,QRect(login_width * 0.76, login_height * 0.17, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.9,QRect(login_width * 0.74, login_height * 0.08, login_width * 0.1, login_width * 0.1))
        self.anim.setKeyValueAt(0.94,QRect(login_width * 0.72, login_height * 0.06, login_width * 0.14, login_width * 0.14))
        self.anim.setEndValue(QRect(login_width * 0.03, login_height * 0.16, login_width * 0.1, login_width * 0.1))
        self.anim.start()


class SleepThread(QThread):
    signal_sleep1 = pyqtSignal()
    signal_sleep6000 = pyqtSignal()

    def __init__(self, sec = 6000, parent = None):
        super().__init__(parent)
        self.sec = sec

    def Sleep(self):
        self.signal_sleep1.emit()
        print('emitted to sleep')
        for i in range(6):
            self.sleep(1)
        print('sleep over')
        self.signal_sleep6000.emit()
'''

