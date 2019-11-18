import socket
import os
import select
import sqlite3

from Constant import *

HOST = '127.0.0.1'
PORT = 9058
BUFFER_SIZE = 4096


def broadcast(sender, msg):
    for s in connections:
        if s != sock and s != sender:
            s.sendall(msg.encode('utf-8'))
            print('Send to', s, msg.encode('utf-8'))


def log_in(s, data):
    cursor.execute("select * from user where username = '{0}' and password = '{1}'".format(data[0], data[1]))
    user = cursor.fetchone()
    if user is None:
        s.sendall('Username or password is wrong!'.encode('utf-8'))
    elif user2conn.get(user[0]) is not None:
        s.sendall('%s has already logged in!' % user[0])
    elif conn2user.get(s) is not None:
        s.sendall('You have already logged in!')
    else:
        user2conn.update({user[0]: s})
        conn2user.update({s: user[0]})
        broadcast(s, '%s log in!' % user[0])
        s.sendall('Log in successfully!'.encode('utf-8'))


def register(s, data):
    cursor.execute("select * from user where username = '{0}'".format(data[0]))
    user = cursor.fetchone()
    if user is None:
        cursor.execute("insert into user (username, password) \
                        values ('{0}', '{1}')".format(data[0], data[1]))
        db.commit()
        s.sendall('User registers successfully!'.encode('utf-8'))
    else:
        s.sendall('User already exists!'.encode('utf-8'))


def send_all(sender, data):
    broadcast(sender, data[0])
    sender.sendall('Send successfully!'.encode('utf-8'))


def send_msg(sender, data):
    receiver = data[0].split('\t')
    rec = []
    for r in receiver:
        cursor.execute("select * from user where username = '{0}'".format(r))
        user = cursor.fetchone()
        if user is None:
            sender.sendall(('User %s does not exists!' % r).encode('utf-8'))
        else:
            try:
                s = user2conn[user[0]]
                rec.append(s)
            except KeyError:
                sender.sendall(('User %s is not online!' % r).encode('utf-8'))
    for s in rec:
        if s != sock:
            s.sendall(data[1].encode('utf-8'))
    sender.sendall('Send successfully!'.encode('utf-8'))


def log_out(s, data):
    user = conn2user[s]
    if user is None:
        s.sendall('You have not logged in!'.encode('utf-8'))
    else:
        broadcast(s, '%s log out!' % user)
        conn2user[s] = None
        s.sendall('Log out successfully!'.encode('utf-8'))


def ask_users(s, data):
    if len(user2conn.keys()) == 0:
        s.sendall('No user!'.encode('utf-8'))
    else:
        s.sendall('\n'.join(user2conn.keys()).encode('utf-8'))


def close(s, data):
    user = conn2user[s]
    if user is not None:
        del user2conn[user]
    del conn2user[s]
    connections.remove(s)
    s.close()


handle_dic = {LOGIN: log_in,
              REGISTER: register,
              SENDMSG: send_msg,
              SENDALL: send_all,
              LOGOUT: log_out,
              ASKUSERS: ask_users,
              CLOSE: close}


def handle(s, data):
    sec = data.split('\r\n')
    print(sec)
    try:
        print(int(sec[0]))
        handle_dic[int(sec[0])](s, sec[1:])
    except Exception as e:
        print(e)


if __name__ == '__main__':

    # Initialize database
    db = sqlite3.connect('./user.db')
    cursor = db.cursor()
    # cursor.execute('drop table if exists user')  # Delete previous registration
    # cursor.execute('create table user(username text primary key not null, password text)')  # Create a new database
    db.commit()

    # Initialize connection
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
                try:
                    data = s.recv(BUFFER_SIZE).decode('utf-8')
                    assert len(data) > 0, 'receive empty message'
                    handle(s, data)
                except Exception as e:
                    print('close ', s.getpeername())
                    connections.remove(s)
                    s.close()

