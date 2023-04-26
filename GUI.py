import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import threading
import time
import Chunk_Announcer as canno
import Chunk_Downloader as cdown

class MainMenu:

    current_menu=0

    def __init__(self,root):

        self.menu_anno=Announcer(root)
        self.menu_disco=Discovery(root)
        self.menu_download=Downloader(root)
        self.menu_upload=Upload(root)






        self.title_area=tk.Label(root,font=('Arial',12,'bold'))
        self.title_area.grid(row=0,columns=2)
        self.title_area.config(bg="#485a78",fg='white')

        self.button_area=tk.Frame(root)
        self.button_area.grid(row=1, column=0)
        self.button_area.config(bg="#37455c")

        self.but_upload=tk.Button(self.button_area,text='Uploader',command=self.on_upload_click,width=10)
        self.but_upload.grid(row=0,columns=1,pady=10,padx=10, sticky='W')
        #self.but_upload.pack(side="top")

        self.but_downloader=tk.Button(self.button_area,text='Downloader',width=10,command=self.on_downloader_click)
        self.but_downloader.grid(row=1,columns=1,pady=10)
        #self.but_downloader.pack(side="top")

        self.but_discovery=tk.Button(self.button_area,text='Discovery',width=10,command=self.on_discovery_click)
        self.but_discovery.grid(row=2,columns=1,pady=10)
        #self.but_discovery.pack(side="top")

        self.but_announcer=tk.Button(self.button_area,text='Announcer ',command=self.on_announcer_click,width=10)
        self.but_announcer.grid(row=3,columns=1,pady=10)
        #self.but_announcer.pack(side="top")


        self.menu_no=0
        self.title_area.config(text='Announcer')
        self.menu_anno.start()


        return


    #0:Announcer 1:Discovery 2:Downloader 3:Uploader
    def on_announcer_click(self):
        if self.menu_no==0 :
            return
        else:
            if self.menu_no==1:
                self.menu_disco.remove()
            if self.menu_no == 2:
                self.menu_download.remove()
            if self.menu_no == 3:
                self.menu_upload.remove()
            self.menu_no=0
            self.title_area.config(text='Announcer')
            self.menu_anno.start()

    def on_upload_click(self):
        if self.menu_no == 3:
            return
        else:
            if self.menu_no == 1:
                self.menu_disco.remove()
            if self.menu_no == 0:
                self.menu_anno.remove()
            if self.menu_no == 2:
                self.menu_download.remove()
            self.menu_no = 3
            self.title_area.config(text='Uploader')
            self.menu_upload.start()

    def on_discovery_click(self):
        if self.menu_no == 1:
            return
        else:
            if self.menu_no==0:
                self.menu_anno.remove()
            elif self.menu_no == 2:
                self.menu_download.remove()
            elif self.menu_upload == 3:
                self.menu_upload.remove()

            self.menu_no=1;
            self.title_area.config(text='Discovery')
            self.menu_disco.start()

    def on_downloader_click(self):
        if self.menu_no==2 :
            return
        else:
            if self.menu_no==1:
                self.menu_disco.remove()
            elif self.menu_no == 0:
                self.menu_anno.remove()
            elif self.menu_upload == 3:
                self.menu_upload.remove()

            self.menu_no=2;
            self.title_area.config(text='Downloader')
            self.menu_download.start()

    def downloaderAnim(self):
        i=0
        while i<=100:
            self.clearTree()
            contacts = []
            contacts.append((f'25.183.80.20', f'forest_1', f'Downloaded', f'2Mb'))
            contacts.append((f'25.183.80.20', f'forest_2', f'Downloading('+str(i)+'%)', '400Kb'))
            contacts.append((f'25.183.80.20', f'forest_3', f'Waiting', '0'))
            contacts.append((f'25.183.80.20', f'forest_4', f'Waiting', '0'))
            for contact in contacts:
                self.menu_download.tree.insert('', tk.END, values=contact)
            i=i+5
            time.sleep(0.1)


    def clearTree(self):
        self.menu_download.tree.delete(*self.menu_download.tree.get_children())


