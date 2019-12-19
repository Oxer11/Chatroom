import socket
import os
import select
import sqlite3
import time
from Constant import *
from util import receive_file

HOST = '127.0.0.1'
PORT = 9078
BUFFER_SIZE = 4096

group = {}


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
    users = list(user2conn.keys())
    s.sendall('\r\n'.join([str(ASKUSERS_RET), str(len(users)), '\n'.join(users)]).encode('utf-8'))


def send_file_all(s, data):
    file_name, file_size, cur_data = receive_file(s, data)
    flie_dic = "./server/files/__{0}__".format(conn2user[s])
    if not os.path.exists(flie_dic):
        os.makedirs(flie_dic)
    path = os.path.join(flie_dic, file_name)
    with open(path, "wb") as f:
        f.write(cur_data)
    broadcast(s, str(SENDFILE_ALL) + '\r\n' + conn2user[s] + '\r\n' + file_name + '\r\n' + file_size)


def send_file(sender, data):
    sep = '\r\n'.encode('utf-8')
    receiver, data = data[:data.find(sep)], data[data.find(sep)+2:]
    file_name, file_size, cur_data = receive_file(sender, data)
    flie_dic = "./server/files/__{0}__".format(conn2user[sender])
    if not os.path.exists(flie_dic):
        os.makedirs(flie_dic)
    path = os.path.join(flie_dic, file_name)
    with open(path, "wb") as f:
        f.write(cur_data)
    receiver = receiver.decode('utf-8').split('\t')
    rec = []
    for r in receiver:  # 向这些人发送信息 先看看数据库里有没有
        cursor.execute("select * from user where username = '{0}'".format(r))
        user = cursor.fetchone()
        if user is None:
            sender.sendall(str(SENDFILE_ERROR).encode('utf-8'))  # 在发送者的套接字上发送 发送信息错误
        else:
            try:
                s = user2conn[user[0]]
                rec.append(s)
            except KeyError:
                sender.sendall(str(SENDFILE_ERROR).encode('utf-8'))
    for s in rec:  # rec是所有合法的收信者
        if s != sock and s != sender:
            s.sendall((str(SENDFILE_PER) + '\r\n' + conn2user[sender] + '\r\n' + file_name + '\r\n' + file_size).encode('utf-8'))


def send_file_group(sender, data):
    sep = '\r\n'.encode('utf-8')
    groupid, data = data[:data.find(sep)], data[data.find(sep)+2:]
    receiver, data = data[:data.find(sep)], data[data.find(sep)+2:]
    file_name, file_size, cur_data = receive_file(sender, data)
    flie_dic = "./server/files/__{0}__".format(conn2user[sender])
    if not os.path.exists(flie_dic):
        os.makedirs(flie_dic)
    path = os.path.join(flie_dic, file_name)
    with open(path, "wb") as f:
        f.write(cur_data)
    receiver = receiver.decode('utf-8').split('\t')
    groupid = groupid.decode('utf-8')
    rec = []
    for r in receiver:  # 向这些人发送信息 先看看数据库里有没有
        cursor.execute("select * from user where username = '{0}'".format(r))
        user = cursor.fetchone()
        if user is None:
            sender.sendall(str(SENDFILE_ERROR).encode('utf-8'))  # 在发送者的套接字上发送 发送信息错误
        else:
            try:
                s = user2conn[user[0]]
                rec.append(s)
            except KeyError:
                sender.sendall(str(SENDFILE_ERROR).encode('utf-8'))
    for s in rec:  # rec是所有合法的收信者
        if s != sock and s != sender:
            s.sendall('\r\n'.join([str(SENDFILE_GROUP), conn2user[sender],
                                   groupid, file_name, file_size]).encode('utf-8'))


def down_file(s, data):
    user, filename = data[0], data[1]
    file_path = './server/files/__{0}__/{1}'.format(user, filename)
    file_size = os.stat(file_path).st_size
    with open(file_path, "rb") as f:
        content = f.read()
    send_data = '\r\n'.join([str(DOWNFILE_SUCCESS), filename, str(file_size)]) + chr(0) + chr(0)
    s.sendall(send_data.encode('utf-8') + content)


