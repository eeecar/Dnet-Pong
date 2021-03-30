import time
import socket
import threading

import traceback

BUFFERSIZE = 1024 * 1024


# lobby class 在此实现控制逻辑
class Lobby(object):
    def __init__(self, lobbyfeature=None, gametypes=None):
        if gametypes is None:
            gametypes = ["Pong"]
        if lobbyfeature is None:
            lobbyfeature = ["BASIC"]
        self.__lobbyfeature = lobbyfeature
        self.__gametypes = gametypes

    def Set_Lobbyfeature(self,lobbyfeature):
        self.__lobbyfeature = lobbyfeature

    #Gametypes
    __gametypes = []
    def Set_Gametypes(self,gametypes):
        self.__gametypes = gametypes
    def Get_Gameytpes(self):
        return self.__gametypes

    #Matchfetures
    #__matches：字典，key为match名字，content为match的feature（BASIC 和COOL）
    #__matchfeatures：
    __pong_matches = {}
    __tron_matches = {}
    __matchfeatures = []
    def Set_Matchfeatures(self,matchfeature):
        self.__matchfeatures = matchfeature

    def Creat_Match(self,gametype,matchname,matchfeature):
        if gametype not in self.__gametypes:
            return "ERR_FAILED_TO_CREATE No such gametype"
        else:
            if gametype=="Pong":
                if self.__pong_matches.__contains__(matchname) or self.__tron_matches.__contains__(matchname):
                    return "ERR_FAILED_TO_CREATE Match name is already taken"
                elif matchfeature not in self.__matchfeatures:
                    return "ERR_FAILED_TO_CREATE No such feature"
                else:
                    self.__pong_matches[matchname] = matchfeature
                    return "MATCH_CREATED"
            elif gametype == "Tron":
                if self.__tron_matches.__contains__(matchname) or self.__pong_matches.__contains__(matchname):
                    return "ERR_FAILED_TO_CREATE Match name is already taken"
                elif matchfeature not in self.__matchfeatures:
                    return "ERR_FAILED_TO_CREATE No such feature"
                else:
                    self.__tron_matches[matchname] = matchfeature
                    return "MATCH_CREATED"



    def List_Match(self, gametype):
        if gametype == "Pong":
            output = []
            for i in self.__pong_matches.keys():
                output.append(i)
        elif gametype == "Tron":
            output = []
            for i in self.__tron_matches.keys():
                output.append(i)
        else:
            return "ERROR_CMD_NOT_UNDERSTOOD"
        return output

    def List_Feature(self,matchname):









# lobby instence
lobby = Lobby(["BASIC"])


# 对接收到的信号预处理，判断errnotunderstood 错误，将合格的信号交给lobby类进行判断。
# tcp信息的收发也在此实现。
# 该函数被connection_handler调用，参数除了client的地址还有lobby类的唯一一个instence。
def control_handler(conn, address, lobby):
    print("get message from[%s:%s]..." % (address[0], address[1]))
    while True:
        client_data = conn.recv(BUFFERSIZE).decode(encoding="ascii")


# lobby tcp server 该函数被udpserver调用，开启多线程确保tcp不堵塞。
def connection_handler(hostip, addr):
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind((hostip, addr))
    ss.listen(8)
    while True:
        conn, address = ss.accept()
        t = threading.Thread(target=control_handler, args=(conn, address, lobby))
        t.start()


# broadcastserver
host = socket.gethostname()
port0 = 54000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # set UDP socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # port reuse
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # set broadcast
s.bind((host, port0))  # bind with localhost
print("Listen on the port 54000......")

while True:
    try:
        bc, addr = s.recvfrom(102400)  # address:The port the server waits for a TCP connection
        print("Receive data from:", addr)  # show the port
        s.sendto("Received", addr)

    except:
        traceback.print_exc()  # 打印异常信息
# 1234
# TCP server (control protocol and return feature information)
#
# port1 = 54001
#
# ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # set TCP socket
# ss.bind(host, port1)
# print("Listen on the port 54001......")
# ss.listen(1)
# conn, addr = ss.accept()
#
