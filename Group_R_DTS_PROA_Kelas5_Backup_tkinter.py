import tkinter
from tkinter import DISABLED, filedialog
from tkinter.font import NORMAL
from distutils.dir_util import copy_tree as ct
import shutil


#posisi awal tombol dan label di window
def awal():
    #variabel dibuat global supaya bisa di panggil fungsi yang lain
    global but, but1, but2, l
    #membuat label judul aplikasi
    l=tkinter.Label(w, text="Program Backup Folder/File",justify="center")
    #membuat tombol pilihan sumber yang akan dibackup
    but=tkinter.Button(text="Nama Folder yang akan di Backup", command=namadir)
    but1=tkinter.Button(text="Nama File yang akan di backup", command=namafile)
    l.pack()
    but.pack()
    but1.pack()

#membatalkan proses backup folder sebelum membackup    
def batal():
    but['state']=NORMAL
    but1['state']=NORMAL
    but2.destroy()
    but3.destroy()
    but4.destroy()
    l2.destroy()
    l3.destroy()

#membatalkan proses backup file sebelum membackup 
def batal1():
    but['state']=NORMAL
    but1['state']=NORMAL
    #but2['state']=NORMAL
    but5.destroy()
    but6.destroy()
    but4.destroy()
    l2.destroy()
    l3.destroy()
    

#Proses backup folder
def bekap():
    src=dirpath
    dest=desti
    ct(src, dest, verbose=1)
    bekap_berhasil()

#Untuk menanmpilakan notifikasi backup folder berhasil, dan menampilkan pilihan keluar atau kembali melakukan backup file atau folder yang lain
def bekap_berhasil():
    global l4,but7
    but.destroy()
    but1.destroy()
    but2.destroy()
    but3.destroy()
    but4.destroy()
    l.destroy()
    l2.destroy()
    l3.destroy()
    l4=tkinter.Label(w, text="Backup Berhasil",justify="center")
    but7=tkinter.Button(text="Backup Lagi", command=reset)
    but8=tkinter.Button(w, text="Selesai", command=w.destroy)
    l4.pack()
    but7.pack()
    but8.pack()

#Untuk menanmpilakan notifikasi backup file berhasil, dan menampilkan pilihan keluar atau kembali melakukan backup file atau folder yang lain
def bekapf_berhasil():
    global l4,but7
    but.destroy()
    but1.destroy()
    but5.destroy()
    but6.destroy()
    but4.destroy()
    l.destroy()
    l2.destroy()
    l3.destroy()
    l4=tkinter.Label(w, text="Backup Berhasil",justify="center")
    but7=tkinter.Button(text="Backup Lagi", command=reset)
    but8=tkinter.Button(w, text="Selesai", command=w.destroy)
    l4.pack()
    but7.pack()
    but8.pack()

#tombol reset kembali keawal
def reset():
    l4.destroy()
    but7.destroy()
    awal()

#Proses backup file
def bekapf():
    shutil.copy2(filepath, despath)
    bekapf_berhasil()      

#mencari file yang akan dibackup
def namafile():
    global l2,but5,filepath
    filepath = filedialog.askopenfilename()
    l2=tkinter.Label(w, text="Nama File yang akan dibackup adalah : " +filepath,justify="center")
    l2.pack()
    but5=tkinter.Button(text="Nama Folder destinasi", command=namadir2)
    but5.pack()
    but['state']=DISABLED
    but1['state']=DISABLED
    print(filepath)

#mencari direktori/folder yang akan dibackup
def namadir():
    global l2,but2,dirpath
    dirpath = filedialog.askdirectory()
    l2=tkinter.Label(w, text="Folder yang akan dibackup adalah : " + dirpath ,justify="center")
    l2.pack()
    but2=tkinter.Button(text="Nama Folder destinasi", command=namadir1)
    but2.pack()
    but1['state']=DISABLED
    but['state']=DISABLED
    print(dirpath)
    
#menentukan destinasi direktori/folder file yang akan dibackup
def namadir1():
    global but3
    global but4
    global l3
    global desti
    desti = filedialog.askdirectory()
    l3=tkinter.Label(w, text="Folder destinasinya adalah : " +desti,justify="center")
    l3.pack()
    but['state']=DISABLED
    but1['state']=DISABLED
    but2['state']=DISABLED
    but3=tkinter.Button(text="Backup", command=bekap)
    but4=tkinter.Button(text="Batal", command=batal) 
    but3.pack()
    but4.pack()
    print(desti)
    print(dirpath)

#menentukan destinasi namafile yang akan dibackup
def namadir2():
    global but6
    global but4
    global l3
    global despath
    despath = filedialog.asksaveasfilename()
    l3=tkinter.Label(w, text="Folder destinasinya adalah : " +despath,justify="center")
    l3.pack()
    but['state']=DISABLED
    but1['state']=DISABLED
    but5['state']=DISABLED
    but6=tkinter.Button(text="Backup", command=bekapf)
    but4=tkinter.Button(text="Batal", command=batal1) 
    but6.pack()
    but4.pack()
    print(filepath)   
    print(despath)
#membuat form window utama
w=tkinter.Tk()
#membuat judul form window
w.title("Tugas Kelompok R DTS PRO")
#memanggil tombol/tampilan awal
awal()
w.mainloop()
