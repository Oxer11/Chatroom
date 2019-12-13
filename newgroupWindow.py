from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from Constant import *
from util import *
import cgitb



class Ui_newgroupWindow(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(newgroup_width, newgroup_height)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
		Form.setSizePolicy(sizePolicy)
		Form.setFixedSize(QtCore.QSize(newgroup_width, newgroup_height))
		Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		Form.setContentsMargins(0,0,0,0)
		self.Form = Form

		self.header = QtWidgets.QLabel(Form)
		self.header.setMinimumSize(QtCore.QSize(newgroup_width, newgroup_height * 0.4))
		self.header.setMaximumSize(QtCore.QSize(newgroup_width, newgroup_height * 0.4))
		self.header.setText("")

		self.header.setStyleSheet('background-color:rgba(255,255,255,40)')
		self.header.setScaledContents(True)
		self.header.setObjectName("header")
		self.header.setGeometry(QRect(0,0,newgroup_width, newgroup_height * 0.4))

		
		self.frame = QtWidgets.QFrame(Form)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
		self.frame.setSizePolicy(sizePolicy)
		self.frame.setFixedSize(QtCore.QSize(newgroup_width, newgroup_height * 0.6))
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.frame.setGeometry(QRect(0,newgroup_height/3,newgroup_width,newgroup_height *0.6))
		#self.groupid = QtWidgets.QLabel(self.frame)
		#self.groupid.setGeometry(QtCore.QRect(newgroup_width / 15, newgroup_height * 0.1, newgroup_width/5, newgroup_height/10))
		font = QtGui.QFont()
		font.setFamily("微软雅黑 Light")
		font.setPointSize(16)
		#self.groupid.setFont(font)
		#self.groupid.setObjectName("id")
		#self.groupid.setStyleSheet('color: #FFFFFF;font-weight:24;')
		self.password = QtWidgets.QLabel(self.frame)
		self.password.setGeometry(QtCore.QRect(newgroup_width / 15, newgroup_height * ( 2.2/10) , newgroup_width/5, newgroup_height/10))
		font = QtGui.QFont()
		font.setFamily("微软雅黑 Light")
		font.setPointSize(16)
		'''
		self.password.setStyleSheet('color: #FFFFFF;font-weight:24;')
		self.password.setFont(font)
		self.password.setObjectName("password")
		'''
		self.groupid_box = QtWidgets.QLineEdit(self.frame)
		self.groupid_box.setGeometry(QtCore.QRect(newgroup_width * 0.19, newgroup_height * 0.12, newgroup_width * 0.57, newgroup_height * 0.40))
		self.groupid_box.setObjectName("id_box")
		self.groupid_box.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,126);font-size:96px;font-weight:bold;color:white;font-family:Comic Sans MS;")
		'''
		self.password_box = QtWidgets.QLineEdit(self.frame)
		self.password_box.setGeometry(QtCore.QRect(newgroup_width * 0.19, newgroup_height*0.24, newgroup_width * 0.55, newgroup_height * 0.07))
		self.password_box.setObjectName("password_box")
		self.password_box.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,126);font-size:16px;font-weight:bold;color:white;font-family:Comic Sans MS;")
		'''

		self.createNewGroup_button = QtWidgets.QPushButton(self.frame)
		self.createNewGroup_button.setGeometry(QtCore.QRect(newgroup_width * 0.78, newgroup_height * 0.32, newgroup_width * 0.2, newgroup_height * 0.19))
		self.createNewGroup_button.setObjectName("createNewGroup_button")
		self.createNewGroup_button.setStyleSheet("border-radius:10px;font-family:Comic Sans MS;font-size:16px;color:white;font-weight:20px;background-color:rgba(255,255,255,126)")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		#self.groupid.setText(_translate("Form", "组号"))
		#self.password.setText(_translate("Form", "密码"))
		self.createNewGroup_button.setText(_translate("Form", "Enter \nGroup!"))