class Announcer:

    def __init__(self,root):
        self.root=root;

    def start(self):
        self.initalButtons(self.root)
        self.initialTable(list_anno)

    def initalButtons(self,root):
        self.button_area=tk.Frame(root)
        self.button_area.grid(row=2, column=1)
        self.button_area.config(bg="#485a78")

        self.bt_remove = tk.Button(self.button_area,text='Remove File',width=15,command=self.onRemoveButton)
        self.bt_remove.grid(row=0,column=1,padx=50,pady=10)
        self.bt_remove["state"] = "disabled"

        self.bt_add=tk.Button(self.button_area,text='Add File',width=15,command=self.onAddButton)
        self.bt_add.grid(row=0,column=0,padx=50,pady=10)

    def onAddButton(self):
        self.root.filename = filedialog.askopenfilename(initialdir="/", title="Select '.png' file",filetypes=(("png files", "*.png"), ("all files", "*.*")))
        #print(self.root.filename)
        if self.root.filename:
            canno.addNewPngToAnnounce(self.root.filename)
        return
    def onRemoveButton(self):
        name = str(self.selectedVall[0])[:str(self.selectedVall[0]).rindex('_')]
        print("Removing Chunks: "+name)
        canno.removeList(name)

    def initialTable(self,contacts):
        #self.remove()
        columns = ('#1', '#2')#, '#3'
        self.tree =ttk.Treeview(self.root, columns=columns, show='headings')
        # define headings

        self.tree.heading('#1', text='File Name')
        #self.tree.heading('#2', text='Number Of Chunks')
        self.tree.heading('#2', text='Bytes of Chunk')
        #self.tree.config(width=50)

        # generate sample data
        #contacts = []
        #contacts.append((f'forest.png',f'5',f'20145'))
        #contacts.append((f'bird.png',f'3',f'25555'))
        #contacts.append((f'zebra.png',f'8',f'525252'))
        #contacts.append((f'Kereviz.png',f'18',f'17200'))

        #for n in range(1, 100):
        #    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # adding data to the treeview
        if not contacts:
            self.bt_remove['state']='disable'

        contacts.reverse()
        for contact in contacts:
            self.tree.insert('', tk.END, values=contact)


        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        self.tree.grid(row=1, column=1, sticky='nsew')

        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=2, sticky='ns')


    def remove(self):
        self.tree.destroy()
        self.bt_add.destroy()
        self.bt_remove.destroy()
        self.scrollbar.destroy()
        self.button_area.destroy()

    def item_selected(self,event):
        for selected_item in self.tree.selection():
            self.bt_remove["state"] = "active"
            # dictionary
            item = self.tree.item(selected_item)
            # list
            self.selectedVall = item['values']
            #print('Information '+str(self.selectedVall))
            #


class Downloader:

    def __init__(self,root):
        self.root=root;

    def start(self):
        self.initialTable(list_down)


    def initialTable(self,contacts):
        columns = ('#1', '#2', '#3','#4')
        self.tree =ttk.Treeview(self.root, columns=columns, show='headings')
        # define headings
        self.tree.heading('#1', text='Peer IP')
        self.tree.heading('#2', text='Chunk Name')
        self.tree.heading('#3', text='Download Percentage')
        self.tree.heading('#4', text='Byte Size')
        #self.tree.config(width=50)

        # generate sample data
        #contacts = []
        #contacts.append((f'25.183.80.20',f'forest_1',f'Downloaded',f'2Mb'))
        #contacts.append((f'25.183.80.20',f'forest_2',f'Downloading(20%)','400Kb'))
        #contacts.append((f'25.183.80.20',f'forest_3',f'Waiting','0'))
        #contacts.append((f'25.183.80.20',f'forest_4',f'Waiting','0'))
        #for n in range(1, 100):
        #    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # adding data to the treeview
        contacts.reverse()
        for contact in contacts:
            self.tree.insert('', tk.END, values=contact)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        self.tree.grid(row=1, column=1, sticky='nsew')

        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=2, sticky='ns')

    def remove(self):
        self.tree.destroy()
        self.scrollbar.destroy()
        #self.button_area.destroy()

    def item_selected(self,event):
        for selected_item in self.tree.selection():
            # dictionary
            item = self.tree.item(selected_item)
            # list
            record = item['values']
            #
            #print('Information'+str(record))


