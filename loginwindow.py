# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class Ui_loginWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(468, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(468, 400))
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self._1_1label_2 = QtWidgets.QLabel(Form)
        self._1_1label_2.setMinimumSize(QtCore.QSize(450, 150))
        self._1_1label_2.setMaximumSize(QtCore.QSize(450, 150))
        self._1_1label_2.setText("")
        self._1_1label_2.setPixmap(QtGui.QPixmap("./images/bittersweet.jpg"))
        self._1_1label_2.setScaledContents(True)
        self._1_1label_2.setObjectName("_1_1label_2")
        self.verticalLayout.addWidget(self._1_1label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(441, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.id = QtWidgets.QLabel(self.frame)
        self.id.setGeometry(QtCore.QRect(40, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.password = QtWidgets.QLabel(self.frame)
        self.password.setGeometry(QtCore.QRect(40, 60, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.id_box = QtWidgets.QLineEdit(self.frame)
        self.id_box.setGeometry(QtCore.QRect(100, 30, 251, 21))
        self.id_box.setObjectName("id_box")
        self.password_box = QtWidgets.QLineEdit(self.frame)
        self.password_box.setGeometry(QtCore.QRect(100, 70, 251, 20))
        self.password_box.setObjectName("password_box")
        self.remember_pw = QtWidgets.QCheckBox(self.frame)
        self.remember_pw.setGeometry(QtCore.QRect(40, 110, 71, 16))
        self.remember_pw.setObjectName("remember_pw")
        self.aotu_login = QtWidgets.QCheckBox(self.frame)
        self.aotu_login.setGeometry(QtCore.QRect(190, 110, 71, 16))
        self.aotu_login.setObjectName("aotu_login")
        self.login_button = QtWidgets.QPushButton(self.frame)
        self.login_button.setGeometry(QtCore.QRect(360, 30, 75, 61))
        self.login_button.setObjectName("login_button")
        self.verticalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.id.setText(_translate("Form", "账号"))
        self.password.setText(_translate("Form", "密码"))
        self.remember_pw.setText(_translate("Form", "记住密码"))
        self.aotu_login.setText(_translate("Form", "自动登录"))
        self.login_button.setText(_translate("Form", "登录"))


class LoginPage(QWidget, Ui_loginWindow):
    CLOSE = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(LoginPage, self).__init__(parent)
        self.setupUi(self)
        self.CLOSE.connect(self.close)


class Ui_chatWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(583, 473)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setMaximumSize(QtCore.QSize(160, 16777215))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 70))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 70))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "ENTER"))


class ChatPage(QWidget, Ui_chatWindow):
    APPEND = QtCore.pyqtSignal(str)
    ask_users = QtCore.pyqtSignal(str)
    SHOW = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(ChatPage, self).__init__(parent)
        self.setupUi(self)
        self.ask_users.connect(self.changeText)
        self.SHOW.connect(self.show)
        self.APPEND.connect(self.textBrowser_2.append)

    def changeText(self, data):
        self.textBrowser.setPlainText(data)
