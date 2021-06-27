from socket import *
import Content_Discovery as cd


class ServerNotFoundError(Exception):

    def __init__(self, ipno, message="Server is not responding"):
        self.ipno = ipno
        self.message = message
        super().__init__(self.message)


class NextIpNotFoundError(Exception):

    def __init__(self, chunkname, message="Next ip is not found for: "):
        self.chunkname = chunkname
        self.message = message
        super().__init__(self.message + chunkname)


class ChunkNotInDictionaryError(Exception):

    def __init__(self, chunkname, message="Chunk is not found in dictionary"):
        self.chunkname = chunkname
        self.message = message
        super().__init__(self.message + chunkname)


def numberofchunks(name: str):
    for i in range(1,20):
       if name + "_" + str(i) in cd.thisdict:
           continue
       else:
           return i-1


def getipaddress(chunkname, ipno):
    if chunkname not in cd.thisdict:
        raise ChunkNotInDictionaryError(chunkname)
    if len(cd.thisdict[chunkname]) <= ipno:
        raise NextIpNotFoundError(chunkname)
    return cd.thisdict[chunkname][ipno]


def requestedjson(chunkname: str):
    return '{“requested_content”: “'+ chunkname +'”}'


def writetofile(data, chunkname):
    with open(chunkname, "wb") as file:
        file.write(data)
    file.close()


def downloadchunks(name: str):
    try:
        size = numberofchunks(name)
        if size == 0:
            raise ChunkNotInDictionaryError(name)

        for i in range(1, size+1):
            clientsocket = socket(AF_INET, SOCK_STREAM)
            address = None
            data = []
            chunkFullName = name+"_"+str(i)
            for j in range(len(cd.thisdict[chunkFullName])+1):
                address = getipaddress(chunkFullName, j)
                try:
                    clientsocket.connect((address,5001))
                except:
                    print("Failed to connect '" + address +"'. Trying to connect next ip")
                    continue
                print(address)
            clientsocket.send(requestedjson(chunkFullName).encode())
            try:
                while True:
                    data = data+clientsocket.recv(1024)
            except ConnectionResetError:
                print("Received data bytes " + str(len(data)) + " " + chunkFullName)
                writetofile(data, chunkFullName)
    except NextIpNotFoundError:
        print("Can Not Found Next-Ip For This Chunk")
    except ChunkNotInDictionaryError:
        print("Chunk not found in dictionary")


