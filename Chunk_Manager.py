import os
import math
import Chunk_Announcer as cannouncer

directory = "./Chunks/"
directoryout = "./Out/"
tag = "[Chunk_Manager] "


def createChunks(content_fullname: str):
    content_name: str = content_fullname
    if content_fullname.endswith('.png'):
        if "\\" in content_fullname:
            content_name = content_fullname[content_fullname.rindex("\\")+1:-4]
        else:
            content_name = content_fullname[:-4]
    else:
        if "\\" in content_fullname:
            content_name: str = content_fullname[content_fullname.rindex("\\")+1:]
        content_fullname += ".png"
    c = os.path.getsize(content_fullname)
    chunk_size = math.ceil(math.ceil(c) / 5)
    index = 1
    with open(content_fullname, 'rb') as infile:
        chunk = infile.read(int(chunk_size))
        while chunk:
             chunkname = content_name+'_'+str(index)
            # print("chunk name is: " + chunkname + "\n")
             with open(directory+chunkname, 'wb+') as chunk_file:
                 chunk_file.write(chunk)
             index += 1
             chunk = infile.read(int(chunk_size))
             cannouncer.mylist.append(chunkname)
    chunk_file.close()
    print(tag+"("+content_name+") Chunks are created!")


def createFile(content_name):
    #content_name = 'py'  # again, this'll be the name of the content that used wanted to download from the network.
    chunknames = [directory+content_name + '_1', directory+content_name + '_2', directory+content_name + '_3', directory+content_name + '_4',
                  directory +content_name + '_5']

    # with open(content_name+'.png', 'w') as outfile:
    with open(directoryout+content_name+'.png', 'wb') as outfile:  # in your code change 'ece.png' to content_name+'.png'
        for chunk in chunknames:
            with open(chunk, 'rb') as infile:
                outfile.write(infile.read())
            infile.close()
    outfile.close()


try:
    os.makedirs(directory, exist_ok=True)
    os.makedirs(directoryout, exist_ok=True)
    print(tag+"Directory '%s' created successfully" % directory)
except OSError as error:
    print(tag+"Directory '%s' can not be created" % directory)


content_fullname: str = input("Enter file name:")
createChunks(content_fullname)
print(cannouncer.mylist)
createFile(content_fullname)








































