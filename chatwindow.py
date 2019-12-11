from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtGui import *
from newgroupWindow import *
from util import *
import cgitb

chat_height = 646
chat_width = 913
# background_path = "./images/star.jpg"
photo_base_path = "./images/photo/"
tiancao_path = "./images/tiancao.png"
star_path = "./images/little_star.png"
darkstar_path = "./images/dark_star.png"
cgitb.enable(format = 'text')
chatbar_path = "./images/hanabi.png"
chatboard_path = "./images/hanabi_colorful.jpg"
kyogre_path = "./images/kyogre-primal.png"
filepage_path = darkstar_path
max_userlist = 10
max_chatlist = 10
max_filelist = 10
groupicon_path = "./images/right2.jpg"


'''
class Ui_chatBar(QFrame):
    def __init__(self,parent = None):
        super().__init__(parent)

    def setupUi(self,width,height):
        self.resize(width,height)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frame")
        self.setStyleSheet("background-color:rgba(25,255,255,0);")
        background_palette = QPalette()
        background_pixmap = QPixmap(chatbar_path).scaled(self.width(),self.height())
        background_palette.setBrush(self.backgroundRole(), QBrush(background_pixmap))
        self.setPalette(background_palette)
'''

class Ui_chatWindow(object):

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(chat_width, chat_height)

        width = self.width()
        height = self.height()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        self.Form = Form

        self.chatBar = QtWidgets.QFrame(Form)
        sizePolicy.setHeightForWidth(self.chatBar.sizePolicy().hasHeightForWidth())
        self.chatBar.setSizePolicy(sizePolicy)
        self.chatBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chatBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chatBar.setObjectName("frame")
        self.chatBar.setGeometry(QRect(0, 0, width * 0.27, height))

        self.chatBarPic = QtWidgets.QLabel(Form)
        self.chatBarPic.setGeometry(QRect(0, 0, width * 0.27, height))
        self.chatBarPic.setObjectName('charBarPic')
        self.chatBarPic.setScaledContents(True)
        self.chatBarPic.setPixmap(QtGui.QPixmap(chatbar_path))

        self.chatBoardPic = QtWidgets.QLabel(Form)
        self.chatBoardPic.setGeometry(QRect(width * 0.27, 0, width * 0.73, height))
        self.chatBoardPic.setObjectName('charBoardPic')
        self.chatBoardPic.setScaledContents(True)
        self.chatBoardPic.setPixmap(QtGui.QPixmap(chatboard_path))

        opaque = 210
        self.opaque = opaque

        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)  # 这个是聊天的
        self.textBrowser_2.setObjectName("conversation_0")
        self.textBrowser_2.setStyleSheet("border-radius:10px;background-color:rgba(126,126,126,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        self.textBrowser_2.setGeometry(QRect(width * 0.3, height * 0.03, width * 0.5, height * 0.75))
        # self.gridLayout.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        # self.textBrowser.setMaximumSize(QtCore.QSize(160, 16777215))
        self.textBrowser.setGeometry(QRect(width * 0.83, height * 0.03, width * 0.15, height * 0.75))
        self.textBrowser.setStyleSheet("border-radius:10px;background-color:rgba(126,126,126,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        self.textBrowser.setObjectName("conversation_rightbar_0")
        # self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QRect(width * 0.3, height * 0.8, width * 0.5, height * 0.18))
        self.textEdit.setStyleSheet("border-radius:10px;background-color:rgba(126,126,126,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        # self.textEdit.setMaximumSize(QtCore.QSize(16777215, 70))
        self.textEdit.setObjectName("conversation_input_0")

        _translate = QtCore.QCoreApplication.translate

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QRect(width * 0.83, height * 0.84, width * 0.15, height * 0.14))
        self.pushButton.setStyleSheet("border-radius:10px;background-color:rgba(126,126,126,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        self.pushButton.setObjectName("conversation_pushButton_0")
        self.pushButton.setCursor(Qt.OpenHandCursor)
        self.pushButton.setText(_translate("Form", "ENTER"))  # 调试

        self.newgroupButton = QtWidgets.QPushButton(Form)
        self.newgroupButton.setGeometry(QRect(width * 0.01, height * 0.91, width * 0.25, height * 0.07))
        self.newgroupButton.setStyleSheet("border-radius:10px;background-color:rgba(126,126,126,{0});\
                    font-size:16px;font-weight:bold;color:white;font-family:Comic Sans MS;".format(opaque))
        self.newgroupButton.setObjectName("conversation_pushButton_0")
        self.newgroupButton.setCursor(Qt.OpenHandCursor)
        self.newgroupButton.setText(_translate("Form", "New Group"))
        

        self.uploadButton = QtWidgets.QPushButton(Form)
        self.uploadButton.setGeometry(QRect(width * 0.83, height * 0.80, width * 0.15, height * 0.03))
        self.uploadButton.setStyleSheet("border-radius:6px;background-color:rgba(126,126,126,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        self.uploadButton.setObjectName("conversation_uploadButton_0")
        self.uploadButton.setCursor(Qt.OpenHandCursor)
        self.uploadButton.setText(_translate("Form", "UPLOAD FILE"))

        self.leftButton = QtWidgets.QPushButton(Form)
        self.leftButton.setGeometry(QRect(width * 0.85, height * 0.75, width * 0.05, height * 0.02))
        self.leftButton.setStyleSheet("border-radius:10px;background-color:rgba(126,126,126,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(0))
        self.leftButton.setObjectName("conversation_leftButton_0")
        self.leftButton.setCursor(Qt.OpenHandCursor)
        self.leftButton.setText(_translate("Form", "<-<-"))  # 调试

        self.rightButton = QtWidgets.QPushButton(Form)
        self.rightButton.setGeometry(QRect(width * 0.92, height * 0.75, width * 0.05, height * 0.02))
        self.rightButton.setStyleSheet("border-radius:10px;background-color:rgba(126,126,126,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(0))

                    #border-image: url('./images/right2.jpg')
        self.rightButton.setObjectName("conversation_rightButton_0")
        self.rightButton.setCursor(Qt.OpenHandCursor)
        self.rightButton.setText(_translate("Form", "->->"))  # 调试

        QtCore.QMetaObject.connectSlotsByName(Form)

        self.create_userlist_label()
        self.create_chatlist_label()
        self.create_file_list()
        
        Form.setWindowTitle(_translate("Form", "Form"))

        '''
        sizePolicy = self.sizePolicy() #QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

        #print('line 151 ',self.sizePolicy())

    def heightForWidth(self, width):
        #print('line 151')
        return width / chat_width * chat_height
        '''
    def create_userlist_label(self):
        _translate = QtCore.QCoreApplication.translate
        opaque = self.opaque
        width = self.width()
        height = self.height()
        self.userlist = []
        for i in range(max_userlist):
            icon_button = QtWidgets.QPushButton(self.Form)
            icon_button.setStyleSheet("QPushButton{border-radius:10px;border-image: url('./images/dark_star');}")
            icon_button.setCursor(Qt.OpenHandCursor)
            icon_button.setObjectName("user_icon_{0}".format(i))
            icon_button.setGeometry(QRect(width * 0.845, height * (0.04 + i * width/height * 0.05 ), width * 0.045, width * 0.045))
            icon_button.hide()
            userid_button = QtWidgets.QPushButton(self.Form)
            userid_button.setText(_translate("Form", str(i)))
            userid_button.setCursor(Qt.OpenHandCursor)
            userid_button.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});\
                        font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
            userid_button.setObjectName("user_userid_{0}".format(i))
            userid_button.setGeometry(QRect(width * 0.89, height * (0.05 + i * width/height * 0.05), width * 0.08, width * 0.03))
            userid_button.hide()
            self.userlist.append(['', icon_button, userid_button])
            # 0是username的字符串 1是头像 2是username的button

    def create_chatlist_label(self):
        _translate = QtCore.QCoreApplication.translate
        opaque = self.opaque
        width = self.width()
        height = self.height()
        self.chatlist = []
        for i in range(max_chatlist):
            icon_button = QtWidgets.QPushButton(self.Form)
            icon_button.setStyleSheet("QPushButton{border-radius:10px;border-image: url('./images/dark_star');}")
            icon_button.setCursor(Qt.OpenHandCursor)
            icon_button.setObjectName("chat_icon_{0}".format(i))
            icon_button.setGeometry(QRect(width * 0.015, height * (0.035 + i * width/height * 0.06 ), width * 0.06, width * 0.06))

            userid_button = QtWidgets.QPushButton(self.Form)
            userid_button.setText(_translate("Form", 'default'))
            userid_button.setCursor(Qt.OpenHandCursor)
            userid_button.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});\
                        font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
            userid_button.setObjectName("chat_userid_{0}".format(i))
            userid_button.setGeometry(QRect(width * 0.08, height * (0.05 + i * width/height * 0.06), width * 0.18, width * 0.045))

            nummessage_label = QtWidgets.QLabel(self.Form)
            nummessage_label.setGeometry(QRect(width * 0.23, height * (0.063 + i * width/height * 0.06), width * 0.03, width * 0.03))
            nummessage_label.setStyleSheet("border-radius:10px;background-color:rgba(0,0,0,{0});\
                        font-size:12px;font-weight:bold;color:white;font-family:Comic Sans MS;".format(opaque))
            nummessage_label.setObjectName('chat_nummessage_{0}'.format(i))
            nummessage_label.setText(_translate("Form", ' 0'))

            close_button = QtWidgets.QPushButton(self.Form)
            close_button.setText(_translate("Form", 'X'))
            close_button.setCursor(Qt.OpenHandCursor)
            close_button.setStyleSheet("border-radius:10px;background-color:rgba(0,0,0,{0});\
                        font-size:16px;font-weight:bold;color:white;font-family:Comic Sans MS;".format(opaque))
            close_button.setObjectName("chat_close_{0}".format(i)) 
            close_button.setGeometry(QRect(width * 0.09, height * (0.06 + i * width/height * 0.06), width * 0.03, width * 0.03))

            icon_button.hide()
            userid_button.hide()
            nummessage_label.hide()
            close_button.hide()
            self.chatlist.append([[], icon_button, userid_button, nummessage_label, close_button])
            # 0是username的字符串 1是头像 2是username的button 3是消息数量的button
    
    def create_file_list(self):
        _translate = QtCore.QCoreApplication.translate
        opaque = self.opaque
        width = self.width()
        height = self.height()
        self.file_list = []
        for i in range(max_filelist):
            icon_button = QtWidgets.QPushButton(self.Form)
            icon_button.setStyleSheet("QPushButton{border-radius:10px;border-image: url('./images/dark_star');}")
            icon_button.setCursor(Qt.OpenHandCursor)
            icon_button.setObjectName("file_icon_{0}".format(i))
            icon_button.setGeometry(QRect(width * 0.285, height * (0.01 + i * width/height * 0.07 ), width * 0.06, width * 0.06))

            userid_button = QtWidgets.QPushButton(self.Form)
            userid_button.setText(_translate("Form", 'default Name'))
            userid_button.setCursor(Qt.OpenHandCursor)
            userid_button.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});\
                        font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;text-align:left;".format(opaque))
            userid_button.setObjectName("file_userid_{0}".format(i))
            userid_button.setGeometry(QRect(width * 0.35, height * (0.025 + i * width/height * 0.07), width * 0.18, width * 0.045))

            filename_button = QtWidgets.QPushButton(self.Form)
            filename_button.setText(_translate("Form", 'default FileName'))
            filename_button.setCursor(Qt.OpenHandCursor)
            filename_button.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});\
                        font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;text-align:left;".format(opaque))
            filename_button.setObjectName("file_filename_{0}".format(i))
            filename_button.setGeometry(QRect(width * 0.54, height * (0.025 + i * width/height * 0.07), width * 0.3, width * 0.045))

            accept_button = QtWidgets.QPushButton(self.Form)
            accept_button.setGeometry(QRect(width * 0.85, height * (0.03 + i * width/height * 0.07), width * 0.04, width * 0.04))
            accept_button.setStyleSheet("border-radius:10px;background-color:rgba(0,0,0,{0});\
                        font-size:12px;font-weight:bold;color:white;font-family:Comic Sans MS;".format(opaque))
            accept_button.setObjectName('file_accept_{0}'.format(i))
            accept_button.setText(_translate("Form", '✓'))  # √,✓,✔
            accept_button.setCursor(Qt.OpenHandCursor)

            reject_button = QtWidgets.QPushButton(self.Form)
            reject_button.setText(_translate("Form", 'X'))
            reject_button.setCursor(Qt.OpenHandCursor)
            reject_button.setStyleSheet("border-radius:10px;background-color:rgba(0,0,0,{0});\
                        font-size:16px;font-weight:bold;color:white;font-family:Comic Sans MS;".format(opaque))
            reject_button.setObjectName("file_reject_{0}".format(i)) 
            reject_button.setGeometry(QRect(width * 0.9, height * (0.03 + i * width/height * 0.07), width * 0.04, width * 0.04))

            icon_button.hide()
            userid_button.hide()
            filename_button.hide()
            accept_button.hide()
            reject_button.hide()

            self.file_list.append([[], icon_button, userid_button,filename_button, accept_button, reject_button])

    def create_conversation_page(self, userid):
        _translate = QtCore.QCoreApplication.translate
        width = self.width()
        height = self.height()
        opaque = self.opaque
        Form = self.Form
        icon_path_0 = photo_base_path + userid + ".png"
        icon_path_1 = photo_base_path + self.clientId + ".png"

        textBrowser_00 = QtWidgets.QTextBrowser(Form)
        textBrowser_00.setObjectName("conversation_" + userid)
        textBrowser_00.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        textBrowser_00.setGeometry(QRect(width * 0.3, height * 0.03, width * 0.5, height * 0.75))
        # self.gridLayout.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        textBrowser_01 = QtWidgets.QTextBrowser(Form)
        # self.textBrowser.setMaximumSize(QtCore.QSize(160, 16777215))
        textBrowser_01.setGeometry(QRect(width *0.83, height * 0.03, width * 0.15, height * 0.75))
        textBrowser_01.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        textBrowser_01.setObjectName("conversation_rightbar_"+userid)
        # self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        textEdit_10 = QtWidgets.QTextEdit(Form)
        textEdit_10.setGeometry(QRect(width * 0.3, height * 0.8, width * 0.5 , height * 0.18))
        textEdit_10.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        # self.textEdit.setMaximumSize(QtCore.QSize(16777215, 70))
        textEdit_10.setObjectName("conversation_input_"+userid)
        # self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        pushButton_11 = QtWidgets.QPushButton(Form)
        # self.pushButton.setMaximumSize(QtCore.QSize(16777215, 70))
        pushButton_11.setGeometry(QRect(width * 0.83, height * 0.84, width * 0.15, height * 0.14))
        pushButton_11.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        pushButton_11.setObjectName("conversation_pushButton_"+userid)
        pushButton_11.setText(_translate("Form", "ENTER"))
        pushButton_11.setCursor(Qt.OpenHandCursor)

        uploadButton = QtWidgets.QPushButton(Form)
        uploadButton.setGeometry(QRect(width * 0.83, height * 0.80, width * 0.15, height * 0.03))
        uploadButton.setStyleSheet("border-radius:6px;background-color:rgba(255,255,255,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        uploadButton.setObjectName("conversation_uploadButton_0")
        uploadButton.setCursor(Qt.OpenHandCursor)
        uploadButton.clicked.connect(self.upload_file)
        uploadButton.setText(_translate("Form", "UPLOAD FILE"))

        icon_button_0 = QtWidgets.QPushButton(self.Form)
        icon_button_0.setStyleSheet("QPushButton{border-radius:10px;border-image: url("+icon_path_0+");}")
        icon_button_0.setCursor(Qt.OpenHandCursor)
        icon_button_0.setObjectName("conversation_icon_0_{0}".format(userid))
        icon_button_0.setGeometry(QRect(width * 0.84, height * 0.05, width * 0.13, width * 0.13))

        icon_button_1 = QtWidgets.QPushButton(self.Form)
        icon_button_1.setStyleSheet("QPushButton{border-radius:10px;border-image: url("+icon_path_1+");}")
        icon_button_1.setCursor(Qt.OpenHandCursor)
        icon_button_1.setObjectName("conversation_icon_1_{0}".format(userid))
        icon_button_1.setGeometry(QRect(width * 0.84, height * 0.58, width * 0.13, width * 0.13))

        textBrowser_00.hide()
        textBrowser_01.hide()
        textEdit_10.hide()
        pushButton_11.hide()
        uploadButton.hide()
        icon_button_1.hide()
        icon_button_0.hide()
        return [textBrowser_00, textBrowser_01, textEdit_10, pushButton_11,uploadButton,icon_button_0,icon_button_1]

    def create_groupchat_page(self, groupid):
        print('line 359 groupid',groupid)
        _translate = QtCore.QCoreApplication.translate
        width = self.width()
        height = self.height()
        opaque = self.opaque
        Form = self.Form

        textBrowser_00 = QtWidgets.QTextBrowser(Form)
        textBrowser_00.setObjectName("groupchat_" + groupid)
        textBrowser_00.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        textBrowser_00.setGeometry(QRect(width * 0.3, height * 0.03, width * 0.5, height * 0.75))
        # self.gridLayout.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        textBrowser_01 = QtWidgets.QTextBrowser(Form)
        # self.textBrowser.setMaximumSize(QtCore.QSize(160, 16777215))
        textBrowser_01.setGeometry(QRect(width *0.83, height * 0.03, width * 0.15, height * 0.75))
        textBrowser_01.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        textBrowser_01.setObjectName("groupchat_rightbar_"+groupid)
        # self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        textEdit_10 = QtWidgets.QTextEdit(Form)
        textEdit_10.setGeometry(QRect(width * 0.3, height * 0.8, width * 0.5 , height * 0.18))
        textEdit_10.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        # self.textEdit.setMaximumSize(QtCore.QSize(16777215, 70))
        textEdit_10.setObjectName("groupchat_input_"+groupid)
        # self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        pushButton_11 = QtWidgets.QPushButton(Form)
        # self.pushButton.setMaximumSize(QtCore.QSize(16777215, 70))
        pushButton_11.setGeometry(QRect(width * 0.83, height * 0.84, width * 0.15, height * 0.14))
        pushButton_11.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        pushButton_11.setObjectName("groupchat_pushButton_"+groupid)
        pushButton_11.setText(_translate("Form", "ENTER"))
        pushButton_11.setCursor(Qt.OpenHandCursor)

        uploadButton = QtWidgets.QPushButton(Form)
        uploadButton.setGeometry(QRect(width * 0.83, height * 0.80, width * 0.15, height * 0.03))
        uploadButton.setStyleSheet("border-radius:6px;background-color:rgba(255,255,255,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        uploadButton.setObjectName("groupchat_uploadButton_"+groupid)
        uploadButton.setCursor(Qt.OpenHandCursor)
        uploadButton.clicked.connect(self.upload_file)
        uploadButton.setText(_translate("Form", "UPLOAD FILE"))

        leftButton = QtWidgets.QPushButton(Form)
        leftButton.setGeometry(QRect(width * 0.85, height * 0.75, width * 0.05, height * 0.02))
        leftButton.setStyleSheet("border-radius:10px;background-color:rgba(126,126,126,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(0))
        leftButton.setObjectName("groupchat_leftButton_"+groupid)
        leftButton.setCursor(Qt.OpenHandCursor)
        leftButton.setText(_translate("Form", "<-<-")) 
        leftButton.clicked.connect(self.last_page)
         

        rightButton = QtWidgets.QPushButton(Form)
        rightButton.setGeometry(QRect(width * 0.92, height * 0.75, width * 0.05, height * 0.02))
        rightButton.setStyleSheet("border-radius:10px;background-color:rgba(126,126,126,{0});\
                    font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(0))

                    #border-image: url('./images/right2.jpg')
        rightButton.setObjectName("groupchat_rightButton_"+groupid)
        rightButton.setCursor(Qt.OpenHandCursor)
        rightButton.setText(_translate("Form", "->->")) 
        rightButton.clicked.connect(self.next_page) 

        items = [textBrowser_00, textBrowser_01, textEdit_10, pushButton_11,uploadButton,leftButton,rightButton]
        userlist = []
        for i in range(max_userlist):
            icon_button = QtWidgets.QPushButton(self.Form)
            icon_button.setStyleSheet("QPushButton{border-radius:10px;border-image: url('./images/dark_star');}")
            icon_button.setCursor(Qt.OpenHandCursor)
            icon_button.setObjectName("group_{0}_user_icon_{1}".format(groupid,i))
            icon_button.setGeometry(QRect(width * 0.845, height * (0.04 + i * width/height * 0.05 ), width * 0.045, width * 0.045))
            icon_button.hide()
            icon_button.clicked.connect(self.CHANGE_PAGE)
            userid_button = QtWidgets.QPushButton(self.Form)
            userid_button.setText(_translate("Form", str(i)))
            userid_button.setCursor(Qt.OpenHandCursor)
            userid_button.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});\
                        font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
            userid_button.setObjectName("group_{0}_user_userid_{1}".format(groupid,i))
            userid_button.setGeometry(QRect(width * 0.89, height * (0.05 + i * width/height * 0.05), width * 0.08, width * 0.03))
            userid_button.hide()
            userid_button.clicked.connect(self.CHANGE_PAGE)
            userlist.append(['', icon_button, userid_button])
            items.append(icon_button)
            items.append(userid_button)


        textBrowser_00.hide()
        textBrowser_01.hide()
        textEdit_10.hide()
        pushButton_11.hide()
        uploadButton.hide()
        leftButton.hide()
        rightButton.hide()
        return items,userlist

    



class ChatPage(QWidget, Ui_chatWindow):
    APPEND = QtCore.pyqtSignal(str)
    new_conv = QtCore.pyqtSignal(str, str)
    new_file = QtCore.pyqtSignal(str, str, str)
    ask_users = QtCore.pyqtSignal(str)
    SHOW = QtCore.pyqtSignal()
    CHANGE_PAGE = QtCore.pyqtSignal()
    DELETE_CONVERSATION = QtCore.pyqtSignal()

    conv_list = []  # 组件信息的列表 记录了组件的 用户名、头像路径和消息数量,or other information
    conv_pages = []  # 每一个页是一个组件的列表 pagelist是列表的列表 其顺序对应chatbar中的顺序
    conv_people = []
    conv_type = [] # public \ file \ private \ group
    group_userbutton_list = {}
    group_user_list = {}
    group_page = {}
    # conv的0都是public 1都是file
    # cur_pageid 记录当前页 页是一个列表 [] 包含4个框 以及可能会有头像和别的按钮 public聊天的用户列表
    # userlist 和 chatlist 是组件的列表
    # conv_people 和 user_peoplelist 是用户（数据）的列表

    def __init__(self, sock, parent=None):
        super(ChatPage, self).__init__(parent)
        
        self.setupUi(self)
        self.sock = sock
        self.ask_users.connect(self.update_userlist)
        self.SHOW.connect(self.show)
        self.APPEND.connect(self.public_append)
        self.new_conv.connect(self.new_conversation)
        self.new_file.connect(self.receive_new_file)
        self.CHANGE_PAGE.connect(self.change_page)
        self.DELETE_CONVERSATION.connect(self.delete_conversation)
        self.pushButton.clicked.connect(self.SEND)
        self.pushButton.clicked.connect(self.textEdit.clear)
        self.uploadButton.clicked.connect(self.upload_file)
        self.leftButton.clicked.connect(self.last_page)
        self.rightButton.clicked.connect(self.next_page)
        for item in self.userlist:
            for button in item[1:]:
                button.clicked.connect(self.CHANGE_PAGE)

        for item in self.chatlist:
            for button in item[1:3]:
                button.clicked.connect(self.CHANGE_PAGE)

        for item in self.chatlist:
            button = item[4]
            button.clicked.connect(self.DELETE_CONVERSATION)

        for item in self.file_list:
            accept_button = item[4]
            reject_button = item[5]
            accept_button.clicked.connect(self.accept_file)
            reject_button.clicked.connect(self.reject_file)

        self.user_peoplelist = []

        self.filedata_list = []  # [['oxer','file1','url1'],['oxer','file2','url2'],['oxer','file3','url3'],['oxer','file4','url4'],['oxer','file5','url5']]
        # 临时代码

        self.cur_pageid = 0
        page = [self.textBrowser_2, self.textBrowser, self.textEdit, self.pushButton, self.uploadButton, self.leftButton, self.rightButton]
        file_page = []
        for tup in self.file_list:
            for item in tup[1:]:
                file_page.append(item)
        for item in self.userlist:
            for button in item[1:]:
                page.append(button)
        self.conv_pages.append(page)
        self.conv_pages.append(file_page)
        self.conv_list.append(['PUBLIC', star_path, 0])
        self.conv_list.append(['FILE',filepage_path, 0])
        self.conv_people.append('PUBLIC')
        self.conv_people.append('FILE')
        self.conv_type = ['public','file']
        self.update_chatlist()

        self.userpage_index = 1
        self.newgroupButton.clicked.connect(self.find_newgroup)
        self.new_groupWindow = NewGroupPage(self.sock)

        #self.new_group('gp_4396')

    def find_newgroup(self):
        self.new_groupWindow.show()
        self.new_groupWindow.owner = self

        


    def last_page(self):
        sender = self.sender()
        name = sender.objectName()
        prefix = name.split('_')[0]
        #print('prefix',prefix)
        if prefix == 'conversation':
            if self.userpage_index > 1:
                self.userpage_index -= 1
                self.update_userlist()
        elif prefix == 'groupchat':
            groupid = 'gp_'+name.split('_')[-1]
            chat_index = self.conv_people.index(groupid)
            if self.group_page[chat_index] > 1:
                self.group_page[chat_index] -=1
                #print('page ',self.group_page[chat_index])
                self.update_group_userlist(chat_index)

    def next_page(self):
        # print('?? ,len(self.users) ',self.userpage_index,len(self.users),max_userlist,self.userpage_index < (len(self.users) // max_userlist))
        sender = self.sender()
        name = sender.objectName()
        prefix = name.split('_')[0]
        #print('prefix',prefix)
        if prefix == 'conversation':
            if self.userpage_index < ((len(self.users) -1) // max_userlist +1):
                self.userpage_index +=1
                self.update_userlist()
        elif prefix == 'groupchat':
            groupid = 'gp_'+name.split('_')[-1]
            chat_index = self.conv_people.index(groupid)
            #print(' chat_index',chat_index)
            if self.group_page[chat_index] < ((len(self.group_user_list[chat_index]) -1)// max_userlist +1):
                self.group_page[chat_index] +=1
                #print('page ',self.group_page[chat_index])
                self.update_group_userlist(chat_index)

    def upload_file(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '')
        id = self.cur_pageid
        if id == 0:
            self.APPEND.emit('I upload file:\n' + openfile_name[0])
            send_file_all(self.sock, openfile_name[0])
        else:
            self.conv_pages[id][0].append('I upload file:\n' + openfile_name[0])
            send_file(self.sock, [self.conv_list[id][0]], openfile_name[0])

    def receive_new_file(self, user, filename, filesize):
        self.filedata_list.append([user, filename, filesize])
        if self.cur_pageid == 1:
            self.flush_page(cur_pageid)
        self.conv_list[1][2] += 1
        self.chatlist[1][3].setText(
            QtCore.QCoreApplication.translate("Form", ' {0}'.format(self.conv_list[1][2])))

    def SEND(self):
        id = self.cur_pageid
        if id == 0:
            data = self.textEdit.toPlainText()
            self.APPEND.emit('I say:\n' + data)
            send_all(self.sock, data)
        else:
            data = self.conv_pages[id][2].toPlainText()
            self.conv_pages[id][0].append('I say:\n' + data)
            send_msg(self.sock, [self.conv_list[id][0]], data)

    def public_append(self, msg):
        if self.cur_pageid != 0:
            self.conv_list[0][2] += 1
            self.chatlist[0][3].setText(
                QtCore.QCoreApplication.translate("Form", ' {0}'.format(self.conv_list[0][2])))

        self.conv_pages[0][0].append(msg)

    def new_conversation(self, user, msg):
        if user not in self.conv_people:
            self.conv_people.append(user)
            icon_path = photo_base_path + user + ".png"

            self.conv_list.append([user, icon_path, 0])
            self.update_chatlist()

            page = self.create_conversation_page(user)
            page[3].clicked.connect(self.SEND)
            page[3].clicked.connect(page[2].clear)
            self.conv_pages.append(page)
            self.conv_type.append('private')
            
        chat_index = self.conv_people.index(user)
        if chat_index != self.cur_pageid:
            self.conv_list[chat_index][2] += 1
            self.chatlist[chat_index][3].setText(QtCore.QCoreApplication.translate("Form", ' {0}'.format(self.conv_list[chat_index][2])))
        # self.flush_page(chat_index)

        self.conv_pages[chat_index][0].append(user + msg)

    def delete_conversation(self):
        sender = self.sender()
        name = sender.objectName()
        btn_idx = int(name.split('_')[-1])
        self.conv_list.pop(btn_idx)
        self.conv_people.pop(btn_idx)
        
        self.update_chatlist()
        self.flush_page(0)
        self.conv_pages.pop(btn_idx)
        #print('btn_idx,',btn_idx,self.conv_type)
        if self.conv_type[btn_idx] == 'group':
            del self.group_userbutton_list[btn_idx]
            del self.group_user_list[btn_idx]
            del self.group_page[btn_idx]
        #print('group page',self.group_page)
        #copy = self.group_page
        for chat_index in self.group_page.copy():
            #print('check index',chat_index)
            self.group_page[chat_index-1] = self.group_page[chat_index]
            self.group_userbutton_list[chat_index-1] = self.group_userbutton_list[chat_index]
            self.group_user_list[chat_index-1] = self.group_user_list[chat_index]
            del self.group_page[chat_index]
            del self.group_userbutton_list[chat_index]
            del self.group_user_list[chat_index]
        self.conv_type.pop(btn_idx)

    def update_userlist(self, data=None):

        _translate = QtCore.QCoreApplication.translate
        for i in range(max_userlist):
            self.userlist[i][0] = ''
            icon_button = self.userlist[i][1]
            userid_button = self.userlist[i][2]
            icon_button.hide()
            userid_button.hide()

        self.user_peoplelist = [['PUBLIC', star_path]]
        if data is not None:
            self.users = data.split('\n')  # 希望保存这个数据

        for i, userid in enumerate(self.users[(self.userpage_index-1)*max_userlist:self.userpage_index*max_userlist]):
            if len(userid) == 0:
                continue
            self.userlist[i][0] = userid
            icon_path = photo_base_path + userid + ".png"
            self.user_peoplelist.append([userid, icon_path])

        log_out_user = None
        for i, item in enumerate(self.conv_list):
            if i != 0 and i != 1 and item[0] not in self.users:
                print(item[0], self.users)
                log_out_user = i
        if log_out_user is not None:
            if self.cur_pageid == log_out_user:
                self.flush_page(0)
            elif self.cur_pageid > log_out_user:
                self.cur_pageid -= 1
            self.conv_list.pop(log_out_user)
            self.conv_people.pop(log_out_user)
            self.conv_pages.pop(log_out_user)
            self.update_chatlist()

        for i, userid in enumerate(self.users[(self.userpage_index-1)*max_userlist:self.userpage_index*max_userlist]):
            if len(userid) == 0:
                continue
            self.userlist[i][0] = userid
            icon_path = photo_base_path + userid + ".png"
            if self.cur_pageid == 0:
                self.userlist[i][2].setText(_translate("Form", userid))
                self.userlist[i][1].setStyleSheet("QPushButton{border-radius:10px;border-image: url('"+icon_path+"');}")
                self.userlist[i][1].show()
                self.userlist[i][2].show()

    def update_group_userlist(self,chat_index, data=None):

        _translate = QtCore.QCoreApplication.translate
        for i in range(max_userlist):
            self.group_userbutton_list[chat_index][i][0] = ''
            icon_button = self.group_userbutton_list[chat_index][i][1]
            userid_button = self.group_userbutton_list[chat_index][i][2]
            icon_button.hide()
            userid_button.hide()

        '''
        self.user_peoplelist = [['PUBLIC', star_path]]
        if data is not None:
            self.users = data.split('\n')  # 希望保存这个数据


        for i, userid in enumerate(self.users[(self.userpage_index-1)*max_userlist:self.userpage_index*max_userlist]):
            if len(userid) == 0:
                continue
            self.userlist[i][0] = userid
            icon_path = photo_base_path + userid + ".png"
            self.user_peoplelist.append([userid, icon_path])

        log_out_user = None
        for i, item in enumerate(self.conv_list):
            if i != 0 and i != 1 and item[0] not in self.users:
                print(item[0], self.users)
                log_out_user = i
        if log_out_user is not None:
            if self.cur_pageid == log_out_user:
                self.flush_page(0)
            elif self.cur_pageid > log_out_user:
                self.cur_pageid -= 1
            self.conv_list.pop(log_out_user)
            self.conv_people.pop(log_out_user)
            self.conv_pages.pop(log_out_user)
            self.update_chatlist()
        '''

        for i, item in enumerate(self.group_user_list[chat_index][(self.group_page[chat_index]-1)*max_userlist:self.group_page[chat_index]*max_userlist]):
            userid = item[0]

            if len(userid) == 0:
                continue
            self.group_userbutton_list[chat_index][i][0] = userid
            icon_path = photo_base_path + userid + ".png"
            if self.cur_pageid == chat_index:
                self.group_userbutton_list[chat_index][i][2].setText(_translate("Form", userid))
                self.group_userbutton_list[chat_index][i][1].setStyleSheet("QPushButton{border-radius:10px;border-image: url('"+icon_path+"');}")
                self.group_userbutton_list[chat_index][i][1].show()
                self.group_userbutton_list[chat_index][i][2].show()

    def update_filelist(self):
        _translate = QtCore.QCoreApplication.translate
        filedata_list = self.filedata_list
        for i in range(max_filelist):
            file_data = self.file_list[i][0]
            icon_button = self.file_list[i][1]
            userid_button = self.file_list[i][2]
            filename_button = self.file_list[i][3]
            accept_button = self.file_list[i][4]
            reject_button = self.file_list[i][5]
            icon_button.hide()
            userid_button.hide()
            filename_button.hide()
            accept_button.hide()
            reject_button.hide()

        for i, file_data in enumerate(filedata_list):
            self.file_list[i][0] = file_data
            icon_button = self.file_list[i][1]
            userid_button = self.file_list[i][2]
            filename_button = self.file_list[i][3]
            accept_button = self.file_list[i][4]
            reject_button = self.file_list[i][5]
            userid = file_data[0]
            filename = file_data[1]
            filesize = file_data[2]
            icon_path = photo_base_path + userid + ".png"
            icon_button.setStyleSheet("QPushButton{border-radius:10px;border-image: url("+icon_path+");}")
            userid_button.setText(_translate("Form", userid))
            filename_button.setText(_translate("Form", filename))
            icon_button.show()
            userid_button.show()
            filename_button.show()
            accept_button.show()
            reject_button.show()

    def update_chatlist(self):
        _translate = QtCore.QCoreApplication.translate
        conv_list = self.conv_list
        for i in range(max_chatlist):
            self.chatlist[i][0] = ''
            icon_button = self.chatlist[i][1]
            userid_button = self.chatlist[i][2]
            messagenum_label = self.chatlist[i][3]
            close_button = self.chatlist[i][4]
            icon_button.hide()
            userid_button.hide()
            messagenum_label.hide()
            close_button.hide()

        for i, item in enumerate(conv_list):
            userid = item[0]
            icon_path = item[1]
            messagenum = item[2]
            icon_button = self.chatlist[i][1]
            userid_button = self.chatlist[i][2]
            messagenum_label = self.chatlist[i][3]
            close_button = self.chatlist[i][4]
            userid_button.setText(_translate("Form", userid))
            icon_button.setStyleSheet("QPushButton{border-radius:10px;border-image: url("+icon_path+");}")
            messagenum_label.setText(_translate("Form", '  '+str(messagenum)))
            icon_button.show()
            userid_button.show()
            messagenum_label.show()
            close_button.show()

        self.chatlist[0][4].hide()
        self.chatlist[1][4].hide()

    def accept_file(self):
        sender = self.sender()
        name = sender.objectName()
        index = int(name.split('_')[-1])
        down_file(self.sock, self.filedata_list[index][0], self.filedata_list[index][1])
        self.filedata_list.pop(index)
        self.update_filelist()

    def reject_file(self):
        sender = self.sender()
        name = sender.objectName()
        index = int(name.split('_')[-1])
        self.filedata_list.pop(index)
        self.update_filelist()

    def change_page(self):
        sender = self.sender()
        name = sender.objectName()
        btn_idx = int(name.split('_')[-1])  # 这个是按钮序号
        #print('btn_idx',btn_idx)
        prefix = name.split('_')[0]
        # pre = chat -> chatbar
        # pre = user -> userbar
        midfix = name.split('_')[1]

        if prefix == 'user' or prefix == 'group':
            if prefix == 'user':
                username = self.userlist[btn_idx][0]  # 用户名
            elif prefix == 'group':
                groupid = 'gp_'+name.split('_')[2]
                chat_index = self.conv_people.index(groupid)
                username = self.group_userbutton_list[chat_index][btn_idx][0]
            #print('username ',self.userlist,username)
            if username == self.clientId:
                return
            if username not in self.conv_people:
                if len(self.conv_list) == max_chatlist:
                    self.conv_list.pop(2)
                    self.conv_people.pop(2)
                    self.update_chatlist()
                    self.flush_page(0)
                    self.conv_pages.pop(2)

                chatnum = len(self.conv_people)
                self.conv_people.append(username)
                # chatbar按时间序

                if midfix == 'icon':
                    icon_ss = sender.styleSheet()
                    icon_path = icon_ss.split("'")[1]  # 如果点的不是头像就找不到了..
                else:
                    icon_path = photo_base_path + username + ".png"

                self.conv_list.append([username, icon_path, 0])

                page = self.create_conversation_page(username)
                page[3].clicked.connect(self.SEND)
                page[3].clicked.connect(page[2].clear)
                self.conv_pages.append(page)
                self.conv_type.append('private')

            chat_index = self.conv_people.index(username)

        elif prefix == 'chat':
            chat_index = btn_idx
        elif prefix == 'conversation':
            chat_index = 0


        self.conv_list[chat_index][2] = 0
        if self.cur_pageid == 1:
            self.update_filelist()
        else:
            self.update_chatlist()
        self.flush_page(chat_index)

    def flush_page(self, chat_index):
        #print('line 788',self.conv_pages[self.cur_pageid])
        for item in self.conv_pages[self.cur_pageid]:
            item.hide()

        page_type = self.conv_type[chat_index]

        if page_type == 'public':
            for item in self.conv_pages[chat_index][:7]:
                item.show() 
            for items in self.userlist[:len(self.user_peoplelist)-1]:
                for item in items[1:3]:
                    item.show()
        elif page_type == 'file':
            self.update_filelist()
            file_list = self.file_list
            for i, filetup in enumerate(file_list[:len(self.filedata_list)]):
                for item in filetup[1:]:
                    item.show()
        elif page_type == 'private':
            for item in self.conv_pages[chat_index]:
                item.show()
        elif page_type == 'group':
            #print('line 815 ',self.conv_pages)
            for item in self.conv_pages[chat_index][:7]:
                item.show()
            print('self group_page',self.group_page)
            userpage = self.group_page[chat_index]

            for i,item in enumerate(self.group_user_list[chat_index][(userpage - 1) *max_userlist : userpage * max_userlist]):
                user = item[0]
                if ( user == ''):
                    break
                icon_path = item[1]
                #print('850 ???',self.group_userbutton_list[chat_index])
                icon_button = self.group_userbutton_list[chat_index][i][1]
                icon_button.setStyleSheet("QPushButton{border-radius:10px;border-image: url('"+icon_path+"');}")
                userid_button = self.group_userbutton_list[chat_index][i][2]
                self.group_userbutton_list[chat_index][i][0] = user
                _translate = QtCore.QCoreApplication.translate
                userid_button.setText(_translate("Form", user))
                icon_button.show()
                userid_button.show()

        self.cur_pageid = chat_index


    def setClientId(self, clientId):
        self.clientId = clientId

    def resizeEvent(self, event):
        width = self.width()
        height = self.height()
        '''
        print('line 710')
        self.setMinimumHeight(width * 0.5 / 0.7)
        print('line 712 ',height,width * 0.5 / 0.7)
        '''
        self.chatBar.setGeometry(QRect(0, 0, width * 0.27, height))
        self.chatBarPic.setGeometry(QRect(0, 0, width * 0.27, height))
        self.chatBoardPic.setGeometry(QRect(width * 0.27, 0, width * 0.73, height))
        self.textBrowser_2.setGeometry(QRect(width * 0.3, height * 0.03, width * 0.5, height * 0.75))
        self.textBrowser.setGeometry(QRect(width * 0.83, height * 0.03, width * 0.15, height * 0.75))
        self.textEdit.setGeometry(QRect(width * 0.3, height * 0.8, width * 0.5, height * 0.18))
        self.pushButton.setGeometry(QRect(width * 0.83, height * 0.84, width * 0.15, height * 0.14))
        self.uploadButton.setGeometry(QRect(width * 0.83, height * 0.80, width * 0.15, height * 0.03))
        self.leftButton.setGeometry(QRect(width * 0.85, height * 0.75, width * 0.05, height * 0.02))
        self.rightButton.setGeometry(QRect(width * 0.92, height * 0.75, width * 0.05, height * 0.02))
         


        for i, tup in enumerate(self.userlist):
            icon_button = tup[1]
            userid_button = tup[2]
            width_ = width
           
            if (height *1.4133 < width):
                width_ = height * 1.4133 
                
            
            icon_button.setGeometry(QRect(width * 0.845, height * (0.04 + i * width_/height * 0.05), width_ * 0.045, width_ * 0.045))
            userid_button.setGeometry(QRect(width * 0.89, height * (0.05 + i * width_/height * 0.05), width_ * 0.08, width_ * 0.03))

        for i, tup in enumerate(self.chatlist):
            icon_button = tup[1]
            userid_button = tup[2]
            nummessage_label = tup[3]
            close_button = tup[4]


            icon_button.setGeometry(QRect(width * 0.015, height * (0.035 + i * width/height * 0.06 ), width * 0.06, width * 0.06))
            userid_button.setGeometry(QRect(width * 0.08, height * (0.05 + i * width/height * 0.06), width * 0.18, width * 0.045))
            nummessage_label.setGeometry(QRect(width * 0.23, height * (0.063 + i * width/height * 0.06), width * 0.03, width * 0.03))
            close_button.setGeometry(QRect(width * 0.09, height * (0.06 + i * width/height * 0.06), width * 0.03, width * 0.03))

        for i,tup in enumerate(self.conv_pages[2:]):
            textBrowser_00 = tup[0]
            textBrowser_01 = tup[1]
            textEdit_10 = tup[2]
            pushButton_11 = tup[3]
            uploadButton = tup[4]
            icon_button_0 = tup[5]
            icon_button_1 = tup[6]
            textBrowser_00.setGeometry(QRect(width * 0.3, height * 0.03, width * 0.5, height * 0.75))
            textBrowser_01.setGeometry(QRect(width *0.83, height * 0.03, width * 0.15, height * 0.75))
            textEdit_10.setGeometry(QRect(width * 0.3, height * 0.8, width * 0.5 , height * 0.18))
            pushButton_11.setGeometry(QRect(width * 0.83, height * 0.84, width * 0.15, height * 0.14))
            uploadButton.setGeometry(QRect(width * 0.83, height * 0.80, width * 0.15, height * 0.03))
            icon_button_0.setGeometry(QRect(width * 0.84, height * 0.05, width * 0.13, width * 0.13))
            icon_button_1.setGeometry(QRect(width * 0.84, height * 0.58, width * 0.13, width * 0.13))

        for i,tup in enumerate(self.file_list):
            icon_button = tup[1]
            userid_button = tup[2]
            filename_button = tup[3]
            accept_button = tup[4]
            reject_button = tup[5]
            icon_button.setGeometry(QRect(width * 0.285, height * (0.01 + i * width/height * 0.07 ), width * 0.06, width * 0.06))
            userid_button.setGeometry(QRect(width * 0.35, height * (0.025 + i * width/height * 0.07), width * 0.18, width * 0.045))
            filename_button.setGeometry(QRect(width * 0.54, height * (0.025 + i * width/height * 0.07), width * 0.3, width * 0.045))
            accept_button.setGeometry(QRect(width * 0.85, height * (0.03 + i * width/height * 0.07), width * 0.04, width * 0.04))
            reject_button.setGeometry(QRect(width * 0.9, height * (0.03 + i * width/height * 0.07), width * 0.04, width * 0.04))


        
        # assert 0.7 * height > 0.45 * width
        '''
        print('line 774 ',width,height,0.45 * width / 0.7)
        if ( height < 0.45 * width / 0.7 -1):
            print('line 778 resize',height , 0.45 * width / 0.7)
            self.resize(width, 0.45 * width / 0.7)
            print('line 713 resize over')
            return
        '''
        
    def new_group(self, groupid): # 就让groupid的格式为'gp_4356'这样吧
        if groupid not in self.conv_people:
            self.conv_people.append(groupid)
            #icon_path = photo_base_path + user + ".png"

            self.conv_list.append([groupid, groupicon_path, 0])
            self.update_chatlist()

            page,group_userbutton_list = self.create_groupchat_page(groupid)
            page[3].clicked.connect(self.SEND)
            page[3].clicked.connect(page[2].clear)
            self.conv_pages.append(page)
            self.conv_type.append('group')
            
        chat_index = self.conv_people.index(groupid)

        # 修改：读取当前聊天室用户数据，并为他们设置头像 现在是测试代码
        group_user_list = []
        for i in range(25):
            dic = {0:'oxer',1:'hwh',2:'wch',3:'lhq'}
            user = dic[ i%4 ]
            icon_path = photo_base_path + user + ".png"
            group_user_list.append((user, icon_path))


        self.group_userbutton_list[chat_index] = group_userbutton_list
        self.group_user_list[chat_index] = group_user_list
        self.group_page[chat_index] = 1
        print('self.group_user_list[chat_index]',self.group_user_list[chat_index])
        if chat_index != self.cur_pageid:
            #self.conv_list[chat_index][2] += 1
            self.chatlist[chat_index][3].setText(QtCore.QCoreApplication.translate("Form", ' {0}'.format(self.conv_list[chat_index][2])))
        
        print('people ',self.conv_people)
        print('list ',self.conv_list)
        print('type ',self.conv_type)
        self.flush_page(chat_index)






















