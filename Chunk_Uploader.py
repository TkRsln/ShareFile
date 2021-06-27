from socket import *
import json
import Chunk_Announcer  as ca
import time
import threading

serverPort = 8000
tag = "[Uploder] "


class ChunkNotExistError(Exception):
    def __init__(self, message="Chunk is not found"):
        self.message = message
        super().__init__(self.message)


def uploadchunks(sck):
    try:
        print(tag+"Upload started")
        jsn = sck.recv(1024)
        chunkname = json.loads(jsn)["requested_content"]
        if chunkname not in ca.mylist:
            raise ChunkNotExistError()
        with open(chunkname, 'rb') as file:
            chunk = file.read()
        chunksize = len(chunk)
        sentByte = 0

        while sentByte < chunksize:
            socket.sendall(chunk[sentByte: min(sentByte+1024), chunksize])
            sentByte += 1024
        time.sleep(1)
        sck.close()
        print(tag+"Successfully sent " + chunkname)

    except ChunkNotExistError:
        print(tag+"Requested chunk is not found!")
        sck.close()


def startserver():
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.bind(('', serverPort))
    serversocket.listen()
    print(tag+"Server started")
    while True:
        connection, addr = serversocket.accept()

        print(tag+"Connection accepted")

        t1 = threading.Thread(target = uploadchunks, args = (connection,))
        t1.start()


def starthread():
    t1 = threading.Thread(target = startserver)
    return t1