class Upload:

    def __init__(self,root):
        self.root=root;

    def start(self):
        self.initialTable(list_up)


    def initialTable(self,contacts):
        columns = ('#1', '#2', '#3','#4')
        self.tree =ttk.Treeview(self.root, columns=columns, show='headings')
        # define headings
        self.tree.heading('#1', text='Peer IP')
        self.tree.heading('#2', text='Chunk Name')
        self.tree.heading('#3', text='Status')
        self.tree.heading('#4', text='Uploaded Bytes')
        #self.tree.config(width=50)

        # generate sample data
        #contacts = []
        #contacts.append((f'forest_1',f'3Mb',f'Uploading(40%)','25.185.75.63'))
        #for n in range(1, 100):
        #    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # adding data to the treeview
        for contact in contacts:
            self.tree.insert('', tk.END, values=contact)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        self.tree.grid(row=1, column=1, sticky='nsew')

        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=2, sticky='ns')

    def remove(self):
        self.tree.destroy()
        self.scrollbar.destroy()
        #self.button_area.destroy()

    def item_selected(self,event):
        for selected_item in self.tree.selection():
            # dictionary
            item = self.tree.item(selected_item)
            # list
            record = item['values']
            #
            #print('Information'+str(record))

class Discovery:

    def __init__(self,root):
        self.root=root;
        self.selected_file=''

    def start(self):
        global list_dis
        self.initialTable(list_dis)
        self.initalButtons(self.root)

    def initalButtons(self,root):
        self.button_area=tk.Frame(root)
        self.button_area.config(bg='#485a78')
        self.button_area.grid(row=2, column=1)

        self.bt_download = tk.Button(self.button_area,text='Download Selected File',command=self.on_download_click)
        self.bt_download.pack(side="left",padx=50,pady=10)
        self.bt_download["state"] = "disabled"
        self.info_msg=tk.Label(self.button_area,bg='#485a78')
        self.info_msg.pack(side='right',padx=20,pady=10)

        #self.btt.place(x=0,y=230)
        #self.btt.pack(side=tk.BOTTOM)

        #self.bt_add=tk.Button(self.button_area,text='Add File',width=15)
        #self.bt_add.pack(side="left",padx=50,pady=10)


    def initialTable(self,contacts):
        columns = ('#1', '#2', '#3','#4')
        self.tree =ttk.Treeview(self.root, columns=columns, show='headings')
        # define headings
        self.tree.heading('#1', text='File Name')
        self.tree.heading('#2', text='Number Of Peers')
        self.tree.heading('#3', text='Peer IPs')
        self.tree.heading('#4', text='Number Of Chunks')
        #self.tree.config(width=50)

        # generate sample data
        #contacts = []
        #contacts.append((f'forest',f'5',f'25.180.90.75 - 25.178.93.80 -25.68.80.40',f'4'))
        #contacts.append((f'kereviz',f'3',f'25.180.90.75',f'5'))
        #contacts.append((f'ananas',f'8',f'25.180.90.75',f'5'))
        #contacts.append((f'bird',f'18',f'25.180.90.75',f'5'))
        #for n in range(1, 100):
        #    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # adding data to the treeview
        contacts.reverse()
        for contact in contacts:
            self.tree.insert('', tk.END, values=contact)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        self.tree.grid(row=1, column=1, sticky='nsew')

        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=2, sticky='ns')



    def remove(self):
        self.tree.destroy()
        self.info_msg.destroy()
        #self.bt_add.destroy()
        self.bt_download.destroy()
        self.scrollbar.destroy()
        self.button_area.destroy()

    def item_selected(self,event):
        for selected_item in self.tree.selection():
            if self.bt_download["state"] == "disabled":
                self.bt_download["state"] = "normal"
            # dictionary
            item = self.tree.item(selected_item)
            # list
            record = item['values']
            #
            #print('Information'+str(record))
            self.selected_file=record[0]

    def on_download_click(self):
        if self.selected_file!='':
            cdown.startDownloadThread(self.selected_file)
            self.info_msg.config(text='Trying to download "'+self.selected_file+'", you can follow from Downloader Menu.', fg='lightgray')

        return

