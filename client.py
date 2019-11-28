import socket
import sys
import select
import threading

from Constant import *
from PyQt5.QtWidgets import QApplication
from loginwindow import *
from chatwindow import *
from util import *


HOST = '127.0.0.1'
PORT = 9058
BUFFER_SIZE = 1024


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
                    ask_users(sock)
                elif op == LOGIN_WRONG:
                    print('Login Error')
                elif op == LOGIN_REPEAT:
                    print('Login Repeat')
                elif op == LOGIN_INFO:
                    ui_chat.APPEND.emit(data[1] + ' has logged in!')
                    ask_users(sock)
                elif op == LOGOUT_INFO:
                    ui_chat.APPEND.emit(data[1] + ' has logged out!')
                    ask_users(sock)
                elif op == SEND_ALL:
                    ui_chat.APPEND.emit(data[1] + ' says:\n' + data[2])
                elif op == SEND_PER:
                    ui_chat.new_conv.emit(data[1], data[2])
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

    ui_login = LoginPage(sock)
    ui_chat = ChatPage(sock)

    listen = threading.Thread(target=listener, args=(), daemon=True)
    listen.start()

    ui_login.show()  # 这个用了才能展示界面
    app.exec_()

    sock.close()
    sys.exit()
