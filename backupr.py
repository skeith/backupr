import shutil
import os
from datetime import datetime
from distutils.dir_util import copy_tree as ct
from distutils import log

# set variables
log.set_verbosity(log.INFO)
log.set_threshold(log.INFO)
tgex = datetime.now()
tgbak = tgex.strftime("%Y.%m.%d-%H.%M")

def bakd():
    """Menerima dua parameter yaitu
    src: sumber folder yang ingin dibackup
    dest: lokasi tujuan backup

    Input harus berupa lokasi absolut"""
    print("Gunakan lokasi absolut")
    src = input("Lokasi folder sumber: ")
    dest = input("Lokasi tujuan backup: ")
    try:
        if not src:
            print("Sumber folder yang ingin dibackup harus dimasukkan")
            return
        if not dest:
            print("Lokasi tujuan backup harus dimasukkan")
            return
        # copy action
        ct(src, dest, verbose=1)
        print("Backup sukses")
        return
    except FileNotFoundError:
        print("Lokasi tidak ditemukan!\n Gunakan lokasi absolut")
        return

def bakf():
    """Menerima empat parameter yaitu
    src: sumber folder lokasi file
    sercf: nama file yang ingin dibackup
    dest: lokasi folder tujuan backup
    destf: nama file hasil backup (opsional, apabila tidak diberikan maka menggunakan nama file sumber

    Input folder harus berupa lokasi absolut
    hasil backup otomatis ditambahkan timestamp"""
    src = input("Lokasi folder sumber: ")
    srcf = input("Nama file yang ingin dibackup (beserta extensi): ")
    dest = input("Lokasi folder tujuan backup: ")
    destf = input("Nama file tujuan backup (kosongkan jika ingin menggunakan nama yang sama): ")
    pisah = "-"
    try:
        if not src and not srcf:
            print("Sumber file yang ingin dibackup harus dimasukkan")
            return
        if not dest:
            print("Lokasi tujuan backup harus dimasukkan")
            return

        # copy action
        if not destf:
            destf = srcf
        fname, extname = os.path.splitext(destf)
        shutil.copy2(os.path.join(src, srcf), os.path.join(dest,fname+pisah+tgbak+extname))
        print("Backup sukses")
        return
    except FileNotFoundError:
        print("Lokasi atau file tidak ditemukan!\n Gunakan lokasi absolut")
        return

# menu
menu = {
    1: 'Backup folder',
    2: 'Backup file',
    3: 'Keluar',
}

def show_menu():
    for opsi in menu.keys():
        print(opsi, '=', menu[opsi])

while True:
    show_menu()
    opt = int(input("Ketik opsi: "))

    if opt == 1:
        bakd()
    elif opt == 2:
        bakf()
    elif opt == 3:
        exit()
    else:
        print("Opsi tersebut tidak ada")
