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
from register_win import RegisterPage
import cgitb


LOG_HEIGHT = 300
LOG_WIDTH = 425
cgitb.enable(format='text')


class Ui_loginWindow(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(LOG_WIDTH, LOG_HEIGHT)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setFixedSize(QtCore.QSize(LOG_WIDTH, LOG_HEIGHT))
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setContentsMargins(0, 0, 0, 0)
        self.Form = Form

        self.header = QtWidgets.QLabel(Form)
        self.header.setMinimumSize(QtCore.QSize(LOG_WIDTH, LOG_HEIGHT * 0.4))
        self.header.setMaximumSize(QtCore.QSize(LOG_WIDTH, LOG_HEIGHT * 0.4))
        self.header.setText("")
        self.header.setStyleSheet('background-color:rgba(255,255,255,40)')
        self.header.setScaledContents(True)
        self.header.setObjectName("header")
        self.header.setGeometry(QRect(0,0,LOG_WIDTH, LOG_HEIGHT * 0.4))

        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFixedSize(QtCore.QSize(LOG_WIDTH, LOG_HEIGHT * 0.6))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(0,LOG_HEIGHT/3,LOG_WIDTH,LOG_HEIGHT *0.6))

        self.id = QtWidgets.QLabel(self.frame)
        self.id.setGeometry(QtCore.QRect(LOG_WIDTH / 15, LOG_HEIGHT * 0.1, LOG_WIDTH/5, LOG_HEIGHT/10))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.id.setStyleSheet('color: white;font-weight:bold;')

        self.password = QtWidgets.QLabel(self.frame)
        self.password.setGeometry(QRect(LOG_WIDTH * .067, LOG_HEIGHT * .22,
                                        LOG_WIDTH * .2, LOG_HEIGHT * .1))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.password.setStyleSheet('color: white;font-weight:bold;')
        self.password.setFont(font)
        self.password.setObjectName("password")

        default_style = {'border-radius': '10px',
                         'background-color': 'rgba(0,0,0,126)',
                         'font-size': '16px',
                         'font-weight': 'bold',
                         'color': 'white',
                         'font-family': 'Comic Sans MS'}


        self.id_box = QtWidgets.QLineEdit(self.frame)
        self.id_box.setObjectName("id_box")
        self.id_box.setStyleSheet(gen_style(default_style))
        self.id_box.setGeometry(QRect(LOG_WIDTH * .19, LOG_HEIGHT * .12,
                                      LOG_WIDTH * .55, LOG_HEIGHT * .07))

        self.password_box = QtWidgets.QLineEdit(self.frame)
        self.password_box.setObjectName("password_box")
        self.password_box.setStyleSheet(gen_style(default_style))
        self.password_box.setGeometry(QRect(LOG_WIDTH * .19, LOG_HEIGHT * .24,
                                            LOG_WIDTH * .55, LOG_HEIGHT * .07))
        self.password_box.setEchoMode(QLineEdit.Password)

        self.login_button = QtWidgets.QPushButton(self.frame)
        self.login_button.setObjectName("login_button")
        self.login_button.setStyleSheet(gen_style(default_style))
        self.login_button.setGeometry(QRect(LOG_WIDTH * .78, LOG_HEIGHT * .12,
                                            LOG_WIDTH * .2, LOG_HEIGHT * .19))

        self.register_button = QtWidgets.QPushButton(self.frame)
        self.register_button.setObjectName("register_button")
        self.register_button.setStyleSheet(gen_style(default_style))
        self.register_button.setGeometry(QRect(LOG_WIDTH * .78, LOG_HEIGHT * .46,
                                               LOG_WIDTH * .16, LOG_HEIGHT * .08))

        self.star_label = QtWidgets.QLabel(self.Form)
        self.star_label.setObjectName("star")
        self.star_label.setGeometry(QRect(LOG_WIDTH * 0.03, LOG_HEIGHT * 0.16,
                                          LOG_WIDTH * 0.1, LOG_WIDTH * 0.1))
        self.star_label.setPixmap(QPixmap(star_path))
        self.star_label.setScaledContents(True)
        self.star_label.resize(QSize(LOG_WIDTH * 0.1, LOG_WIDTH * 0.1))

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("border-radius:20px")

        self.close_button = QtWidgets.QPushButton(self.Form)
        self.close_button.setObjectName("close")
        self.close_button.setStyleSheet("QPushButton{border-image: url('./images/dark_star');}")
        self.close_button.setGeometry(QRect(LOG_WIDTH * 0.88, LOG_HEIGHT * 0.02,
                                            LOG_WIDTH * 0.1, LOG_WIDTH * 0.1))
        self.close_button.setCursor(Qt.OpenHandCursor)
        self.close_button.resize(QSize(LOG_WIDTH * 0.1, LOG_WIDTH * 0.1))

        background_palette = QPalette()
        background_pixmap = QPixmap(background_path).scaled(self.width(), self.height())
        background_palette.setBrush(self.backgroundRole(), QBrush(background_pixmap))
        self.setPalette(background_palette)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.id.setText(_translate("Form", "账号"))
        self.password.setText(_translate("Form", "密码"))
        self.login_button.setText(_translate("Form", "登录"))
        self.register_button.setText(_translate("Form", "注册"))


