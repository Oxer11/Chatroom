from Constant import *
import sys
import os

max_file_size = 1024*1024*50
BUFFER_SIZE = 4096


def gen_style(dic, new_dic={}):
    cur_dic = dic.copy()
    cur_dic.update(new_dic)
    str = ""
    for item in cur_dic.items():
        str += item[0] + ":" + item[1] + ";"
    return str


def send(sock, msg, add=b''):
    msg = msg.encode('utf-8') + add
    sock.sendall(msg)  # 通过这个套接字将信息全部发送出去
    print('send:', msg)


def receive_file(s, data):
    sep = bytes(chr(0) + chr(0), encoding='utf-8')
    header, cur_data = data[:data.find(sep)], data[data.find(sep) + 2:]
    header = header.decode('utf-8')
    file_name, file_size = header.split('\r\n')[0], header.split('\r\n')[1]
    res_byte = int(file_size) - len(cur_data)
    while res_byte > 0:
        if res_byte > BUFFER_SIZE:
            cur_data += s.recv(BUFFER_SIZE)
        else:
            cur_data += s.recv(res_byte)
        res_byte = int(file_size) - len(cur_data)
    return file_name, file_size, cur_data


def send_file(sock, pre, file_path):
    file_name = os.path.basename(file_path)
    file_size = os.stat(file_path).st_size
    if file_size > max_file_size: return
    with open(file_path, "rb") as f:
        content = f.read()
    send_data = '\r\n'.join([pre, file_name, str(file_size)]) + chr(0) + chr(0)
    send(sock, send_data, content)


def send_msg(sock, receiver, data):
    print(receiver)
    send_data = [str(SENDMSG), '\t'.join(receiver), data]
    send(sock, '\r\n'.join(send_data))


def send_group_msg(sock, groupid, receiver, data):
    print(groupid, receiver)
    send_data = [str(SENDGROUPMSG), groupid, '\t'.join(receiver), data]
    send(sock, '\r\n'.join(send_data))


def send_all(sock, data):
    send(sock, str(SENDALL) + '\r\n' + data)


def down_file(sock, user, filename):
    send(sock, str(DOWNFILE) + '\r\n' + user + '\r\n' + filename)


def ask_users(sock):
    send(sock, str(ASKUSERS))


def ask_group_users(sock, groupid):
    send(sock, str(ASKGROUPUSERS) + '\r\n' + groupid)


def group_log_out(sock, groupid, user):
    send(sock, str(GROUPLOGOUT) + '\r\n' + groupid + '\r\n' + user)


def log_out(sock):
    send(sock, str(LOGOUT))


def close(sock):
    sock.close()
    sys.exit()
