import socket
import sys
import select
import threading

from Constant import *
#from chat_page import *
from PyQt5.QtWidgets import QApplication, QWidget
from loginwindow import *
from chatwindow import *
import time


HOST = '127.0.0.1'
PORT = 9058
BUFFER_SIZE = 1024


def send(msg):
    msg = msg.encode('utf-8')
    sock.sendall(msg) #通过这个套接字将信息全部发送出去
    print('send:', msg)


def log_in():
    
    username = ui_login.id_box.text()
    password = ui_login.password_box.text()
    send('\r\n'.join([str(LOGIN), username, password])) #发送登录信息


def register():
    user, pwd, re_pwd = input('username: '), input('password: '), input('repeat password: ')
    if pwd == re_pwd:
        send('\r\n'.join([str(REGISTER), user, pwd])) #发送注册信息
    else:
        print('Password is inconsistent!')


def send_msg():
    send_data, receiver = [str(SENDMSG)], []
    cur = input('receiver: ')
    while len(cur) > 0:
        receiver.append(cur)
        cur = input('receiver: ')
    send_data.append('\t'.join(receiver))
    data = input('message: ')
    send_data.append(data)
    send('\r\n'.join(send_data))


def send_all():
    data = ui_chat.textEdit.toPlainText()
    ui_chat.APPEND.emit('I say:\n' + data)
    send(str(SENDALL) + '\r\n' + data)


def ask_users():
    send(str(ASKUSERS))


def log_out():
    send(str(LOGOUT))


def close():
    sock.close()
    sys.exit()


handle_dic = {LOGIN: log_in,
              REGISTER: register,
              SENDMSG: send_msg,
              SENDALL: send_all,
              LOGOUT: log_out,
              ASKUSERS: ask_users,
              CLOSE: close}


def listener():
    while True:
        # Response
        r, w, e = select.select([sock], [], [])
        for s in r:
            try:
                recv_data = s.recv(BUFFER_SIZE).decode('utf-8')
                print('Receive:', recv_data)
                data = recv_data.split('\r\n')
                op = int(data[0])
                if op == LOGIN_SUCCESS:
                    ui_login.CLOSE.emit()
                    ui_chat.SHOW.emit()
                    ask_users()
                elif op == LOGIN_WRONG:
                    print('Login Error')
                elif op == LOGIN_REPEAT:
                    print('Login Repeat')
                elif op == LOGIN_INFO:
                    ui_chat.APPEND.emit(data[1] + ' has logged in!')
                    ask_users()
                elif op == LOGOUT_INFO:
                    ui_chat.APPEND.emit(data[1] + ' has logged out!')
                    ask_users()
                elif op == SEND_ALL:
                    ui_chat.APPEND.emit(data[1] + ' says:\n' + data[2])
                elif op == ASKUSERS_RET:
                    ui_chat.ask_users.emit(data[2])
            except Exception as e:
                print(e)
                return


if __name__ == '__main__':
    sock = socket.socket()
    try:
        sock.connect((HOST, PORT))
        print('Connected with server')
    except Exception as e:
        print("Fail to connect (%s, %s) due to" % (HOST, PORT), e)
        exit()

    app = QApplication(sys.argv)
    ui_login = LoginPage()
    ui_login.login_button.clicked.connect(log_in)
    ui_login.login_button.clicked.connect(ui_login.id_box.clear)
    ui_login.login_button.clicked.connect(ui_login.password_box.clear)

    ui_chat = ChatPage()
    ui_chat.pushButton.clicked.connect(send_all)
    ui_chat.pushButton.clicked.connect(ui_chat.textEdit.clear)

    listen = threading.Thread(target=listener, args=(), daemon=True)
    listen.start()

    ui_login.show()  # 这个用了才能展示界面
    #ui_chat.show()
    app.exec_()

    # action()
    sock.close()
    sys.exit()
