import socket
import sys
import select
import threading

from Constant import *


HOST = '127.0.0.1'
PORT = 9058
BUFFER_SIZE = 1024


def send(msg):
    msg = msg.encode('utf-8')
    sock.sendall(msg)
    print('send:', msg)


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
    send_data = [str(SENDALL)]
    data = input('message: ')
    send_data.append(data)
    send('\r\n'.join(send_data))


def close():
    sock.close()
    sys.exit()


handle_dic = {SENDMSG: send_msg, SENDALL: send_all, CLOSE: close}


def listener():
    while True:
        # Response
        r, w, e = select.select([sock], [], [])
        for s in r:
            try:
                recv_data = s.recv(BUFFER_SIZE)
                print('Receive:', recv_data.decode('utf-8'))
            except Exception as e:
                print(e)
                return


def action():
    while True:
        # Request
        op = input('Operation Type: ')
        try:
            handle_dic[int(op)]()
        except Exception:
            print('Please input a valid type number.')
            continue


if __name__ == '__main__':
    sock = socket.socket()
    try:
        sock.connect((HOST, PORT))
        print('Connected with server')
    except Exception as e:
        print("Fail to connect (%s, %s) due to" % (HOST, PORT), e)
        exit()
    listen = threading.Thread(target=listener, args=(), daemon=True)
    listen.start()
    action()
    sock.close()
    sys.exit()
