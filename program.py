daftar_kontak = []
daftar_kontak.append({
    "nama" : "acim",
    "email" : "acimcemungut@gmail.com",
    "telepon" : "082345678999"
})

def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("=================")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")

def new_kontak():
    nama = input("Nama : ")
    email = input("Email : ")
    telepon = input("Telepon/No Wa : ")
    kontak = {
        "nama": nama,
        "email" : email,
        "telepon" : telepon
    }
    return kontak

def hapus_kontak(daftar_kontak):
    telepon = input("Nomer telepon yang akan di hapus : ")

    index = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon == kontak ["telepon"]:
            index = i
            break
    
    if index == -1:
        print("Data kontak tidak ditemukan")
    else:
        del daftar_kontak[index]
        print("Berhasil menghapus data kontak")

def cari_kontak(daftar_kontak):
    nama_yg_dicari = input("Nama yang dicari : ")

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(nama_yg_dicari.lower()) != -1:
            print("==================")
            print(f"Nama : {kontak['nama']}")
            print(f"Email : {kontak['email']}")
            print(f"Telepon : {kontak['telepon']}")
        
while True:
    print("#Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar Program")

    menu = input("Pilih menu : ")

    if menu == "0":
        break
    elif menu == "1":
        display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = new_kontak()
        daftar_kontak.append(kontak)
    elif menu == "3":
        daftar_kontak
        hapus_kontak(daftar_kontak)
    elif menu == "4":
        cari_kontak(daftar_kontak)
    else:
        print("Menu tidak ditemukan")

print("Program Selesai")