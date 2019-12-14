from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from Constant import *
from util import *


GROUP_HEIGHT = 300
GROUP_WIDTH = 425

default_style = {'border-radius': '10px',
                 'background-color': 'rgba(255,255,255,126)',
                 'font-size': '16px',
                 'font-weight': 'bold',
                 'color': 'black',
                 'font-family': 'Comic Sans MS'}


class Ui_newgroupWindow(object):

	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(GROUP_WIDTH, GROUP_HEIGHT)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
		Form.setSizePolicy(sizePolicy)
		Form.setFixedSize(QtCore.QSize(GROUP_WIDTH, GROUP_HEIGHT))
		Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		Form.setContentsMargins(0, 0, 0, 0)
		self.Form = Form

		self.header = QtWidgets.QLabel(Form)
		self.header.setMinimumSize(QtCore.QSize(GROUP_WIDTH, GROUP_HEIGHT * 0.4))
		self.header.setMaximumSize(QtCore.QSize(GROUP_WIDTH, GROUP_HEIGHT * 0.4))
		self.header.setText("")

		self.header.setStyleSheet('background-color:rgba(255,255,255,40)')
		self.header.setScaledContents(True)
		self.header.setObjectName("header")
		self.header.setGeometry(QRect(0, 0, GROUP_WIDTH, GROUP_HEIGHT * 0.4))
		
		self.frame = QtWidgets.QFrame(Form)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
		self.frame.setSizePolicy(sizePolicy)
		self.frame.setFixedSize(QtCore.QSize(GROUP_WIDTH, GROUP_HEIGHT * 0.6))
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.frame.setGeometry(QRect(0, GROUP_HEIGHT/3,
									 GROUP_WIDTH, GROUP_HEIGHT *0.6))

		self.groupid_box = QtWidgets.QLineEdit(self.frame)
		self.groupid_box.setGeometry(QtCore.QRect(GROUP_WIDTH * 0.19, GROUP_HEIGHT * 0.12,
												  GROUP_WIDTH * 0.57, GROUP_HEIGHT * 0.40))
		self.groupid_box.setObjectName("id_box")
		self.groupid_box.setStyleSheet(gen_style(default_style, {'font-size': '96px'}))

		self.star_label = QtWidgets.QLabel(self.Form)
		self.star_label.setPixmap(QPixmap(star_path))
		self.star_label.setScaledContents(True)
		self.star_label.setObjectName("star")
		self.star_label.resize(QSize(GROUP_WIDTH * 0.1, GROUP_WIDTH * 0.1))
		self.star_label.setGeometry(QRect(GROUP_WIDTH * 0.03, GROUP_HEIGHT * 0.16,
										  GROUP_WIDTH * 0.1, GROUP_WIDTH * 0.1))
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setStyleSheet("border-radius:20px")

		self.close_button = QtWidgets.QPushButton(self.Form)
		self.close_button.setStyleSheet("QPushButton{border-image: url('./images/dark_star');}")
		self.close_button.setCursor(Qt.OpenHandCursor)
		self.close_button.setObjectName("close")
		self.close_button.resize(QSize(GROUP_WIDTH * 0.1, GROUP_WIDTH * 0.1))
		self.close_button.setGeometry(QRect(GROUP_WIDTH * 0.88, GROUP_HEIGHT * 0.02,
											GROUP_WIDTH * 0.1, GROUP_WIDTH * 0.1))

		self.createNewGroup_button = QtWidgets.QPushButton(self.frame)
		self.createNewGroup_button.setGeometry(QtCore.QRect(GROUP_WIDTH * 0.78, GROUP_HEIGHT * 0.32,
															GROUP_WIDTH * 0.2, GROUP_HEIGHT * 0.19))
		self.createNewGroup_button.setObjectName("createNewGroup_button")
		self.createNewGroup_button.setStyleSheet(gen_style(default_style, {'font-weight': '20px'}))

		background_palette = QPalette()
		background_pixmap = QPixmap(newgroup_path).scaled(self.width(), self.height())
		background_palette.setBrush(self.backgroundRole(), QBrush(background_pixmap))
		self.setPalette(background_palette)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.createNewGroup_button.setText(_translate("Form", "Enter \nGroup!"))


