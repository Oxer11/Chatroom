# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from Constant import *
from util import *
import cgitb


REG_HEIGHT = 300
REG_WIDTH = 425
cgitb.enable(format='text')


class Ui_registerWindow(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(REG_WIDTH, REG_HEIGHT)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setFixedSize(QtCore.QSize(REG_WIDTH, REG_HEIGHT))
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setContentsMargins(0, 0, 0, 0)
        self.Form = Form

        self.header = QtWidgets.QLabel(Form)
        self.header.setMinimumSize(QtCore.QSize(REG_WIDTH, REG_HEIGHT * 0.4))
        self.header.setMaximumSize(QtCore.QSize(REG_WIDTH, REG_HEIGHT * 0.4))
        self.header.setText("")

        self.header.setStyleSheet('background-color:rgba(255,255,255,40)')
        self.header.setScaledContents(True)
        self.header.setObjectName("header")
        self.header.setGeometry(QRect(0, 0, REG_WIDTH, REG_HEIGHT * 0.4))

        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFixedSize(QtCore.QSize(REG_WIDTH, REG_HEIGHT * 0.6))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(0, REG_HEIGHT * .33,
                                     REG_WIDTH, REG_HEIGHT * 0.6))

        self.id = QtWidgets.QLabel(self.frame)
        self.id.setGeometry(QRect(REG_WIDTH * .067, REG_HEIGHT * .1,
                                  REG_WIDTH * .2, REG_HEIGHT * .1))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.id.setStyleSheet('color: black;font-weight:bold;')

        self.password = QtWidgets.QLabel(self.frame)
        self.password.setGeometry(QRect(REG_WIDTH * 0.067, REG_HEIGHT * 0.22,
                                        REG_WIDTH * 0.2, REG_HEIGHT * 0.1))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.password.setStyleSheet('color: black;font-weight:bold;')
        self.password.setFont(font)
        self.password.setObjectName("password")

        default_style = {'border-radius': '10px',
                         'background-color': 'rgba(150,150,150,126)',
                         'font-size': '16px',
                         'font-weight': 'bold',
                         'color': 'black',
                         'font-family': 'Comic Sans MS'}

        self.id_box = QtWidgets.QLineEdit(self.frame)
        self.id_box.setObjectName("id_box")
        self.id_box.setStyleSheet(gen_style(default_style))
        self.id_box.setGeometry(QRect(REG_WIDTH * 0.19, REG_HEIGHT * 0.12,
                                      REG_WIDTH * 0.55, REG_HEIGHT * 0.07))
        self.id_box.setPlaceholderText(" 3~10位，数字或字母")

        self.password_box = QtWidgets.QLineEdit(self.frame)
        self.password_box.setObjectName("password_box")
        self.password_box.setStyleSheet(gen_style(default_style))
        self.password_box.setGeometry(QRect(REG_WIDTH * 0.19, REG_HEIGHT * 0.24,
                                            REG_WIDTH * 0.55, REG_HEIGHT * 0.07))
        self.password_box.setEchoMode(QLineEdit.Password)
        self.password_box.setPlaceholderText(" 6~15位，数字或字母")

        self.register_button = QtWidgets.QPushButton(self.frame)
        self.register_button.setObjectName("register_button")
        self.register_button.setStyleSheet(gen_style(default_style, {'font-weight': 'bold'}))
        self.register_button.setGeometry(QRect(REG_WIDTH * 0.78, REG_HEIGHT * 0.12,
                                                REG_WIDTH * 0.2, REG_HEIGHT * 0.19))

        self.close_button = QtWidgets.QPushButton(self.Form)
        self.close_button.setObjectName("close")
        self.close_button.setStyleSheet("QPushButton{border-image: url('./images/dark_star');}")
        self.close_button.setGeometry(QRect(REG_WIDTH * 0.88, REG_HEIGHT * 0.02,
                                            REG_WIDTH * 0.1, REG_WIDTH * 0.1))
        self.close_button.setCursor(Qt.OpenHandCursor)
        self.close_button.resize(QSize(REG_WIDTH * 0.1, REG_WIDTH * 0.1))

        self.star_label = QtWidgets.QLabel(self.Form)
        self.star_label.setObjectName("star")
        self.star_label.setGeometry(QRect(REG_WIDTH * 0.03, REG_HEIGHT * 0.16,
                                          REG_WIDTH * 0.1, REG_WIDTH * 0.1))
        self.star_label.setPixmap(QPixmap(star_path))
        self.star_label.setScaledContents(True)
        self.star_label.resize(QSize(REG_WIDTH * 0.1, REG_WIDTH * 0.1))

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("border-radius:20px")

        background_palette = QPalette()
        background_pixmap = QPixmap(register_path).scaled(self.width(), self.height())
        background_palette.setBrush(self.backgroundRole(), QBrush(background_pixmap))
        self.setPalette(background_palette)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.id.setText(_translate("Form", "账号"))
        self.password.setText(_translate("Form", "密码"))
        self.register_button.setText(_translate("Form", "注册"))