def close(s, data):
    user = conn2user[s]
    if user is not None:
        for grp in group.copy():
            if user in group[grp]:
                group_log_out(s, [grp, user])
        broadcast(s, str(LOGOUT_INFO) + '\r\n' + user)
        del user2conn[user]
    del conn2user[s]
    connections.remove(s)
    s.close()


def new_group(s, data):
    user = conn2user[s]
    if data[0] not in group:
        group[data[0]] = [user]
    else:
        if user in group[data[0]]:
            s.sendall((str(GROUP_FAIL)).encode('utf-8'))
            return
        for u in group[data[0]]:
            user2conn[u].sendall('\r\n'.join([str(GROUP_LOGIN), user, data[0]]).encode('utf-8'))
        group[data[0]].append(user)
    s.sendall((str(GROUP_SUCCESS) + '\r\n' + data[0]).encode('utf-8'))


def ask_group_users(s, data):
    users = group[data[0]]
    s.sendall('\r\n'.join([str(ASKGROUPUSERS_RET), data[0], '\n'.join(users)]).encode('utf-8'))


def send_group_msg(sender, data):
    receiver = data[1].split('\t')
    rec = []
    for r in receiver:  # 向这些人发送信息 先看看数据库里有没有
        cursor.execute("select * from user where username = '{0}'".format(r))
        user = cursor.fetchone()
        if user is None:
            sender.sendall(str(SENDGROUPMSG_ERROR).encode('utf-8'))  # 在发送者的套接字上发送 发送信息错误
        else:
            try:
                s = user2conn[user[0]]
                rec.append(s)
            except KeyError:
                sender.sendall(str(SENDGROUPMSG_ERROR).encode('utf-8'))
    for s in rec:  # rec是所有合法的收信者
        if s != sock and s != sender:
            s.sendall('\r\n'.join([str(SENDGROUPMSG_SUCCESS), conn2user[sender], data[0], data[2]]).encode('utf-8'))


def group_log_out(sender, data):
    group[data[0]].remove(data[1])
    if len(group[data[0]]) == 0:
        del group[data[0]]
    else:
        for u in group[data[0]]:
            user2conn[u].sendall('\r\n'.join([str(GROUP_LOGOUT), data[1], data[0]]).encode('utf-8'))
            time.sleep(1)


def up_photo(sender, data):
    file_name, file_size, cur_data = receive_file(sender, data)
    path = "./server/photo/{0}.png".format(conn2user[sender])
    with open(path, "wb") as f:
        f.write(cur_data)
    for s in connections:
        if s != sock:
            s.sendall(('\r\n'.join([str(UP_PHOTO), conn2user[sender], file_name, str(file_size)])
                       + chr(0) + chr(0)).encode('utf-8') + cur_data)


handle_dic = {LOGIN: log_in,
              REGISTER: register,
              SENDMSG: send_msg,
              SENDALL: send_all,
              LOGOUT: log_out,
              ASKUSERS: ask_users,
              SENDFILEALL: send_file_all,
              SENDFILE: send_file,
              DOWNFILE: down_file,
              CLOSE: close,
              NEWGROUP: new_group,
              ASKGROUPUSERS: ask_group_users,
              SENDGROUPMSG: send_group_msg,
              GROUPLOGOUT: group_log_out,
              SENDFILEGROUP: send_file_group,
              UPPHOTO: up_photo}


def handle(s, data):  # 处理收到的信息
    sec = data[:10].decode('utf-8').split('\r\n')
    try:
        if int(sec[0]) in [SENDFILEALL, SENDFILE]:
            handle_dic[int(sec[0])](s, data[3:])
        elif int(sec[0]) in [SENDFILEGROUP, UPPHOTO]:
            handle_dic[int(sec[0])](s, data[4:])
        else:
            sec = data.decode('utf-8').split('\r\n')
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
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
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
                conn, addr = s.accept()  # sock接受一个连接 记录其套接字conn
                connections.add(conn)
                conn2user[conn] = None
            else:
                try:
                    data = s.recv(BUFFER_SIZE)
                    assert len(data) > 0, 'receive empty message'
                    handle(s, data)
                except Exception as e:
                    close(s, None)
