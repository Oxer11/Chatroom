import socket
import os
import select

from Constant import *

HOST = '127.0.0.1'
PORT = 9058
BUFFER_SIZE = 4096


def send_all(sender, data):
    for s in connections:
        if s != sock and s != sender:
            s.sendall(data[0].encode('utf-8'))
            print('Send to', s, data[0].encode('utf-8'))
    sender.sendall('Send successfully!'.encode('utf-8'))


def send_msg(sender, data):
    receiver = data[0].split('\t')
    # Not Finished !
    for s in receiver:
        if s != sock and s != sender:
            s.sendall(data[1].encode('utf-8'))
    sender.sendall('Send successfully!'.encode('utf-8'))


def close(s, data):
    connections.remove(s)
    s.close()


handle_dic = {SENDMSG: send_msg, SENDALL: send_all, CLOSE: close}


def handle(s, data):
    sec = data.split('\r\n')
    print(sec)
    try:
        print(int(sec[0]))
        handle_dic[int(sec[0])](s, sec[1:])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen()
    print("start server", HOST, PORT)
    conn2user = {}
    user2conn = {}
    connections = set([sock])
    while True:
        r, w, e = select.select(list(connections), [], [])
        for s in r:
            if s == sock:
                conn, addr = s.accept()
                print("new connection", addr)
                connections.add(conn)
                conn2user[conn] = None

            else:
                print("now: ", s)
                try:
                    data = s.recv(BUFFER_SIZE).decode('utf-8')
                    print("request: ", data)
                    assert len(data) > 0, '接收空消息'
                    handle(s, data)
                except Exception as e:
                    print(e)
                    connections.remove(s)
                    s.close()
                    print('close ', s)
