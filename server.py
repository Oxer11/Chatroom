import socket
import os
import select
import sqlite3
import time
from Constant import *

HOST = '127.0.0.1'
PORT = 9058
BUFFER_SIZE = 4096


def broadcast(sender, msg):
    for s in connections:
        if s != sock and s != sender:
            s.sendall(msg.encode('utf-8'))


def log_in(s, data):
    # cursor用来执行sql语句
    cursor.execute("select * from user where username = '{0}' and password = '{1}'".format(data[0], data[1]))
    user = cursor.fetchone()
    if user is None:  # 没有对应的用户 登陆失败
        s.sendall(str(LOGIN_WRONG).encode('utf-8'))  # sendall 发送完整的tcp数据到连接的套接字后返回
    elif user2conn.get(user[0]) is not None:  # 这个用户已经登录过了
        s.sendall(str(LOGIN_REPEAT).encode('utf-8'))
    else:
        user2conn.update({user[0]: s})  # 将这个人的用户名和对应的处理套接字加入字典
        conn2user.update({s: user[0]})  # 反之亦然
        count = 0
        i = 0
        j = 0
        top = 27000000
        ''' 测试时这个太慢了
		while( i < top):
			while( j < top):
				count = (count + 1) % 1000
				j+=1
				#print(count)
			i+=1
		'''
        s.sendall(str(LOGIN_SUCCESS).encode('utf-8'))
        broadcast(s, str(LOGIN_INFO) + '\r\n' + user[0])  # 由发送者s向所有套接字发送信息 说明这个人登录了


def register(s, data):
    cursor.execute("select * from user where username = '{0}'".format(data[0]))
    user = cursor.fetchone()
    if user is None:
        cursor.execute("insert into user (username, password) \
						values ('{0}', '{1}')".format(data[0], data[1]))
        db.commit()
        s.sendall(str(REGISTER_SUCCESS).encode('utf-8'))
    else:
        s.sendall(str(REGISTER_ERROR).encode('utf-8'))


def send_all(sender, data):  # 向所有人发送信息（聊天信息
    broadcast(sender, str(SEND_ALL) + '\r\n' + conn2user[sender] + '\r\n' + data[0])


def send_msg(sender, data):
    receiver = data[0].split('\t')
    rec = []
    for r in receiver:  # 向这些人发送信息 先看看数据库里有没有
        cursor.execute("select * from user where username = '{0}'".format(r))
        user = cursor.fetchone()
        if user is None:
            sender.sendall(str(SENDMSG_ERROR).encode('utf-8'))  # 在发送者的套接字上发送 发送信息错误
        else:
            try:
                s = user2conn[user[0]]
                rec.append(s)
            except KeyError:
                sender.sendall(str(SENDMSG_ERROR).encode('utf-8'))
    for s in rec:  # rec是所有合法的收信者
        if s != sock:
            s.sendall((str(SEND_PER) + '\r\n' + conn2user[sender] + '\r\n' + data[1]).encode('utf-8'))


def log_out(s, data):
    user = conn2user[s]
    if user is None:
        s.sendall('You have not logged in!'.encode('utf-8'))
    else:
        broadcast(s, str(LOGOUT_INFO) + '\r\n' + user)
        conn2user[s] = None


def ask_users(s, data):
    user = conn2user[s]
    users = list(user2conn.keys())
    users.remove(user)
    s.sendall('\r\n'.join([str(ASKUSERS_RET), str(len(user2conn.keys())), '\n'.join(users)]).encode('utf-8'))


def close(s, data):
    print('line 86 close ', s.getpeername())
    user = conn2user[s]
    if user is not None:
        broadcast(s, str(LOGOUT_INFO) + '\r\n' + user)
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


def handle(s, data):  # 处理收到的信息
    sec = data.split('\r\n')
    print('line 107 ', sec)
    try:
        print('line 109 function', int(sec[0]), handle_dic[int(sec[0])])
        handle_dic[int(sec[0])](s, sec[1:])
    # handle_dic查找对应的函数
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
    # print('connections ',connections)
    while True:
        r, w, e = select.select(list(connections), [], [])
        for s in r:
            if s == sock:
                conn, addr = s.accept()  # sock接受一个连接 记录其套接字conn
                print("line 138 new connection", addr)
                connections.add(conn)
                # print('connections ',connections,conn)
                conn2user[conn] = None
            else:
                try:
                    print('line 144 try')
                    data = s.recv(BUFFER_SIZE).decode('utf-8')
                    assert len(data) > 0, 'receive empty message'
                    handle(s, data)
                except Exception as e:
                    close(s, None)
