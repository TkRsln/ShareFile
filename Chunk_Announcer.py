import json
import socket
import time
import threading

mylist = []
tag = "[Announcer] "

def json_list(list):
    return json.dumps({'chunks': list})


def startannouncer():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server.settimeout(0.2)
    server.bind(("", 36789))

    while True:
        message = json_list(mylist)
        encoded_string = message.encode()
        byte_array = bytearray(encoded_string)
        server.sendto(byte_array, ('25.255.255.255', 5001))
        print(tag+"message sent!")
        time.sleep(60)


def starthread():
    t1 = threading.Thread(target = startannouncer)
    return t1


print(json_list(mylist))


