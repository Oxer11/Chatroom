import socket
import sys
import select
import threading

from Constant import *
from PyQt5.QtWidgets import QApplication
from login_win import *
from chat_win import *
from util import *


HOST = '127.0.0.1'
PORT = 9078
BUFFER_SIZE = 1024

my_group = {}


def listener():
    while True:
        # Response
        r, w, e = select.select([sock], [], [])
        for s in r:
            try:
                recv_data = s.recv(BUFFER_SIZE)
                op = int(recv_data[:3].decode('utf-8'))
                if op in [DOWNFILE_SUCCESS, UP_PHOTO]:
                    data = recv_data[5:]
                else:
                    data = recv_data.decode('utf-8').split('\r\n')
                print(op)
                if op == LOGIN_SUCCESS:
                    ui_chat.setClientId(ui_login.clientId)
                    ui_login.CLOSE.emit()
                    ui_login.ui_register.CLOSE.emit()
                    ui_chat.SHOW.emit()
                    ask_users(sock)
                elif op == LOGIN_WRONG:
                    ui_login.ERROR.emit('用户名或密码错误！')
                elif op == LOGIN_REPEAT:
                    ui_login.ERROR.emit('重复登录！')
                elif op == LOGIN_INFO:
                    ui_chat.APPEND.emit(data[1] + ' has logged in!')
                    ask_users(sock)
                elif op == LOGOUT_INFO:
                    ui_chat.APPEND.emit(data[1] + ' has logged out!')
                    ask_users(sock)
                elif op == SEND_ALL:
                    ui_chat.APPEND.emit('<pre><em>' + data[1] + ' says:</em>\n' + data[2] + '</pre>')
                elif op == SEND_PER:
                    ui_chat.new_conv.emit(data[1], ' says:</em>\n' + data[2] + '</pre>')
                elif op == SENDFILE_ALL:
                    ui_chat.APPEND.emit('<pre><em>' + data[1] + ' uploads a file:</em>' + data[2] + '\n<em>size:</em>' + data[3] + '</pre>')
                    ui_chat.new_file.emit(data[1], data[2], data[3])
                elif op == SENDFILE_PER:
                    ui_chat.new_conv.emit(data[1], ' uploads a file:</em>' + data[2] + '\n<em>size:</em>' + data[3] + '</pre>')
                    ui_chat.new_file.emit(data[1], data[2], data[3])
                elif op == ASKUSERS_RET:
                    ui_chat.ask_users.emit((data[2]+'\n')*1)
                elif op == REGISTER_SUCCESS:
                    ui_login.ui_register.CLOSE.emit()
                elif op == DOWNFILE_SUCCESS:
                    file_name, file_size, cur_data = receive_file(s, data)
                    flie_dic = "./client/files/__{0}__".format(ui_chat.clientId)
                    if not os.path.exists(flie_dic):
                        os.makedirs(flie_dic)
                    path = os.path.join(flie_dic, file_name)
                    with open(path, "wb") as f:
                        f.write(cur_data)
                elif op == GROUP_SUCCESS:
                    my_group[data[1]] = True
                    ui_chat.NEW_GROUP.emit(data[1])
                    ask_group_users(sock, data[1])
                elif op == ASKGROUPUSERS_RET:
                    ui_chat.ASK_GROUP_USERS.emit(data[1], data[2])
                elif op == SENDGROUPMSG_SUCCESS:
                    ui_chat.NEW_GROUP_MSG.emit(data[1], data[2], ' says:</em>\n' + data[3])
                elif op == GROUP_LOGIN:
                    ui_chat.NEW_GROUP_USER.emit(data[1], data[2])
                elif op == GROUP_LOGOUT:
                    ui_chat.OUT_GROUP_USER.emit(data[1], data[2])
                elif op == SENDFILE_GROUP:
                    ui_chat.NEW_GROUP_MSG.emit(data[1], data[2], ' uploads a file:</em>' + data[3] + '\n<em>size:</em>' + data[4])
                    ui_chat.new_file.emit(data[1], data[3], data[4])
                elif op == UP_PHOTO:
                    sep = data.find('\r\n'.encode('utf-8'))
                    user, data = data[:sep].decode('utf-8'), data[sep+2:]
                    file_name, file_size, cur_data = receive_file(s, data)
                    path = "./client/photo/{0}.png".format(user)
                    with open(path, "wb") as f:
                        f.write(cur_data)
                    ui_chat.FLUSH.emit()
            except Exception as e:
                print(e)
                return


if __name__ == '__main__':
    sock = socket.socket()
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    try:
        sock.connect((HOST, PORT))
        print('Connected with server')
    except Exception as e:
        print("Fail to connect (%s, %s) due to" % (HOST, PORT), e)
        exit()

    app = QApplication(sys.argv)

    ui_login = LoginPage(sock)
    ui_chat = ChatPage(sock)

    listen = threading.Thread(target=listener, args=(), daemon=True)
    listen.start()

    ui_login.show()  # 这个用了才能展示界面
    app.exec_()

    sock.close()
    sys.exit()