menu=any
def startUI():
    global menu
    root = tk.Tk()
    # root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='images/Başlıksız-1.png'))
    root.title('CMP2204 - Python')
    # root.geometry("700x400")
    menu = MainMenu(root)
    # 485a78 Blue
    # 285225 Green
    root.config(bg="#485a78")
    root.resizable(False, False)
    root.mainloop()

def startThread():
    t1=threading.Thread(target=startUI)
    t1.start()

list_anno=[]
def refreshAnnouncer(list):
    global menu
    global list_anno
    list_anno=list
    if menu.menu_no == 0 :
        menu.menu_anno.initialTable(list_anno)


list_dis=[]
# contacts.append((f'bird',f'18',f'25.180.90.75',f'5'))
def refreshDiscovery(list):

    global menu
    global list_dis

    file_name=''
    ip_peer=[]
    number_chunk=0
    for val in list:
        name=val[:val.rindex('_')]
        if name != file_name and file_name != '':
            ips=''
            print(name+" !="+file_name+" & "+file_name+" != ''")
            for i in ip_peer:
                if i not in ips:
                    ips+=" - "+i
            for item in list_dis:
                if file_name in item:
                    list_dis.remove(item)
            list_dis.append((f'{file_name}',f'{str(len(ip_peer))}',f'{ips[3:]}',f'{number_chunk}'))
            ip_peer = []
            number_chunk = 1
        else:
            number_chunk+=1
            for ips in list[val]:
                if ips not in ip_peer:
                    ip_peer.append(ips)
        file_name=name
    if file_name != '':
        for i in ip_peer:
            if i not in ips:
                ips+=" - "+i
        for item in list_dis:
            if file_name in item:
                list_dis.remove(item)
        list_dis.append((f'{file_name}', f'{str(len(ip_peer))}', f'{ips[0:]}', f'{number_chunk}'))
    if menu.menu_no == 1 :
        menu.menu_disco.initialTable(list_dis)


list_down=[]
#contacts.append((f'25.183.80.20',f'forest_1',f'Downloaded',f'2Mb'))
def refreshDownloader(dict):
    global menu
    global list_down
    for key in dict:
        for i in range(5):
            message="Waiting"
            if dict[key][0]==i:
                message="Downloading Now"
            elif dict[key][0]>i:
                message="Downloaded"
            k1=(dict[key][2][i])
            k2=key+"_"+str(i+1)
            k3=message
            k4=str(dict[key][1][i])
            for item in list_down:
                if k2 in item:
                    list_down.remove(item)
                    break
            list_down.append((f'{k1}',f'{k2}',f'{k3}',f'{k4}'))

    if menu.menu_no == 2:
        menu.menu_download.initialTable(list_down)

list_up=[]
def uploadRefresh(adress:str,chunkName:str,sentByte,status:bool,byte_total): #IP / CHUNK / Status / Uploaded

    if status :
        k1=adress
        k2=chunkName
        k3="Uploaded"
        k4=str(sentByte)
        list_up.append((f'{k1}',f'{k2}',f'{k3}',f'{k4}'))
        if menu.menu_no==3:
            menu.menu_upload.initialTable(list_up)
    else:
        list=list_up.copy()
        k1 = adress
        k2 = chunkName
        perc=100*(sentByte/byte_total)
        if perc>100:
            perc=100
        k3 = "Uploading / "+str(perc)
        k4 = str(sentByte)
        list.append((f'{k1}', f'{k2}', f'{k3}', f'{k4}'))
        if menu.menu_no == 3:
            menu.menu_upload.initialTable(list)


    return