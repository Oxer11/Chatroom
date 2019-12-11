# client send
LOGIN = 0  # user pwd
REGISTER = 1  # user pwd
SENDMSG = 2  # receiver msg_length msg
SENDALL = 3  # msg_length msg
LOGOUT = 4
ASKUSERS = 5
SENDFILE = 6  # receiver file_name file_size + data of file
DOWNFILE = 7  # sender file_name
SENDFILEALL = 8
CLOSE = 9

# server response
LOGIN_WRONG = 100
LOGIN_SUCCESS = 101
LOGIN_REPEAT = 102
LOGIN_INFO = 103  # username (to all)

REGISTER_ERROR = 200
REGISTER_SUCCESS = 201

LOGOUT_INFO = 300  # username (to all)

SENDMSG_ERROR = 200
SEND_ALL = 210  # sender msg_length + msg (to all)
SEND_NONE = 211  # receiver
SEND_PER = 212  # sender msg_length + msg

ASKUSERS_RET = 400  # length of user_list + user_list

SENDFILE_ERROR = 500
SENDFILE_NONE = 501
SENDFILE_SUCCESS = 502
SENDFILE_ALL = 510  # sender file_name (to all)
SENDFILE_NONE = 511
SENDFILE_PER = 512  # sender file_name

DOWNFILE_SUCCESS = 600  # sender file_name file_size +data of file
DOWNFILE_NONE = 601


WRONG_MESSAGE=900

background_path = "./images/star.jpg"
register_path = "./images/tiancao.png"
newgroup_path = register_path
tiancao_path = "./images/tiancao.png"
star_path = "./images/little_star.png"
darkstar_path = "./images/dark_star.png"
login_height = 300
login_width = 425
register_height = login_height
register_width = login_width
newgroup_height = 300
newgroup_width = 425