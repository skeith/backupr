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
# print statement debugging
# print(tgex)
# print(tgbak)

def bakd(src, dest):
    """Menerima dua parameter yaitu
    src: sumber folder yang ingin dibackup
    dest: lokasi tujuan backup

    Input harus berupa lokasi absolut"""
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

# print("Pilih opsi backup\n")
# print("1 : Backup folder")
# print("2 : Backup file")
# print("")

# if else
    if opt == 1:
        print("Gunakan lokasi absolut")
        a = input("Lokasi folder sumber: ")
        b = input("Lokasi tujuan backup: ")
        bakd(a, b)
    elif opt == 2:
        print("Opsi belum siap")
    elif opt == 3:
        exit()
    else:
        print("Opsi tidak ada")
