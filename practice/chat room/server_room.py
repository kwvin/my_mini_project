from socket import *
import os
import sys
import multiprocessing as mp

#管理员喊话功能
def do_child(s, ADDR):
    while True:
        msg = input("管理员消息:")
        msg = 'C 管理员 ' + msg
        s.sendto(msg.encode(), ADDR)


#接受消息，转发消息
def do_login(s, user, name, addr):
    if (name in user)  or  name == '管理员':
        s.sendto("该用户已存在".encode(),addr)
        return
    else:
        s.sendto(b'OK', addr)

    # 通知其他人
    msg = "\n欢迎 %s 进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    # 插入用户
    user[name] = addr



def do_chat(s, user, name, msg):
    msg = "\n%s 说:%s" % (name, msg)
    for i in user:
        if i == name:
            pass
        else:
            s.sendto(msg.encode(),user[i])


def do_quit(s, user, name):
    msg = '\n' + name + "退出了聊天室"
    for i in user:
        if i == name:
            s.sendto(b'EXIT',user[i])
        else:
            s.sendto(msg.encode(),user[i])
    #从字典删除用户
    del user[name]


def do_parent(s):
    # 存储结构 {'zhangsan':('127.0.0.1',9999)}
    user = {}
    while True:
        msg,addr = s.recvfrom(1024)
        msgList = msg.decode().split(' ')

        # 区分请求类型
        if msgList[0] == 'L':
            do_login(s, user, msgList[1], addr)
        elif msgList[0] == 'C':
            do_chat(s, user, msgList[1], ' '.join(msgList[2:]))
        elif msgList[0] == 'Q':
            do_quit(s, user, msgList[1])


def main(argc,argv,envp):
    # 创建套接字
    ADDR = ("192.168.0.119", 8888)
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    #创建一个单独的进程处理管理员喊话功能
    p = mp.Process(target = do_child(s,ADDR))
    p2 =mp.Process(target = do_parent(s))
    p2.start()
    p.start()
    p.join()
    p2.join()


if __name__ == "__main__":
    sys.exit(main(len(sys.argv),sys.argv,os.environ))