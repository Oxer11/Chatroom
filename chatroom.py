from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMessageBox
from loginwindow import *
import sys
from socket import *
import threading


def run():
	app = QtWidgets.QApplication(sys.argv)
	widget = QtWidgets.QWidget()
	ui = Ui_loginWindow()
	ui.setupUi(widget) # 这个函数将widget绑定到ui对象上
	widget.show() # 这个用了才能展示界面

	sys.exit(app.exec_()) #没有这个的话就会直接结束 


if __name__ == '__main__':
	
	run()

