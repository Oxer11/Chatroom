
class UserEntry():
    def __init__(self, username, icon, userid):
        self.username = username
        self.icon = icon
        self.userid = userid

    def show(self):
        self.icon.show()
        self.userid.show()

    def hide(self):
        self.icon.hide()
        self.userid.hide()


class ChatLabelEntry():
    def __init__(self, users, icon, userid, num_msg, close):
        self.users = users
        self.icon = icon
        self.userid = userid
        self.num_msg = num_msg
        self.close = close

    def show(self):
        self.icon.show()
        self.userid.show()
        self.num_msg.show()
        self.close.show()

    def hide(self):
        self.icon.hide()
        self.userid.hide()
        self.num_msg.hide()
        self.close.hide()


class FileEntry():
    def __init__(self, data, icon, userid, name, ac, re):
        self.data_user = data[0]
        self.data_name = data[1]
        self.data_size = data[2]
        self.icon = icon
        self.userid = userid
        self.name = name
        self.ac = ac
        self.re = re

    def set_data(self, data):
        self.data_user = data[0]
        self.data_name = data[1]
        self.data_size = data[2]

    def show(self):
        self.icon.show()
        self.userid.show()
        self.name.show()
        self.ac.show()
        self.re.show()

    def hide(self):
        self.icon.hide()
        self.userid.hide()
        self.name.hide()
        self.ac.hide()
        self.re.hide()


class ConvEntry():
    def __init__(self, name, path, num_msg):
        self.name = name
        self.path = path
        self.num_msg = num_msg
