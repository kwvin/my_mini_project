from socket import *
import os
import sys
import multiprocessing as mp


def send_msg(s, name, addr):
    while True:
        text = input("发言:")
        #如果输入quit表示退出
        if text.strip() == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(),addr)
            sys.exit("退出聊天室")
        msg = 'C %s %s'%(name,text)
        s.sendto(msg.encode(),addr)


def recv_msg(s):
    while True:
        data,addr = s.recvfrom(2048)
        if data.decode() == 'EXIT':
            sys.exit(0)
        print(data.decode() + "\n发言:",end="")


def main(argc,argv,envp):
    HOST = '192.168.0.119'
    PORT = 8888
    ADDR = (HOST,PORT)

    # 创建套接字
    s = socket(AF_INET, SOCK_DGRAM)

    while True:
        name = input("请输入姓名:")
        msg = "L " + name
        # 发送登录请求
        s.sendto(msg.encode(), ADDR)
        # 等待服务器回复
        data, addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break
        else:
            # 不成功服务端会回复不允许登录原因
            print(data.decode())

    # 创建父子进程
    #创建一个单独的进程处理管理员喊话功能
    p = mp.Process(target = send_msg(s, name, ADDR))
    p2 =mp.Process(target = recv_msg(s))
    p2.start()
    p.start()
    p.join()
    p2.join()


if __name__ == "__main__":
    sys.exit(main(len(sys.argv),sys.argv,os.environ))