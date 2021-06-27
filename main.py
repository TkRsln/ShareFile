import time
import threading
import Content_Discovery as cdisc
import Chunk_Downloader as cdown
import Chunk_Uploader as cupload
import Chunk_Announcer as can
#lock = threading.Lock()

can.starthread().start()
cdisc.starthread().start()
#cupload.starthread().start()
































"""
x = 5


def chunkannouncer():
    while True:
        with lock:
            x = 2
            time.sleep(1)
        print(x)


def chunkdownloader():
    while True:
        with lock:
            x = 3
            time.sleep(1)
        print(x)


t1 = threading.Thread(target=chunkannouncer)
t2 = threading.Thread(target=chunkdownloader)


#t1.start()
#t2.start()

cd.thisdict["forest_1"] = ["192","168"]
cd.thisdict["chunk_2"] = ["192","168"]
cd.thisdict["chunk_3"] = ["192","168"]

print(ch.numberofchunks("chunk"))


"""