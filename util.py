from Constant import *
import sys


def send(sock, msg):
    msg = msg.encode('utf-8')
    sock.sendall(msg)  # 通过这个套接字将信息全部发送出去
    print('send:', msg)


def register():
    user, pwd, re_pwd = input('username: '), input('password: '), input('repeat password: ')
    if pwd == re_pwd:
        send('\r\n'.join([str(REGISTER), user, pwd]))  # 发送注册信息
    else:
        print('Password is inconsistent!')


def send_msg(sock, receiver, data):
    print(receiver)
    send_data = [str(SENDMSG), '\t'.join(receiver), data]
    send(sock, '\r\n'.join(send_data))


def send_all(sock, data):
    send(sock, str(SENDALL) + '\r\n' + data)


def ask_users(sock):
    send(sock, str(ASKUSERS))


def log_out(sock):
    send(sock, str(LOGOUT))


def close(sock):
    sock.close()
    sys.exit()