class NewGroupPage(QWidget, Ui_newgroupWindow):
	CLOSE = QtCore.pyqtSignal()

	def __init__(self, sock, parent=None):
		super(NewGroupPage, self).__init__(parent)
		self.setupUi(self)  # 可以在外部调用这个createNewGroupPage的CLOSE信号
		self.sock = sock
		self.CLOSE.connect(self.close)
		background_palette = QPalette()
		background_pixmap = QPixmap(newgroup_path).scaled(self.width(),self.height())
		background_palette.setBrush(self.backgroundRole(),QBrush(background_pixmap))
		self.setPalette(background_palette)
		self.createNewGroup_button.clicked.connect(self.createNewGroup_anim)
		self.createNewGroup_button.setCursor(Qt.OpenHandCursor)
		self.star_label = QtWidgets.QLabel(self.Form)
		self.star_label.setPixmap(QPixmap(star_path))
		self.star_label.setScaledContents(True)
		self.star_label.setObjectName("star")
		self.star_label.resize(QSize(newgroup_width * 0.1,newgroup_width * 0.1))
		self.star_label.setGeometry(QRect(newgroup_width * 0.03, newgroup_height * 0.16, newgroup_width * 0.1, newgroup_width * 0.1))
		#self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setStyleSheet("border-radius:20px")
		self.close_button = QtWidgets.QPushButton(self.Form)
		self.close_button.setStyleSheet("QPushButton{border-image: url('./images/dark_star');}")
		self.close_button.setCursor(Qt.OpenHandCursor)
		self.close_button.setObjectName("close")
		self.close_button.resize(QSize(newgroup_width * 0.1,newgroup_width * 0.1))
		self.close_button.setGeometry(QRect(newgroup_width * 0.88, newgroup_height * 0.02, newgroup_width * 0.1, newgroup_width * 0.1))
		self.close_button.clicked.connect(self.CLOSE)

		self.createNewGroup_button.clicked.connect(self.createNewGroup)
		self.createNewGroup_button.clicked.connect(self.groupid_box.clear)
		self.flag = 0 # 测试
		self.groupid = ''
		#self.createNewGroup_button.clicked.connect(self.password_box.clear)

	def createNewGroup(self):
		self.groupid = 'gp_'+self.groupid_box.text()
		self.owner.new_group(self.groupid)
		self.CLOSE.emit()
		#send(self.sock, '\r\n'.join([str(createNewGroup), username, password]))  # 发送注册信息

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.draw_bigtrigger(qp)
		qp.end()

	def draw_bigtrigger(self,qp):
		pen = QPen(Qt.white, 0.3, Qt.CustomDashLine)
		qp.setPen(pen)
		qp.drawLine(newgroup_width * 0.08, newgroup_height * 0.21,newgroup_width * 0.25, newgroup_height * 0.15)
		qp.drawLine(newgroup_width * 0.25, newgroup_height * 0.15,newgroup_width * 0.32, newgroup_height * 0.18)
		qp.drawLine(newgroup_width * 0.32, newgroup_height * 0.18, newgroup_width * 0.5, newgroup_height * 0.19)
		qp.drawLine(newgroup_width * 0.5, newgroup_height * 0.19, newgroup_width * 0.56, newgroup_height * 0.29)
		qp.drawLine(newgroup_width * 0.56, newgroup_height * 0.29, newgroup_width * 0.81, newgroup_height * 0.22)
		qp.drawLine(newgroup_width * 0.81, newgroup_height * 0.22, newgroup_width * 0.79, newgroup_height * 0.13)
		

		#self.frame.setStyleSheet("background-image:url('./images/star.jpg') ")
	def createNewGroup_anim(self):
		
		self.anim = QPropertyAnimation(self.star_label, b'geometry')
		self.anim.setDuration(6000)
		self.anim.setStartValue(QRect(newgroup_width * 0.03, newgroup_height * 0.16, newgroup_width * 0.1, newgroup_width * 0.1))
		self.anim.setKeyValueAt(0.15,QRect(newgroup_width * 0.19, newgroup_height * 0.09, newgroup_width * 0.12, newgroup_width * 0.12))
		self.anim.setKeyValueAt(0.17,QRect(newgroup_width * 0.2, newgroup_height * 0.1, newgroup_width * 0.1, newgroup_width * 0.1))
		self.anim.setKeyValueAt(0.19,QRect(newgroup_width * 0.2, newgroup_height * 0.1, newgroup_width * 0.1, newgroup_width * 0.1))
		self.anim.setKeyValueAt(0.3,QRect(newgroup_width * 0.27, newgroup_height * 0.13, newgroup_width * 0.1, newgroup_width * 0.1))
		self.anim.setKeyValueAt(0.32,QRect(newgroup_width * 0.26, newgroup_height * 0.12, newgroup_width * 0.12, newgroup_width * 0.12))
		self.anim.setKeyValueAt(0.34,QRect(newgroup_width * 0.27, newgroup_height * 0.13, newgroup_width * 0.1, newgroup_width * 0.1))
		self.anim.setKeyValueAt(0.45,QRect(newgroup_width * 0.45, newgroup_height * 0.14, newgroup_width * 0.1, newgroup_width * 0.1))
		self.anim.setKeyValueAt(0.47,QRect(newgroup_width * 0.44, newgroup_height * 0.13, newgroup_width * 0.12, newgroup_width * 0.12))
		self.anim.setKeyValueAt(0.49,QRect(newgroup_width * 0.45, newgroup_height * 0.14, newgroup_width * 0.1, newgroup_width * 0.1))
		self.anim.setKeyValueAt(0.6,QRect(newgroup_width * 0.51, newgroup_height * 0.24, newgroup_width * 0.1, newgroup_width * 0.1))
		self.anim.setKeyValueAt(0.62,QRect(newgroup_width * 0.50, newgroup_height * 0.23, newgroup_width * 0.12, newgroup_width * 0.12))
		self.anim.setKeyValueAt(0.64,QRect(newgroup_width * 0.51, newgroup_height * 0.24, newgroup_width * 0.1, newgroup_width * 0.1))
		self.anim.setKeyValueAt(0.75,QRect(newgroup_width * 0.76, newgroup_height * 0.17, newgroup_width * 0.1, newgroup_width * 0.1))
		self.anim.setKeyValueAt(0.77,QRect(newgroup_width * 0.75, newgroup_height * 0.16, newgroup_width * 0.12, newgroup_width * 0.12))
		self.anim.setKeyValueAt(0.79,QRect(newgroup_width * 0.76, newgroup_height * 0.17, newgroup_width * 0.1, newgroup_width * 0.1))
		self.anim.setKeyValueAt(0.9,QRect(newgroup_width * 0.74, newgroup_height * 0.08, newgroup_width * 0.1, newgroup_width * 0.1))
		self.anim.setKeyValueAt(0.94,QRect(newgroup_width * 0.72, newgroup_height * 0.06, newgroup_width * 0.14, newgroup_width * 0.14))
		self.anim.setEndValue(QRect(newgroup_width * 0.03, newgroup_height * 0.16, newgroup_width * 0.1, newgroup_width * 0.1))
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