class NewGroupPage(QWidget, Ui_newgroupWindow):
	CLOSE = QtCore.pyqtSignal()

	def __init__(self, sock, parent=None):
		super(NewGroupPage, self).__init__(parent)
		self.setupUi(self)  # 可以在外部调用这个createNewGroupPage的CLOSE信号
		self.sock = sock
		self.CLOSE.connect(self.close)

		self.createNewGroup_button.clicked.connect(self.createNewGroup_anim)
		self.createNewGroup_button.setCursor(Qt.OpenHandCursor)

		self.close_button.clicked.connect(self.CLOSE)

		self.createNewGroup_button.clicked.connect(self.createNewGroup)
		self.createNewGroup_button.clicked.connect(self.groupid_box.clear)
		self.flag = 0  # 测试
		self.groupid = ''

	def createNewGroup(self):
		self.groupid = 'gp_' + self.groupid_box.text()
		# self.owner.new_group(self.groupid)
		self.CLOSE.emit()
		send(self.sock, '\r\n'.join([str(NEWGROUP), self.groupid]))

	def createNewGroup_anim(self):
		self.anim = QPropertyAnimation(self.star_label, b'geometry')
		self.anim.setDuration(6000)
		self.anim.setStartValue(QRect(GROUP_WIDTH * 0.03, GROUP_HEIGHT * 0.16,
									  GROUP_WIDTH * 0.1, GROUP_WIDTH * 0.1))
		star = [(.15, .19, .09), (.17, .2, .1), (.19, .2, .1), (.3, .27, .13),
				(.32, .26, .12), (.34, .27, .13), (.45, .45, .14), (.47, .44, .13),
				(.49, .45, .14), (.6, .51, .24), (.62, .5, .23), (.64, .51, .24),
				(.75, .76, .17), (.77, .75, .16), (.79, .76, .17), (.9, .74, .08),
				(.94, .72, .06)]
		for i, pos in enumerate(star):
			if i in [0, 4, 7, 10, 13]: scale = .12
			elif i == 18: scale = .14
			else: scale = .1
			self.anim.setKeyValueAt(pos[0], QRect(GROUP_WIDTH * pos[1], GROUP_HEIGHT * pos[2],
												  GROUP_WIDTH * scale, GROUP_WIDTH * scale))
		self.anim.setEndValue(QRect(GROUP_WIDTH * 0.03, GROUP_HEIGHT * 0.16, GROUP_WIDTH * 0.1, GROUP_WIDTH * 0.1))
		self.anim.start()

	'''
	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.draw_bigtrigger(qp)
		qp.end()

	def draw_bigtrigger(self,qp):
		pen = QPen(Qt.white, 0.3, Qt.CustomDashLine)
		qp.setPen(pen)
		qp.drawLine(GROUP_WIDTH * 0.08, GROUP_HEIGHT * 0.21,GROUP_WIDTH * 0.25, GROUP_HEIGHT * 0.15)
		qp.drawLine(GROUP_WIDTH * 0.25, GROUP_HEIGHT * 0.15,GROUP_WIDTH * 0.32, GROUP_HEIGHT * 0.18)
		qp.drawLine(GROUP_WIDTH * 0.32, GROUP_HEIGHT * 0.18, GROUP_WIDTH * 0.5, GROUP_HEIGHT * 0.19)
		qp.drawLine(GROUP_WIDTH * 0.5, GROUP_HEIGHT * 0.19, GROUP_WIDTH * 0.56, GROUP_HEIGHT * 0.29)
		qp.drawLine(GROUP_WIDTH * 0.56, GROUP_HEIGHT * 0.29, GROUP_WIDTH * 0.81, GROUP_HEIGHT * 0.22)
		qp.drawLine(GROUP_WIDTH * 0.81, GROUP_HEIGHT * 0.22, GROUP_WIDTH * 0.79, GROUP_HEIGHT * 0.13)
		

		#self.frame.setStyleSheet("background-image:url('./images/star.jpg') ")

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