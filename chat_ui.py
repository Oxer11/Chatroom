from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from group_win import *
from util import *
from others import *
import cgitb

CHAT_HEIGHT = 646
CHAT_WIDTH = 913
MAX_USER = 10
MAX_CHAT = 10
MAX_FILE = 10
photo_base_path = "./images/photo/"
darkstar_path = "./images/dark_star.png"
cgitb.enable(format = 'text')
chatbar_path = "./images/hanabi.png"
chatboard_path = "./images/hanabi_colorful.jpg"
kyogre_path = "./images/kyogre-primal.png"
filepage_path = darkstar_path
groupicon_path = "./images/right2.jpg"


opacity = 210
default_style = {'border-radius': '10px',
                 'background-color': 'rgba(126,126,126,{0})'.format(opacity),
                 'font-size': '16px',
                 'font-weight': 'bold',
                 'color': 'black',
                 'font-family': 'Comic Sans MS'}

class Ui_chatWindow(object):

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(CHAT_WIDTH, CHAT_HEIGHT)
        WIDTH = self.width()
        HEIGHT = self.height()
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
        self.chatBar.setGeometry(QRect(0, 0, WIDTH * 0.27, HEIGHT))

        self.chatBarPic = QtWidgets.QLabel(Form)
        self.chatBarPic.setGeometry(QRect(0, 0, WIDTH * 0.27, HEIGHT))
        self.chatBarPic.setObjectName('charBarPic')
        self.chatBarPic.setScaledContents(True)
        self.chatBarPic.setPixmap(QtGui.QPixmap(chatbar_path))

        self.chatBoardPic = QtWidgets.QLabel(Form)
        self.chatBoardPic.setGeometry(QRect(WIDTH * 0.27, 0, WIDTH * 0.73, HEIGHT))
        self.chatBoardPic.setObjectName('charBoardPic')
        self.chatBoardPic.setScaledContents(True)
        self.chatBoardPic.setPixmap(QtGui.QPixmap(chatboard_path))

        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)  # 这个是聊天的
        self.textBrowser_2.setObjectName("conversation_0")
        self.textBrowser_2.setStyleSheet(gen_style(default_style))
        self.textBrowser_2.setGeometry(QRect(WIDTH * 0.3, HEIGHT * 0.03,
                                             WIDTH * 0.5, HEIGHT * 0.75))

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("conversation_rightbar_0")
        self.textBrowser.setStyleSheet(gen_style(default_style))
        self.textBrowser.setGeometry(QRect(WIDTH * 0.83, HEIGHT * 0.03,
                                           WIDTH * 0.15, HEIGHT * 0.75))

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("conversation_input_0")
        self.textEdit.setStyleSheet(gen_style(default_style))
        self.textEdit.setGeometry(QRect(WIDTH * 0.3, HEIGHT * 0.8,
                                        WIDTH * 0.5, HEIGHT * 0.18))

        _translate = QtCore.QCoreApplication.translate

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("conversation_pushButton_0")
        self.pushButton.setStyleSheet(gen_style(default_style))
        self.pushButton.setGeometry(QRect(WIDTH * 0.83, HEIGHT * 0.84,
                                          WIDTH * 0.15, HEIGHT * 0.14))
        self.pushButton.setCursor(Qt.OpenHandCursor)
        self.pushButton.setText(_translate("Form", "ENTER"))  # 调试

        self.newgroupButton = QtWidgets.QPushButton(Form)
        self.newgroupButton.setObjectName("conversation_pushButton_0")
        self.newgroupButton.setStyleSheet(gen_style(default_style))
        self.newgroupButton.setGeometry(QRect(WIDTH * 0.01, HEIGHT * 0.91,
                                              WIDTH * 0.25, HEIGHT * 0.07))
        self.newgroupButton.setCursor(Qt.OpenHandCursor)
        self.newgroupButton.setText(_translate("Form", "New Group"))

        self.uploadButton = QtWidgets.QPushButton(Form)
        self.uploadButton.setObjectName("conversation_uploadButton_0")
        self.uploadButton.setStyleSheet(gen_style(default_style, {'border-radius':'6px'}))
        self.uploadButton.setGeometry(QRect(WIDTH * 0.83, HEIGHT * 0.80,
                                            WIDTH * 0.15, HEIGHT * 0.03))
        self.uploadButton.setCursor(Qt.OpenHandCursor)
        self.uploadButton.setText(_translate("Form", "UPLOAD FILE"))

        self.leftButton = QtWidgets.QPushButton(Form)
        self.leftButton.setObjectName("conversation_leftButton_0")
        self.leftButton.setStyleSheet(gen_style(default_style))
        self.leftButton.setGeometry(QRect(WIDTH * 0.85, HEIGHT * 0.75,
                                          WIDTH * 0.05, HEIGHT * 0.02))
        self.leftButton.setCursor(Qt.OpenHandCursor)
        self.leftButton.setText(_translate("Form", "<-<-"))

        self.rightButton = QtWidgets.QPushButton(Form)
        self.rightButton.setObjectName("conversation_rightButton_0")
        self.rightButton.setStyleSheet(gen_style(default_style))
        self.rightButton.setGeometry(QRect(WIDTH * 0.92, HEIGHT * 0.75,
                                           WIDTH * 0.05, HEIGHT * 0.02))
        self.rightButton.setCursor(Qt.OpenHandCursor)
        self.rightButton.setText(_translate("Form", "->->"))

        QtCore.QMetaObject.connectSlotsByName(Form)

        self.create_userlist_label()
        self.create_chatlist_label()
        self.create_filelist()
        
        Form.setWindowTitle(_translate("Form", "Form"))

    def create_userlist_label(self):
        _translate = QtCore.QCoreApplication.translate
        WIDTH = self.width()
        HEIGHT = self.height()
        self.userlist = []
        for i in range(MAX_USER):
            icon_btn = QtWidgets.QPushButton(self.Form)
            icon_btn.setStyleSheet("QPushButton{border-radius:10px;border-image: url('./images/dark_star');}")
            icon_btn.setCursor(Qt.OpenHandCursor)
            icon_btn.setObjectName("user_icon_{0}".format(i))
            icon_btn.setGeometry(QRect(WIDTH * 0.845, HEIGHT * (0.04 + i * WIDTH/HEIGHT * 0.05),
                                       WIDTH * 0.045, WIDTH * 0.045))

            userid_btn = QtWidgets.QPushButton(self.Form)
            userid_btn.setText(_translate("Form", str(i)))
            userid_btn.setCursor(Qt.OpenHandCursor)
            userid_btn.setStyleSheet(gen_style(default_style, {
                'background-color': 'rgba(255,255,255,{0})'.format(opacity)}))
            userid_btn.setObjectName("user_userid_{0}".format(i))
            userid_btn.setGeometry(QRect(WIDTH * 0.89, HEIGHT * (0.05 + i * WIDTH/HEIGHT * 0.05),
                                         WIDTH * 0.08, WIDTH * 0.03))

            cur_user = UserEntry('', icon_btn, userid_btn)
            cur_user.hide()
            self.userlist.append(cur_user)

    def create_chatlist_label(self):
        _translate = QtCore.QCoreApplication.translate
        WIDTH = self.width()
        HEIGHT = self.height()
        self.chatlist = []
        for i in range(MAX_CHAT):
            icon_btn = QtWidgets.QPushButton(self.Form)
            icon_btn.setStyleSheet("QPushButton{border-radius:10px;border-image: url('./images/dark_star');}")
            icon_btn.setCursor(Qt.OpenHandCursor)
            icon_btn.setObjectName("chat_icon_{0}".format(i))
            icon_btn.setGeometry(QRect(WIDTH * 0.015, HEIGHT * (0.035 + i * WIDTH/HEIGHT * 0.06),
                                       WIDTH * 0.06, WIDTH * 0.06))

            userid_btn = QtWidgets.QPushButton(self.Form)
            userid_btn.setObjectName("chat_userid_{0}".format(i))
            userid_btn.setStyleSheet(gen_style(default_style, {
                'background-color': 'rgba(255,255,255,{0})'.format(opacity)}))
            userid_btn.setGeometry(QRect(WIDTH * 0.08, HEIGHT * (0.05 + i * WIDTH/HEIGHT * 0.06),
                                         WIDTH * 0.18, WIDTH * 0.045))
            userid_btn.setText(_translate("Form", 'default'))
            userid_btn.setCursor(Qt.OpenHandCursor)

            num_msg_label = QtWidgets.QLabel(self.Form)
            num_msg_label.setObjectName('chat_nummessage_{0}'.format(i))
            num_msg_label.setStyleSheet(gen_style(default_style, {
                'background-color': 'rgba(0,0,0,{0})'.format(opacity),
                'font-size': '12px',
                'color': 'white'}))
            num_msg_label.setGeometry(QRect(WIDTH * 0.23, HEIGHT * (0.063 + i * WIDTH/HEIGHT * 0.06),
                                            WIDTH * 0.03, WIDTH * 0.03))
            num_msg_label.setText(_translate("Form", ' 0'))

            close_btn = QtWidgets.QPushButton(self.Form)
            close_btn.setObjectName("chat_close_{0}".format(i))
            close_btn.setStyleSheet(gen_style(default_style, {
                'background-color': 'rgba(0,0,0,{0})'.format(opacity),
                'color': 'white'}))
            close_btn.setGeometry(QRect(WIDTH * 0.09, HEIGHT * (0.06 + i * WIDTH/HEIGHT * 0.06),
                                        WIDTH * 0.03, WIDTH * 0.03))
            close_btn.setText(_translate("Form", 'X'))
            close_btn.setCursor(Qt.OpenHandCursor)

            cur_chat = ChatLabelEntry([], icon_btn, userid_btn, num_msg_label, close_btn)
            cur_chat.hide()
            self.chatlist.append(cur_chat)

    def create_filelist(self):
        _translate = QtCore.QCoreApplication.translate
        WIDTH = self.width()
        HEIGHT = self.height()
        self.filelist = []
        for i in range(MAX_FILE):
            icon_btn = QtWidgets.QPushButton(self.Form)
            icon_btn.setObjectName("file_icon_{0}".format(i))
            icon_btn.setStyleSheet("QPushButton{border-radius:10px;border-image: url('./images/dark_star');}")
            icon_btn.setGeometry(QRect(WIDTH * 0.285, HEIGHT * (0.01 + i * WIDTH/HEIGHT * 0.07),
                                       WIDTH * 0.06, WIDTH * 0.06))
            icon_btn.setCursor(Qt.OpenHandCursor)

            userid_btn = QtWidgets.QPushButton(self.Form)
            userid_btn.setObjectName("file_userid_{0}".format(i))
            userid_btn.setStyleSheet(gen_style(default_style, {
                'background-color': 'rgba(255,255,255,{0})'.format(opacity),
                'text-align': 'left'}))
            userid_btn.setGeometry(QRect(WIDTH * 0.35, HEIGHT * (0.025 + i * WIDTH / HEIGHT * 0.07),
                                         WIDTH * 0.18, WIDTH * 0.045))
            userid_btn.setText(_translate("Form", 'default Name'))
            userid_btn.setCursor(Qt.OpenHandCursor)

            filename_btn = QtWidgets.QPushButton(self.Form)
            filename_btn.setObjectName("file_filename_{0}".format(i))
            filename_btn.setStyleSheet(gen_style(default_style, {
                'background-color': 'rgba(255,255,255,{0})'.format(opacity),
                'text-align': 'left'}))
            filename_btn.setGeometry(QRect(WIDTH * 0.54, HEIGHT * (0.025 + i * WIDTH/HEIGHT * 0.07),
                                           WIDTH * 0.3, WIDTH * 0.045))
            filename_btn.setText(_translate("Form", 'default FileName'))
            filename_btn.setCursor(Qt.OpenHandCursor)

            ac_btn = QtWidgets.QPushButton(self.Form)
            ac_btn.setObjectName('file_accept_{0}'.format(i))
            ac_btn.setStyleSheet(gen_style(default_style, {
                'background-color': 'rgba(0,0,0,{0})'.format(opacity),
                'color': 'white',
                'font-size': '12px'}))
            ac_btn.setGeometry(QRect(WIDTH * 0.85, HEIGHT * (0.03 + i * WIDTH/HEIGHT * 0.07),
                                     WIDTH * 0.04, WIDTH * 0.04))
            ac_btn.setText(_translate("Form", '✓'))  # √,✓,✔
            ac_btn.setCursor(Qt.OpenHandCursor)

            re_btn = QtWidgets.QPushButton(self.Form)
            re_btn.setObjectName("file_reject_{0}".format(i))
            re_btn.setStyleSheet(gen_style(default_style, {
                'background-color': 'rgba(0,0,0,{0})'.format(opacity),
                'color': 'white'}))
            re_btn.setGeometry(QRect(WIDTH * .9, HEIGHT * (.03 + i * WIDTH/HEIGHT * .07),
                                     WIDTH * .04, WIDTH * .04))
            re_btn.setText(_translate("Form", 'X'))
            re_btn.setCursor(Qt.OpenHandCursor)

            cur_file = FileEntry(['', '', 0], icon_btn, userid_btn, 
                                 filename_btn, ac_btn, re_btn)
            cur_file.hide()
            self.filelist.append(cur_file)

    def create_conversation_page(self, userid):
        _translate = QtCore.QCoreApplication.translate
        WIDTH = self.width()
        HEIGHT = self.height()
        Form = self.Form
        icon_path_0 = photo_base_path + userid + ".png"
        icon_path_1 = photo_base_path + self.clientId + ".png"

        textBrowser_00 = QtWidgets.QTextBrowser(Form)
        textBrowser_00.setObjectName("conversation_" + userid)
        textBrowser_00.setStyleSheet(gen_style(default_style, {
                'background-color': 'rgba(255,255,255,{0})'.format(opacity)}))
        textBrowser_00.setGeometry(QRect(WIDTH * 0.3, HEIGHT * 0.03,
                                         WIDTH * 0.5, HEIGHT * 0.75))
        textBrowser_00.hide()

        textBrowser_01 = QtWidgets.QTextBrowser(Form)
        textBrowser_01.setObjectName("conversation_rightbar_" + userid)
        textBrowser_01.setStyleSheet(gen_style(default_style, {
                'background-color': 'rgba(255,255,255,{0})'.format(opacity)}))
        textBrowser_01.setGeometry(QRect(WIDTH * 0.83, HEIGHT * 0.03,
                                         WIDTH * 0.15, HEIGHT * 0.75))
        textBrowser_01.hide()

        textEdit_10 = QtWidgets.QTextEdit(Form)
        textEdit_10.setObjectName("conversation_input_"+userid)
        textEdit_10.setStyleSheet(gen_style(default_style, {
                'background-color': 'rgba(255,255,255,{0})'.format(opacity)}))
        textEdit_10.setGeometry(QRect(WIDTH * 0.3, HEIGHT * 0.8,
                                      WIDTH * 0.5, HEIGHT * 0.18))
        textEdit_10.hide()

        pushButton_11 = QtWidgets.QPushButton(Form)
        pushButton_11.setObjectName("conversation_pushButton_" + userid)
        pushButton_11.setStyleSheet(gen_style(default_style, {
                'background-color': 'rgba(255,255,255,{0})'.format(opacity)}))
        pushButton_11.setGeometry(QRect(WIDTH * 0.83, HEIGHT * 0.84,
                                        WIDTH * 0.15, HEIGHT * 0.14))
        pushButton_11.setText(_translate("Form", "ENTER"))
        pushButton_11.setCursor(Qt.OpenHandCursor)
        pushButton_11.hide()

        uploadButton = QtWidgets.QPushButton(Form)
        uploadButton.setObjectName("conversation_uploadButton_0")
        uploadButton.setStyleSheet(gen_style(default_style, {
            'background-color': 'rgba(255,255,255,{0})'.format(opacity),
            'border-radius': '6px'}))
        uploadButton.setGeometry(QRect(WIDTH * 0.83, HEIGHT * 0.80,
                                       WIDTH * 0.15, HEIGHT * 0.03))
        uploadButton.setCursor(Qt.OpenHandCursor)
        uploadButton.clicked.connect(self.upload_file)
        uploadButton.setText(_translate("Form", "UPLOAD FILE"))
        uploadButton.hide()

        icon_btn_0 = QtWidgets.QPushButton(self.Form)
        icon_btn_0.setObjectName("conversation_icon_0_{0}".format(userid))
        icon_btn_0.setStyleSheet("QPushButton{border-radius:10px;border-image: url("+icon_path_0+");}")
        icon_btn_0.setGeometry(QRect(WIDTH * 0.84, HEIGHT * 0.05,
                                     WIDTH * 0.13, WIDTH * 0.13))
        icon_btn_0.setCursor(Qt.OpenHandCursor)
        icon_btn_0.hide()

        icon_btn_1 = QtWidgets.QPushButton(self.Form)
        icon_btn_1.setObjectName("conversation_icon_1_{0}".format(userid))
        icon_btn_1.setStyleSheet("QPushButton{border-radius:10px;border-image: url("+icon_path_1+");}")
        icon_btn_1.setGeometry(QRect(WIDTH * 0.84, HEIGHT * 0.58,
                                     WIDTH * 0.13, WIDTH * 0.13))
        icon_btn_1.setCursor(Qt.OpenHandCursor)
        icon_btn_1.hide()

        return [textBrowser_00, textBrowser_01, textEdit_10, pushButton_11, uploadButton, icon_btn_0, icon_btn_1]

    def create_groupchat_page(self, groupid):
        _translate = QtCore.QCoreApplication.translate
        WIDTH = self.width()
        HEIGHT = self.height()
        Form = self.Form

        textBrowser_00 = QtWidgets.QTextBrowser(Form)
        textBrowser_00.setObjectName("groupchat_" + groupid)
        textBrowser_00.setStyleSheet(gen_style(default_style, {
            'background-color': 'rgba(255,255,255,{0})'.format(opacity)}))
        textBrowser_00.setGeometry(QRect(WIDTH * 0.3, HEIGHT * 0.03,
                                         WIDTH * 0.5, HEIGHT * 0.75))
        textBrowser_00.hide()

        textBrowser_01 = QtWidgets.QTextBrowser(Form)
        textBrowser_01.setObjectName("groupchat_rightbar_" + groupid)
        textBrowser_01.setStyleSheet(gen_style(default_style, {
            'background-color': 'rgba(255,255,255,{0})'.format(opacity)}))
        textBrowser_01.setGeometry(QRect(WIDTH * 0.83, HEIGHT * 0.03,
                                         WIDTH * 0.15, HEIGHT * 0.75))
        textBrowser_01.hide()

        textEdit_10 = QtWidgets.QTextEdit(Form)
        textEdit_10.setObjectName("groupchat_input_" + groupid)
        textEdit_10.setStyleSheet(gen_style(default_style, {
            'background-color': 'rgba(255,255,255,{0})'.format(opacity)}))
        textEdit_10.setGeometry(QRect(WIDTH * 0.3, HEIGHT * 0.8,
                                      WIDTH * 0.5 , HEIGHT * 0.18))
        textEdit_10.hide()

        pushButton_11 = QtWidgets.QPushButton(Form)
        pushButton_11.setObjectName("groupchat_pushButton_" + groupid)
        pushButton_11.setStyleSheet(gen_style(default_style, {
            'background-color': 'rgba(255,255,255,{0})'.format(opacity)}))
        pushButton_11.setGeometry(QRect(WIDTH * 0.83, HEIGHT * 0.84,
                                        WIDTH * 0.15, HEIGHT * 0.14))
        pushButton_11.setText(_translate("Form", "ENTER"))
        pushButton_11.setCursor(Qt.OpenHandCursor)
        pushButton_11.hide()

        uploadButton = QtWidgets.QPushButton(Form)
        uploadButton.setObjectName("groupchat_uploadButton_" + groupid)
        uploadButton.setStyleSheet(gen_style(default_style, {
            'background-color': 'rgba(255,255,255,{0})'.format(opacity),
            'border-radius': '6px'}))
        uploadButton.setGeometry(QRect(WIDTH * 0.83, HEIGHT * 0.80,
                                       WIDTH * 0.15, HEIGHT * 0.03))
        uploadButton.setCursor(Qt.OpenHandCursor)
        uploadButton.clicked.connect(self.upload_file)
        uploadButton.setText(_translate("Form", "UPLOAD FILE"))
        uploadButton.hide()

        leftButton = QtWidgets.QPushButton(Form)
        leftButton.setObjectName("groupchat_leftButton_" + groupid)
        leftButton.setStyleSheet(gen_style(default_style))
        leftButton.setGeometry(QRect(WIDTH * 0.85, HEIGHT * 0.75,
                                     WIDTH * 0.05, HEIGHT * 0.02))
        leftButton.setCursor(Qt.OpenHandCursor)
        leftButton.setText(_translate("Form", "<-<-")) 
        leftButton.clicked.connect(self.last_page)
        leftButton.hide()

        rightButton = QtWidgets.QPushButton(Form)
        rightButton.setObjectName("groupchat_rightButton_" + groupid)
        rightButton.setStyleSheet(gen_style(default_style))
        rightButton.setGeometry(QRect(WIDTH * 0.92, HEIGHT * 0.75,
                                      WIDTH * 0.05, HEIGHT * 0.02))
        rightButton.setCursor(Qt.OpenHandCursor)
        rightButton.setText(_translate("Form", "->->")) 
        rightButton.clicked.connect(self.next_page) 
        rightButton.hide()

        items = [textBrowser_00, textBrowser_01, textEdit_10, pushButton_11, uploadButton, leftButton, rightButton]
        userlist = []
        for i in range(MAX_USER):
            icon_btn = QtWidgets.QPushButton(self.Form)
            icon_btn.setStyleSheet("QPushButton{border-radius:10px;border-image: url('./images/dark_star');}")
            icon_btn.setCursor(Qt.OpenHandCursor)
            icon_btn.setObjectName("group_{0}_user_icon_{1}".format(groupid, i))
            icon_btn.setGeometry(QRect(WIDTH * 0.845, HEIGHT * (0.04 + i * WIDTH/HEIGHT * 0.05),
                                       WIDTH * 0.045, WIDTH * 0.045))
            icon_btn.hide()
            icon_btn.clicked.connect(self.CHANGE_PAGE)

            userid_btn = QtWidgets.QPushButton(self.Form)
            userid_btn.setObjectName("group_{0}_user_userid_{1}".format(groupid, i))
            userid_btn.setStyleSheet(gen_style(default_style, {
                'background-color': 'rgba(255,255,255,{0})'.format(opacity),
                'border-radius': '6px'}))
            userid_btn.setGeometry(QRect(WIDTH * 0.89, HEIGHT * (0.05 + i * WIDTH/HEIGHT * 0.05),
                                         WIDTH * 0.08, WIDTH * 0.03))
            userid_btn.setText(_translate("Form", str(i)))
            userid_btn.setCursor(Qt.OpenHandCursor)
            userid_btn.hide()
            userid_btn.clicked.connect(self.CHANGE_PAGE)

            cur_user = UserEntry('', icon_btn, userid_btn)
            cur_user.hide()
            userlist.append(cur_user)

            items.append(icon_btn)
            items.append(userid_btn)

        return items, userlist

