from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.Qt import *
import cgitb
import time
import client

chat_height = 646
chat_width = 913
#background_path = "./images/star.jpg"
tiancao_path = "./images/tiancao.png"
star_path = "./images/little_star.png"
darkstar_path = "./images/dark_star.png"
cgitb.enable(format = 'text')
chatbar_path = "./images/hanabi.png"
chatboard_path = "./images/hanabi_colorful.jpg"


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
        background_palette.setBrush(self.backgroundRole(),QBrush(background_pixmap))
        self.setPalette(background_palette)
        #print('where am i ?')



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
        self.chatBar.setGeometry(QRect(0,0,width * 0.27, height ))

        
        self.chatBarPic = QtWidgets.QLabel(Form)
        self.chatBarPic.setGeometry(QRect(0,0,width * 0.27, height ))
        self.chatBarPic.setObjectName('charBarPic')
        self.chatBarPic.setScaledContents(True)
        self.chatBarPic.setPixmap(QtGui.QPixmap(chatbar_path))

        self.chatBoardPic = QtWidgets.QLabel(Form)
        self.chatBoardPic.setGeometry(QRect(width * 0.27,0,width * 0.73, height ))
        self.chatBoardPic.setObjectName('charBoardPic')
        self.chatBoardPic.setScaledContents(True)
        self.chatBoardPic.setPixmap(QtGui.QPixmap(chatboard_path))

        opaque = 210
        self.opaque = opaque

        self.textBrowser_2 = QtWidgets.QTextBrowser(Form) #这个是聊天的
        self.textBrowser_2.setObjectName("conversation_0")
        self.textBrowser_2.setStyleSheet("border-radius:10px;background-color:rgba(126,126,126,{0});font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        self.textBrowser_2.setGeometry(QRect(width * 0.3, height * 0.03, width * 0.5, height * 0.75))
        #self.gridLayout.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        #self.textBrowser.setMaximumSize(QtCore.QSize(160, 16777215))
        self.textBrowser.setGeometry(QRect(width *0.83, height * 0.03, width * 0.15, height * 0.75))
        self.textBrowser.setStyleSheet("border-radius:10px;background-color:rgba(126,126,126,{0});font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        self.textBrowser.setObjectName("conversation_rightbar_0")
        #self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QRect(width * 0.3, height * 0.8, width * 0.5 , height * 0.18))
        self.textEdit.setStyleSheet("border-radius:10px;background-color:rgba(126,126,126,{0});font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        #self.textEdit.setMaximumSize(QtCore.QSize(16777215, 70))
        self.textEdit.setObjectName("conversation_input_0")
        #self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        #self.pushButton.setMaximumSize(QtCore.QSize(16777215, 70))
        self.pushButton.setGeometry(QRect(width * 0.83, height * 0.8, width * 0.15, height * 0.18))
        self.pushButton.setStyleSheet("border-radius:10px;background-color:rgba(126,126,126,{0});font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        self.pushButton.setObjectName("conversation_pushButton_0")


        QtCore.QMetaObject.connectSlotsByName(Form)

        self.create_userlist_label()
        self.create_chatlist_label()
        #self.conversationlist 

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "ENTER")) #调试

    def create_userlist_label(self):
        _translate = QtCore.QCoreApplication.translate
        opaque = self.opaque
        width = self.width()
        height = self.height()
        self.userlist = []
        for i in range(10):
            #icon_path = temporary_icon[userid]
            icon_button = QtWidgets.QPushButton(self.Form)
            icon_button.setStyleSheet("QPushButton{border-image: url('./images/dark_star');}")
            icon_button.setCursor(Qt.OpenHandCursor)
            icon_button.setObjectName("user_icon_{0}".format(i))
            icon_button.setGeometry(QRect(width * 0.845, height * (0.04 + i * width/height * 0.05 ), width * 0.045, width * 0.045))
            icon_button.hide()
            userid_button = QtWidgets.QPushButton(self.Form)
            userid_button.setText(_translate("Form", str(i)))
            userid_button.setCursor(Qt.OpenHandCursor)
            userid_button.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
            userid_button.setObjectName("user_userid_{0}".format(i))
            userid_button.setGeometry(QRect(width * 0.89, height * (0.05 + i * width/height * 0.05), width * 0.08, width * 0.03))
            userid_button.hide()
            self.userlist.append(['',icon_button,userid_button]) # 0是username的字符串 1是头像 2是username的button

    def create_chatlist_label(self):
        _translate = QtCore.QCoreApplication.translate
        opaque = self.opaque
        width = self.width()
        height = self.height()
        self.chatlist = []
        for i in range(10):
            #icon_path = temporary_icon[userid]
            icon_button = QtWidgets.QPushButton(self.Form)
            icon_button.setStyleSheet("QPushButton{border-image: url('./images/dark_star');}")
            icon_button.setCursor(Qt.OpenHandCursor)
            icon_button.setObjectName("chat_icon_{0}".format(i))
            icon_button.setGeometry(QRect(width * 0.015, height * (0.035 + i * width/height * 0.06 ), width * 0.06, width * 0.06))


            #icon_button.hide()
            userid_button = QtWidgets.QPushButton(self.Form)
            userid_button.setText(_translate("Form", 'default'))
            userid_button.setCursor(Qt.OpenHandCursor)
            userid_button.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
            userid_button.setObjectName("chat_userid_{0}".format(i))
            userid_button.setGeometry(QRect(width * 0.08, height * (0.05 + i * width/height * 0.06), width * 0.18, width * 0.045))
            #userid_button.hide()
            nummessage_label = QtWidgets.QLabel(self.Form)
            nummessage_label.setGeometry(QRect(width * 0.23, height * (0.063 + i * width/height * 0.06), width * 0.03, width * 0.03))
            nummessage_label.setStyleSheet("border-radius:10px;background-color:rgba(0,0,0,{0});font-size:12px;font-weight:bold;color:white;font-family:Comic Sans MS;".format(opaque))
            nummessage_label.setObjectName('chat_nummessage_{0}'.format(i))
            nummessage_label.setText(_translate("Form",' 0'))

            close_button = QtWidgets.QPushButton(self.Form)
            close_button.setText(_translate("Form", 'X'))
            close_button.setCursor(Qt.OpenHandCursor)
            close_button.setStyleSheet("border-radius:10px;background-color:rgba(0,0,0,{0});font-size:16px;font-weight:bold;color:white;font-family:Comic Sans MS;".format(opaque))
            close_button.setObjectName("chat_close_{0}".format(i)) 
            close_button.setGeometry(QRect(width * 0.09, height * (0.06 + i * width/height * 0.06), width * 0.03, width * 0.03))

            icon_button.hide()
            userid_button.hide()
            nummessage_label.hide()
            close_button.hide()
            #nummessage_label.hide()
            self.chatlist.append([[],icon_button,userid_button,nummessage_label,close_button]) # 0是username的字符串 1是头像 2是username的button 3是消息数量的button
    
    def create_conversation_page(self, userid):
        _translate = QtCore.QCoreApplication.translate
        width = self.width()
        height = self.height()
        opaque = self.opaque
        Form = self.Form

        textBrowser_00 = QtWidgets.QTextBrowser(Form) #这个是聊天的
        textBrowser_00.setObjectName("conversation_"+userid)
        textBrowser_00.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        textBrowser_00.setGeometry(QRect(width * 0.3, height * 0.03, width * 0.5, height * 0.75))
        #self.gridLayout.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        textBrowser_01 = QtWidgets.QTextBrowser(Form)
        #self.textBrowser.setMaximumSize(QtCore.QSize(160, 16777215))
        textBrowser_01.setGeometry(QRect(width *0.83, height * 0.03, width * 0.15, height * 0.75))
        textBrowser_01.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        textBrowser_01.setObjectName("conversation_rightbar_"+userid)
        #self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        textEdit_10 = QtWidgets.QTextEdit(Form)
        textEdit_10.setGeometry(QRect(width * 0.3, height * 0.8, width * 0.5 , height * 0.18))
        textEdit_10.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        #self.textEdit.setMaximumSize(QtCore.QSize(16777215, 70))
        textEdit_10.setObjectName("conversation_input_"+userid)
        #self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        pushButton_11 = QtWidgets.QPushButton(Form)
        #self.pushButton.setMaximumSize(QtCore.QSize(16777215, 70))
        pushButton_11.setGeometry(QRect(width * 0.83, height * 0.8, width * 0.15, height * 0.18))
        pushButton_11.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,{0});font-size:16px;font-weight:bold;color:black;font-family:Comic Sans MS;".format(opaque))
        pushButton_11.setObjectName("conversation_pushButton_"+userid)
        pushButton_11.setText(_translate("Form", "ENTER"))

        textBrowser_00.hide()
        textBrowser_01.hide()
        textEdit_10.hide()
        pushButton_11.hide()
        return [textBrowser_00,textBrowser_01,textEdit_10,pushButton_11]


kyogre_path = "./images/kyogre-primal.png"
temporary_icon = { 'oxer':tiancao_path, 'hwh':kyogre_path}

class ChatPage(QWidget, Ui_chatWindow):
    APPEND = QtCore.pyqtSignal(str)
    ask_users = QtCore.pyqtSignal(str)
    SHOW = QtCore.pyqtSignal()
    CHANGE_PAGE = QtCore.pyqtSignal()
    DELETE_CONVERSATION = QtCore.pyqtSignal()
    conversationlist = [] #组件信息的列表 记录了组件的 用户名、头像路径和消息数量
    conversation_pagelist = [] #每一个页是一个组件的列表 pagelist是列表的列表 其顺序对应chatbar中的顺序
    user2index = {} 
    index2user = {}
    conversation_peoplelist = []
    # currentpage 记录当前页 页是一个列表 [] 包含4个框 以及可能会有头像和别的按钮 public聊天的用户列表 
    # userlist 和chatlist 是组件的列表
    # conversation_peoplelist 和 user_peoplelist 是用户（数据）的列表

    


    def __init__(self, parent=None):
        super(ChatPage, self).__init__(parent)
        
        self.setupUi(self)
        self.ask_users.connect(self.update_userlist)
        self.SHOW.connect(self.show)
        self.APPEND.connect(self.textBrowser_2.append)
        self.CHANGE_PAGE.connect(self.change_page)
        self.DELETE_CONVERSATION.connect(self.delete_conversation)
        for item in self.userlist:
            for button in item[1:]:
                button.clicked.connect(self.CHANGE_PAGE)

        for item in self.chatlist:
            for button in item[1:3]:
                button.clicked.connect(self.CHANGE_PAGE)



        for item in self.chatlist:
            button = item[4]
            button.clicked.connect(self.DELETE_CONVERSATION)

        self.currentpage = [self.textBrowser_2,self.textBrowser,self.textEdit,self.pushButton]
        for item in self.userlist :
            for button in item[1:]:
                self.currentpage.append(button)
        self.conversation_pagelist.append(self.currentpage)
        self.conversationlist.append(['PUBLIC',star_path,0])
        self.conversation_peoplelist.append('PUBLIC')
        #self.user2index['PUBLIC'] = 0
        #self.index2user[0] = 'PUBLIC'
        self.update_chatlist()

    def delete_conversation(self):
        sender = self.sender()
        name = sender.objectName()
        button_index = int(name.split('_')[-1]) #这个是按钮序号
        self.conversationlist.pop(button_index)
        self.conversation_peoplelist.pop(button_index)
        self.conversation_pagelist.pop(button_index)
        self.update_chatlist()
        self.flush_page(0)

    def update_userlist(self, data):
        _translate = QtCore.QCoreApplication.translate
        for i in range(10):
            self.userlist[i][0] = ''
            icon_button = self.userlist[i][1]
            userid_button = self.userlist[i][2]
            icon_button.hide()
            userid_button.hide()

        self.user_peoplelist = [['PUBLIC',star_path]]

        for i,userid in enumerate(data.split('\n')):
            self.userlist[i][0] = userid
            icon_button = self.userlist[i][1]
            userid_button = self.userlist[i][2]
            icon_path = temporary_icon[userid]
            userid_button.setText(_translate("Form", userid))
            icon_button.setStyleSheet("QPushButton{border-image: url('"+icon_path+"');}")
            icon_button.show()
            userid_button.show()
            self.user_peoplelist.append([userid, icon_path])

        #print(self.userlist)
    def update_chatlist(self):
        _translate = QtCore.QCoreApplication.translate
        conversationlist = self.conversationlist
        for i in range(10):
            self.chatlist[i][0] = ''
            icon_button = self.chatlist[i][1]
            userid_button = self.chatlist[i][2]
            messagenum_label = self.chatlist[i][3]
            close_button = self.chatlist[i][4]
            icon_button.hide()
            userid_button.hide()
            messagenum_label.hide()
            close_button.hide()

        for i, item in enumerate(conversationlist):
            userid = item[0]
            icon_path = item[1]
            messagenum = item[2]
            icon_button = self.chatlist[i][1]
            userid_button = self.chatlist[i][2]
            messagenum_label = self.chatlist[i][3]
            close_button = self.chatlist[i][4]
            userid_button.setText(_translate("Form", userid))
            icon_button.setStyleSheet("QPushButton{border-image: url("+icon_path+");}")
            messagenum_label.setText(_translate("Form", '  '+str(messagenum)))
            icon_button.show()
            userid_button.show()
            messagenum_label.show()
            close_button.show()

        self.chatlist[0][4].hide()

        

    def change_page(self):
        sender = self.sender()
        #print('213 ',sender.objectName()) #得用这个获取名字..手动找API 
        name = sender.objectName()
        button_index = int(name.split('_')[-1]) #这个是按钮序号
        prefix = name.split('_')[0] #如果是左边的chatbar 这边的名字应该以chat开头..如果是右边开头则是user 这是个比较蠢的策略 但很方便.. 做2个信号量比较麻烦
        midfix = name.split('_')[1]
        #print('index ',button_index)
        if prefix == 'user':
            print('line 340 ',prefix,name,button_index)
            username = self.userlist[button_index][0] #0是用户名的字符串
            if not username in self.conversation_peoplelist :
                chatnum = len(self.conversation_peoplelist)
                self.conversation_peoplelist.append(username)
                #目前左侧chatbar的顺序是根据在列表中的顺序来的 也就是先进的在前面
                
                if midfix == 'icon':
                    icon_ss = sender.styleSheet()
                    icon_path = icon_ss.split("'")[1] #如果点的不是头像就找不到了..
                else:
                    icon_path = temporary_icon[username]

                print('icon path',icon_path)
                self.conversationlist.append([username,icon_path,0])
                self.update_chatlist()

                page = self.create_conversation_page(username)
                self.conversation_pagelist.append(page)

            chat_index = self.conversation_peoplelist.index(username)
        elif prefix == 'chat':
            chat_index = button_index
        elif prefix == 'conversation' : 
            chat_index = 0

        self.flush_page(chat_index)

        

    def flush_page(self,chat_index):
        print('line 364',chat_index)

        for item in self.currentpage:
            item.hide()

        if chat_index != 0:
            
            for item in self.conversation_pagelist[chat_index]:
                item.show()
        else:
            for item in self.conversation_pagelist[chat_index][:4]:
                item.show() 
                #print(self.userlist)
            for items in self.userlist[:len(self.user_peoplelist)-1] :
                for item in items[1:3]:
                    item.show()
        self.currentpage = self.conversation_pagelist[chat_index]






