class RegisterPage(QWidget, Ui_registerWindow):
    CLOSE = QtCore.pyqtSignal()

    def __init__(self, sock, parent=None):
        super(RegisterPage, self).__init__(parent)
        self.setupUi(self)
        self.sock = sock
        self.CLOSE.connect(self.close)

        self.register_button.setCursor(Qt.OpenHandCursor)
        self.register_button.clicked.connect(self.register_anim)
        self.register_button.clicked.connect(self.register)
        self.register_button.clicked.connect(self.id_box.clear)
        self.register_button.clicked.connect(self.password_box.clear)

        self.close_button.clicked.connect(self.CLOSE)

    def register(self):
        username = self.id_box.text()
        password = self.password_box.text()
        send(self.sock, '\r\n'.join([str(REGISTER), username, password]))

    def register_anim(self):
        self.anim = QPropertyAnimation(self.star_label, b'geometry')
        self.anim.setDuration(6000)
        self.anim.setStartValue(QRect(REG_WIDTH * 0.03, REG_HEIGHT * 0.16,
                                      REG_WIDTH * 0.1, REG_WIDTH * 0.1))
        star = [(.15, .19, .09), (.17, .2, .1), (.19, .2, .1), (.3, .27, .13),
                (.32, .26, .12), (.34, .27, 0.13), (.45, .45, .14), (.47, .44, 0.13),
                (.49, .45, .14), (.6, .51, .24), (.62, .5, .23), (.64, .51, .24),
                (.75, .76, .17), (.77, .75, .16), (.79, .76, .17), (.9, .74, .08),
                (.94, .72, .06)]
        for i, pos in enumerate(star):
            if i in [0, 4, 7, 10, 13]:
                scale = .12
            elif i == 18:
                scale = .14
            else:
                scale = .1
            self.anim.setKeyValueAt(pos[0], QRect(REG_WIDTH * pos[1], REG_HEIGHT * pos[2],
                                                  REG_WIDTH * scale, REG_WIDTH * scale))
        self.anim.setEndValue(QRect(REG_WIDTH * 0.03, REG_HEIGHT * 0.16,
                                    REG_WIDTH * 0.1, REG_WIDTH * 0.1))
        self.anim.start()

    '''
    # Oxer:这段有啥用？
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_bigtrigger(qp)
        qp.end()

    def draw_bigtrigger(self, qp):
        pen = QPen(Qt.white, 0.3, Qt.CustomDashLine)
        qp.setPen(pen)
        line = [(.08, .21, .25, .15), (.25, .15, .32, .18), (.32, .18, .5, .19),
                (.5, .19, .56, .29), (.56, .29, .81, .22), (.81, .22, .79, .13)]
        for pos in line:
            qp.drawLine(REG_WIDTH * pos[0], REG_HEIGHT * pos[1],
                        REG_WIDTH * pos[2], REG_HEIGHT * pos[3])
    '''

    '''
    # Oxer:这段有啥用？没用的话我就删了
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
