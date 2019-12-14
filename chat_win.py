from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from chat_ui import *


class ChatPage(QWidget, Ui_chatWindow):
    APPEND = QtCore.pyqtSignal(str)
    new_conv = QtCore.pyqtSignal(str, str)
    new_file = QtCore.pyqtSignal(str, str, str)
    NEW_GROUP = QtCore.pyqtSignal(str)
    ask_users = QtCore.pyqtSignal(str)
    ASK_GROUP_USERS = QtCore.pyqtSignal(str, str)
    NEW_GROUP_MSG = QtCore.pyqtSignal(str, str, str)
    NEW_GROUP_USER = QtCore.pyqtSignal(str, str)
    OUT_GROUP_USER = QtCore.pyqtSignal(str, str)
    SHOW = QtCore.pyqtSignal()
    CHANGE_PAGE = QtCore.pyqtSignal()
    DELETE_CONVERSATION = QtCore.pyqtSignal()

    conv_list = []  # 组件信息的列表 记录了组件的 用户名、头像路径和消息数量,or other information
    conv_pages = []  # 每一个页是一个组件的列表 pagelist是列表的列表 其顺序对应chatbar中的顺序
    conv_people = []
    conv_type = []  # public \ file \ private \ group
    grp_userbtn_list = {}
    grp_user_list = {}
    grp_page = {}

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
        self.NEW_GROUP.connect(self.new_group)
        self.ASK_GROUP_USERS.connect(self.update_group)
        self.NEW_GROUP_MSG.connect(self.new_group_msg)
        self.NEW_GROUP_USER.connect(self.new_group_user)
        self.OUT_GROUP_USER.connect(self.out_group_user)
        self.CHANGE_PAGE.connect(self.change_page)
        self.DELETE_CONVERSATION.connect(self.delete_conversation)
        self.pushButton.clicked.connect(self.SEND)
        self.pushButton.clicked.connect(self.textEdit.clear)
        self.uploadButton.clicked.connect(self.upload_file)
        self.leftButton.clicked.connect(self.last_page)
        self.rightButton.clicked.connect(self.next_page)
        for item in self.userlist:
            item.icon.clicked.connect(self.CHANGE_PAGE)
            item.userid.clicked.connect(self.CHANGE_PAGE)

        for item in self.chatlist:
            item.icon.clicked.connect(self.CHANGE_PAGE)
            item.userid.clicked.connect(self.CHANGE_PAGE)
            item.close.clicked.connect(self.group_logout)
            item.close.clicked.connect(self.DELETE_CONVERSATION)

        for item in self.filelist:
            item.ac.clicked.connect(self.accept_file)
            item.re.clicked.connect(self.reject_file)

        self.user_peoplelist = []

        self.filedata_list = []

        self.cur_pageid = 0
        page = [self.textBrowser_2, self.textBrowser, self.textEdit, self.pushButton,
                self.uploadButton, self.leftButton, self.rightButton]
        file_page = []
        for tup in self.filelist:
            file_page += [tup.icon, tup.userid, tup.name, tup.ac, tup.re]
        for item in self.userlist:
            page += [item.icon, item.userid]
        self.conv_pages.append(page)
        self.conv_pages.append(file_page)
        self.conv_list.append(ConvEntry('PUBLIC', star_path, 0))
        self.conv_list.append(ConvEntry('FILE', filepage_path, 0))
        self.conv_people.append('PUBLIC')
        self.conv_people.append('FILE')
        self.conv_type = ['public', 'file']
        self.update_chatlist()

        self.userpage_index = 1
        self.newgroupButton.clicked.connect(self.find_newgroup)
        self.new_groupWindow = NewGroupPage(self.sock)

    def group_logout(self):
        sender = self.sender()
        name = sender.objectName()
        idx = int(name.split('_')[2])
        groupid = self.conv_list[idx].name
        group_log_out(self.sock, groupid, self.clientId)

    def find_newgroup(self):
        self.new_groupWindow.show()

    def last_page(self):
        sender = self.sender()
        name = sender.objectName()
        prefix = name.split('_')[0]
        if prefix == 'conversation':
            if self.userpage_index > 1:
                self.userpage_index -= 1
                self.update_userlist()
        elif prefix == 'groupchat':
            groupid = 'gp_' + name.split('_')[-1]
            chat_index = self.conv_people.index(groupid)
            if self.grp_page[chat_index] > 1:
                self.grp_page[chat_index] -= 1
                self.update_group_userlist(chat_index)

    def next_page(self):
        sender = self.sender()
        name = sender.objectName()
        prefix = name.split('_')[0]
        if prefix == 'conversation':
            if self.userpage_index < (len(self.users) - 1) // MAX_USER + 1:
                self.userpage_index += 1
                self.update_userlist()
        elif prefix == 'groupchat':
            groupid = 'gp_' + name.split('_')[-1]
            chat_index = self.conv_people.index(groupid)
            if self.grp_page[chat_index] < (len(self.grp_user_list[chat_index]) - 1) // MAX_USER + 1:
                self.grp_page[chat_index] += 1
                self.update_group_userlist(chat_index)

    def upload_file(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '')
        id = self.cur_pageid
        if id == 0:
            self.APPEND.emit('I upload file:\n' + openfile_name[0])
            send_file_all(self.sock, openfile_name[0])
        elif self.conv_type[id] == 'private':
            self.conv_pages[id][0].append('I upload file:\n' + openfile_name[0])
            send_file(self.sock, [self.conv_list[id].name], openfile_name[0])
        else:
            self.conv_pages[id][0].append('I say:\n' + openfile_name[0])
            group_id = self.conv_list[id].name
            chat_index = self.conv_people.index(group_id)
            send_file_group(self.sock, group_id, [x[0] for x in self.grp_user_list[chat_index]], openfile_name[0])

    def receive_new_file(self, user, filename, filesize):
        self.filedata_list.append([user, filename, filesize])
        if self.cur_pageid == 1:
            self.flush_page(cur_pageid)
        self.conv_list[1].num_msg += 1
        self.chatlist[1].num_msg.setText(
            QtCore.QCoreApplication.translate("Form", ' {0}'.format(self.conv_list[1].num_msg)))

    def SEND(self):
        id = self.cur_pageid
        if id == 0:
            data = self.textEdit.toPlainText()
            self.APPEND.emit('I say:\n' + data)
            send_all(self.sock, data)
        elif self.conv_type[id] == 'private':
            data = self.conv_pages[id][2].toPlainText()
            self.conv_pages[id][0].append('I say:\n' + data)
            send_msg(self.sock, [self.conv_list[id].name], data)
        else:
            data = self.conv_pages[id][2].toPlainText()
            self.conv_pages[id][0].append('I say:\n' + data)
            group_id = self.conv_list[id].name
            chat_index = self.conv_people.index(group_id)
            send_group_msg(self.sock, group_id, [x[0] for x in self.grp_user_list[chat_index]], data)

    def public_append(self, msg):
        if self.cur_pageid != 0:
            self.conv_list[0].num_msg += 1
            self.chatlist[0].num_msg.setText(
                QtCore.QCoreApplication.translate("Form", ' {0}'.format(self.conv_list[0].num_msg)))

        self.conv_pages[0][0].append(msg)

    def new_conversation(self, user, msg):
        if user not in self.conv_people:
            self.conv_people.append(user)
            icon_path = photo_base_path + user + ".png"

            self.conv_list.append(ConvEntry(user, icon_path, 0))
            self.update_chatlist()

            page = self.create_conversation_page(user)
            page[3].clicked.connect(self.SEND)
            page[3].clicked.connect(page[2].clear)
            self.conv_pages.append(page)
            self.conv_type.append('private')

        chat_index = self.conv_people.index(user)
        if chat_index != self.cur_pageid:
            self.conv_list[chat_index].num_msg += 1
            self.chatlist[chat_index].num_msg.setText(
                QtCore.QCoreApplication.translate("Form", ' {0}'.format(self.conv_list[chat_index].num_msg)))

        self.conv_pages[chat_index][0].append(user + msg)

    def new_group_msg(self, user, groupid, msg):
        chat_index = self.conv_people.index(groupid)
        if chat_index != self.cur_pageid:
            self.conv_list[chat_index].num_msg += 1
            self.chatlist[chat_index].num_msg.setText(
                QtCore.QCoreApplication.translate("Form", ' {0}'.format(self.conv_list[chat_index].num_msg)))

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
        if self.conv_type[btn_idx] == 'group':
            del self.grp_userbtn_list[btn_idx]
            del self.grp_user_list[btn_idx]
            del self.grp_page[btn_idx]
        for chat_idx in self.grp_page.copy():
            self.grp_page[chat_idx-1] = self.grp_page[chat_idx]
            self.grp_userbtn_list[chat_idx-1] = self.grp_userbtn_list[chat_idx]
            self.grp_user_list[chat_idx-1] = self.grp_user_list[chat_idx]
            del self.grp_page[chat_idx]
            del self.grp_userbtn_list[chat_idx]
            del self.grp_user_list[chat_idx]
        self.conv_type.pop(btn_idx)

    def update_userlist(self, data=None):
        _translate = QtCore.QCoreApplication.translate
        for i in range(MAX_USER):
            self.userlist[i].username = ''
            self.userlist[i].hide()

        self.user_peoplelist = [['PUBLIC', star_path]]
        if data is not None:
            self.users = data.split('\n')  # 希望保存这个数据

        cur_idx = (self.userpage_index - 1) * MAX_USER
        for i, userid in enumerate(self.users[cur_idx:cur_idx+MAX_USER]):
            if len(userid) == 0: continue
            self.userlist[i].username = userid
            icon_path = photo_base_path + userid + ".png"
            self.user_peoplelist.append([userid, icon_path])

        log_out_user = None
        for i, item in enumerate(self.conv_list):
            if i != 0 and i != 1 and item.name not in self.users and item.name not in self.conv_people:
                print(item.name, self.users)
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

        for i, userid in enumerate(self.users[cur_idx:cur_idx+MAX_USER]):
            if len(userid) == 0: continue
            self.userlist[i].username = userid
            icon_path = photo_base_path + userid + ".png"
            self.userlist[i].userid.setText(_translate("Form", userid))
            self.userlist[i].icon.setStyleSheet(
                "QPushButton{border-radius:10px;border-image: url('" + icon_path + "');}")
            if self.cur_pageid == 0:
                self.userlist[i].show()

    def new_group_user(self, user, groupid):
        chat_index = self.conv_people.index(groupid)
        icon_path = photo_base_path + user + ".png"
        self.grp_user_list[chat_index].append((user, icon_path))
        self.update_group_userlist(chat_index)

    def out_group_user(self, user, groupid):
        chat_index = self.conv_people.index(groupid)
        icon_path = photo_base_path + user + ".png"
        self.grp_user_list[chat_index].remove((user, icon_path))
        self.update_group_userlist(chat_index)

    def update_group(self, groupid, data):
        chat_index = self.conv_people.index(groupid)
        grp_user_list = []
        for user in data.split("\n"):
            icon_path = photo_base_path + user + ".png"
            grp_user_list.append((user, icon_path))
        self.grp_user_list[chat_index] = grp_user_list
        self.update_group_userlist(chat_index)

    def update_group_userlist(self, chat_index):
        _translate = QtCore.QCoreApplication.translate
        for i in range(MAX_USER):
            self.grp_userbtn_list[chat_index][i].username = ''
            self.grp_userbtn_list[chat_index][i].hide()

        cur_idx = (self.grp_page[chat_index] - 1) * MAX_USER
        for i, item in enumerate(self.grp_user_list[chat_index][cur_idx:cur_idx+MAX_USER]):
            if len(item[0]) == 0: continue
            self.grp_userbtn_list[chat_index][i].username = item[0]
            if self.cur_pageid == chat_index:
                self.grp_userbtn_list[chat_index][i].userid.setText(_translate("Form", item[0]))
                self.grp_userbtn_list[chat_index][i].icon.setStyleSheet(
                    "QPushButton{border-radius:10px;border-image: url('" + item[1] + "');}")
                self.grp_userbtn_list[chat_index][i].show()

    def update_filelist(self):
        _translate = QtCore.QCoreApplication.translate
        filedata_list = self.filedata_list
        for i in range(MAX_FILE):
            self.filelist[i].hide()

        for i, file_data in enumerate(filedata_list):
            self.filelist[i].show()
            self.filelist[i].set_data(file_data)
            userid = file_data[0]
            filename = file_data[1]
            icon_path = photo_base_path + userid + ".png"
            self.filelist[i].icon.setStyleSheet("QPushButton{border-radius:10px;border-image: url(" + icon_path + ");}")
            self.filelist[i].userid.setText(_translate("Form", userid))
            self.filelist[i].name.setText(_translate("Form", filename))
            self.filelist[i].show()

    def update_chatlist(self):
        _translate = QtCore.QCoreApplication.translate
        for i in range(MAX_CHAT):
            self.chatlist[i].users = []
            self.chatlist[i].hide()

        for i, item in enumerate(self.conv_list):
            self.chatlist[i].userid.setText(_translate("Form", item.name))
            self.chatlist[i].icon.setStyleSheet("QPushButton{border-radius:10px;border-image: url(" + item.path + ");}")
            self.chatlist[i].num_msg.setText(_translate("Form", '  ' + str(item.num_msg)))
            self.chatlist[i].show()

        self.chatlist[0].close.hide()
        self.chatlist[1].close.hide()

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
        prefix = name.split('_')[0]
        midfix = name.split('_')[1]

        if prefix == 'user' or prefix == 'group':
            if prefix == 'user':
                username = self.userlist[btn_idx].username  # 用户名
            elif prefix == 'group':
                groupid = 'gp_' + name.split('_')[2]
                chat_index = self.conv_people.index(groupid)
                username = self.grp_userbtn_list[chat_index][btn_idx].username
            if username == self.clientId:
                return
            if username not in self.conv_people:
                if len(self.conv_list) == MAX_CHAT:
                    self.conv_list.pop(2)
                    self.conv_people.pop(2)
                    self.update_chatlist()
                    self.flush_page(0)
                    self.conv_pages.pop(2)

                self.conv_people.append(username)
                # chatbar按时间序

                if midfix == 'icon':
                    icon_ss = sender.styleSheet()
                    icon_path = icon_ss.split("'")[1]  # 如果点的不是头像就找不到了..
                else:
                    icon_path = photo_base_path + username + ".png"

                self.conv_list.append(ConvEntry(username, icon_path, 0))

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

        self.conv_list[chat_index].num_msg = 0
        if self.cur_pageid == 1:
            self.update_filelist()
        else:
            self.update_chatlist()
        self.flush_page(chat_index)

    def flush_page(self, chat_index):
        for item in self.conv_pages[self.cur_pageid]:
            item.hide()

        page_type = self.conv_type[chat_index]

        if page_type == 'public':
            for item in self.conv_pages[chat_index][:7]:
                item.show()
            print(self.user_peoplelist)
            for items in self.userlist[:len(self.user_peoplelist) - 1]:
                items.show()
        elif page_type == 'file':
            self.update_filelist()
            filelist = self.filelist[:len(self.filedata_list)]
            for tup in filelist:
                tup.show()
        elif page_type == 'private':
            for item in self.conv_pages[chat_index]:
                item.show()
        elif page_type == 'group':
            for item in self.conv_pages[chat_index][:7]:
                item.show()

            cur_idx = (self.grp_page[chat_index] - 1) * MAX_USER
            for i, item in enumerate(self.grp_user_list[chat_index][cur_idx:cur_idx+MAX_USER]):
                if item[0] == '': break
                self.grp_userbtn_list[chat_index][i].icon.setStyleSheet(
                    "QPushButton{border-radius:10px;border-image: url('" + item[1] + "');}")
                self.grp_userbtn_list[chat_index][i].username = item[0]
                _translate = QtCore.QCoreApplication.translate
                self.grp_userbtn_list[chat_index][i].userid.setText(_translate("Form", item[0]))
                self.grp_userbtn_list[chat_index][i].show()

        self.cur_pageid = chat_index

    def setClientId(self, clientId):
        self.clientId = clientId

    def new_group(self, groupid):  # 就让groupid的格式为'gp_4356'这样吧
        if groupid not in self.conv_people:
            self.conv_people.append(groupid)

            self.conv_list.append(ConvEntry(groupid, groupicon_path, 0))
            self.update_chatlist()

            page, grp_userbtn_list = self.create_groupchat_page(groupid)
            page[3].clicked.connect(self.SEND)
            page[3].clicked.connect(page[2].clear)
            self.conv_pages.append(page)
            self.conv_type.append('group')

        chat_index = self.conv_people.index(groupid)

        self.grp_userbtn_list[chat_index] = grp_userbtn_list
        self.grp_user_list[chat_index] = []
        self.grp_page[chat_index] = 1
        if chat_index != self.cur_pageid:
            self.chatlist[chat_index].num_msg.setText(
                QtCore.QCoreApplication.translate("Form", ' {0}'.format(self.conv_list[chat_index].num_msg)))

        self.flush_page(chat_index)

    def resizeEvent(self, event):
        width = self.width()
        height = self.height()
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
            icon_btn = tup.icon
            userid_btn = tup.userid
            width_ = width

            if height * 1.4133 < width:
                width_ = height * 1.4133

            icon_btn.setGeometry(
                QRect(width * 0.845, height * (0.04 + i * width_ / height * 0.05), width_ * 0.045, width_ * 0.045))
            userid_btn.setGeometry(
                QRect(width * 0.89, height * (0.05 + i * width_ / height * 0.05), width_ * 0.08, width_ * 0.03))

        for i, tup in enumerate(self.chatlist):
            tup.icon.setGeometry(
                QRect(width * 0.015, height * (0.035 + i * width / height * 0.06), width * 0.06, width * 0.06))
            tup.userid.setGeometry(
                QRect(width * 0.08, height * (0.05 + i * width / height * 0.06), width * 0.18, width * 0.045))
            tup.num_msg.setGeometry(
                QRect(width * 0.23, height * (0.063 + i * width / height * 0.06), width * 0.03, width * 0.03))
            tup.close.setGeometry(
                QRect(width * 0.09, height * (0.06 + i * width / height * 0.06), width * 0.03, width * 0.03))

        for i, tup in enumerate(self.conv_pages[2:]):
            textBrowser_00 = tup[0]
            textBrowser_01 = tup[1]
            textEdit_10 = tup[2]
            pushButton_11 = tup[3]
            uploadButton = tup[4]
            icon_btn_0 = tup[5]
            icon_btn_1 = tup[6]
            textBrowser_00.setGeometry(QRect(width * 0.3, height * 0.03, width * 0.5, height * 0.75))
            textBrowser_01.setGeometry(QRect(width * 0.83, height * 0.03, width * 0.15, height * 0.75))
            textEdit_10.setGeometry(QRect(width * 0.3, height * 0.8, width * 0.5, height * 0.18))
            pushButton_11.setGeometry(QRect(width * 0.83, height * 0.84, width * 0.15, height * 0.14))
            uploadButton.setGeometry(QRect(width * 0.83, height * 0.80, width * 0.15, height * 0.03))
            icon_btn_0.setGeometry(QRect(width * 0.84, height * 0.05, width * 0.13, width * 0.13))
            icon_btn_1.setGeometry(QRect(width * 0.84, height * 0.58, width * 0.13, width * 0.13))

        for i, tup in enumerate(self.filelist):
            tup.icon.setGeometry(
                QRect(width * 0.285, height * (0.01 + i * width / height * 0.07), width * 0.06, width * 0.06))
            tup.userid.setGeometry(
                QRect(width * 0.35, height * (0.025 + i * width / height * 0.07), width * 0.18, width * 0.045))
            tup.name.setGeometry(
                QRect(width * 0.54, height * (0.025 + i * width / height * 0.07), width * 0.3, width * 0.045))
            tup.ac.setGeometry(
                QRect(width * 0.85, height * (0.03 + i * width / height * 0.07), width * 0.04, width * 0.04))
            tup.re.setGeometry(
                QRect(width * 0.9, height * (0.03 + i * width / height * 0.07), width * 0.04, width * 0.04))