class LoginPage(QWidget, Ui_loginWindow):
    CLOSE = QtCore.pyqtSignal()
    ERROR = QtCore.pyqtSignal(str)

    def __init__(self, sock, parent=None):
        super(LoginPage, self).__init__(parent)
        self.setupUi(self)

        self.sock = sock
        self.ui_register = RegisterPage(self.sock)

        self.ERROR.connect(self.error_msg)

        self.CLOSE.connect(self.close)
        self.CLOSE.connect(self.ui_register.close)

        self.login_button.setCursor(Qt.OpenHandCursor)
        self.login_button.clicked.connect(self.login_anim)
        self.login_button.clicked.connect(self.log_in)
        self.login_button.clicked.connect(self.id_box.clear)
        self.login_button.clicked.connect(self.password_box.clear)

        self.register_button.setCursor(Qt.OpenHandCursor)
        self.register_button.clicked.connect(self.show_registerWindow)

        self.close_button.clicked.connect(self.CLOSE)

    def error_msg(self, msg):
        QMessageBox.warning(self, 'warning', msg)

    def log_in(self):
        username = self.id_box.text()
        password = self.password_box.text()
        self.clientId = username
        send(self.sock, '\r\n'.join([str(LOGIN), username, password]))

    def show_registerWindow(self):
        self.ui_register.show()

    def login_anim(self):
        self.anim = QPropertyAnimation(self.star_label, b'geometry')
        self.anim.setDuration(6000)
        self.anim.setStartValue(QRect(LOG_WIDTH * 0.03, LOG_HEIGHT * 0.16,
                                      LOG_WIDTH * 0.1, LOG_WIDTH * 0.1))
        star = [(.15, .19, .09), (.17, .2, .1), (.19, .2, .1), (.3, .27, .13),
                (.32, .26, .12), (.34, .27, .13), (.45, .45, .14), (.47, .44, .13),
                (.49, .45, .14), (.6, .51, .24), (.62, .5, .23), (.64, .51, .24),
                (.75, .76, .17), (.77, .75, .16), (.79, .76, .17), (.9, .74, .08),
                (.94, .72, .06)]
        for i, pos in enumerate(star):
            if i in [0, 4, 7, 10, 13]: scale = .12
            elif i == 18: scale = .14
            else: scale = .1
            self.anim.setKeyValueAt(pos[0], QRect(LOG_WIDTH * pos[1], LOG_HEIGHT * pos[2],
                                                  LOG_WIDTH * scale, LOG_WIDTH * scale))
        self.anim.setEndValue(QRect(LOG_WIDTH * 0.03, LOG_HEIGHT * 0.16,
                                    LOG_WIDTH * 0.1, LOG_WIDTH * 0.1))
        self.anim.start()

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
            qp.drawLine(LOG_WIDTH * pos[0], LOG_HEIGHT * pos[1],
                        LOG_WIDTH * pos[2], LOG_HEIGHT * pos[3])

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
