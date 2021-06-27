import socket
import json
import threading

thisdict = {}
tag = "[Discovery] "


def addictionary(chunk: str, address: str):
    if chunk in thisdict:
        ipaddr = thisdict[chunk]
    else:
        ipaddr = []
    ipaddr.append(address)
    ipaddr = list(dict.fromkeys(ipaddr))
    thisdict[chunk] = ipaddr


def getdictionary(chunk:str):
    return thisdict[chunk]


def startlisten():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.bind(("", 5001))
    print(tag + "Socket start listen")
    while True:
        data, addr = client.recvfrom(1024)
        x = data.decode('UTF-8')
        a = json.loads(x)
        print(tag+str(len(a['chunks'])))
        for i in a['chunks']:
            addictionary(i, addr[0])
        print(tag+a)


def starthread():
    print(tag + "Thread starting")
    t1 = threading.Thread(target = startlisten)
    return t1