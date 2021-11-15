# membuat variable terlebih dahulu entah variable tunggal atau variable list
pin = '123456'
saldo = 1500000
list = ['Info saldo','Penarikan tunai','Setor Uang','exit']
l_penarikan = ['Rp.50.000','Rp.100.000','Rp.200.000','Rp.250.000']
l_setor = ['Rp.50.000','Rp.100.000','Rp.200.000','Rp.250.000']

# membuat heading untuk pembuka bank kita buat perulangan untuk pin yang akan kita masukkan dengan ketentuan jika lebih dari 3 kali salah maka program akan berhenti
print('Selamat datang di ATM Bank Krut')
for i in range(3):
    inPin = input("Silakan masukkan pin anda :")
    if inPin == pin :
        print("pin yang anda masukkan benar")
        break
    else:
        print("pin anda salah") 
        # kita beri logika agar tahu ketika pin yang dimasukkan tersebut melebihi 3 kali 
        if i == 2 :
            print("Maaf kami tidak bisa jalankan")
            quit() #fungsi ini digunakan untuk menghentikan program
#untuk melanjutkan program ketika sudah benarkita membuat programnya dengan menggunakan program pengulangan while
while True:
    print("============================")
    print("Silakan pilih pilih MENU")
    for item in range(0, len(list)):
        print(f'{item +1}.{list[item]}')
    item_menu = input('Silahkan Pilih Platfom 1-4 : ')
    if item_menu == "1":
        print(f"Saldo anda berjumlah:{saldo} ")

    elif item_menu == "2":
        for item_penarikan in range(0,len(l_penarikan)):
            print(f'{item_penarikan +1}.{l_penarikan[item_penarikan]}')
        pilih_penarikan = input('Berapa yang akan diambil :')
        if pilih_penarikan == "1":
            if saldo < 50000 :
                print("maaf saldo kurang")
            else:
                total = saldo - 50000
                print(f"total saldo anda: {total}")
            continue
        elif pilih_penarikan == "2":
            if saldo < 100000 :
                print("maaf saldo kurang")
            else:
                total = saldo - 100000
                print(f"total saldo anda: {total}")
            continue
        elif pilih_penarikan == "3":
            if saldo < 200000 :
                print("maaf saldo kurang")
            else:
                total = saldo - 200000
                print(f"total saldo anda: {total}")
            continue
        elif pilih_penarikan == "4":
            if saldo < 250000 :
                print("maaf saldo kurang")
            else:
                total = saldo - 250000
                print(f"total saldo anda: {total}")
            continue
        else:
            print("ATM eror")
        continue

    elif item_menu == "3":
        for item_setor in range(0,len(l_setor)):
            print(f'{item_setor +1}.{l_setor[item_setor]}')
        pilih_setoran = input('Berapa yang akan disetorkan :')
        if pilih_setoran == "1":
            setoran = saldo + 50000
            print(f"Uang yang anda setorkan senilai {setoran} ")
            continue
        elif pilih_setoran == "2":
            setoran = saldo + 100000
            print(f"Uang yang anda setorkan senilai {setoran} ")
            continue
        elif pilih_setoran == "3":
            setoran = saldo + 200000
            print(f"Uang yang anda setorkan senilai {setoran} ")
            continue
        elif pilih_setoran == "4":
            setoran = saldo + 250000
            print(f"Uang yang anda setorkan senilai {setoran} ")
            continue
        else:
            print("ATM eror")
        continue

    elif item_menu == "4":
        pilih = input('Apakah mau melanjutkan ? y/n:')
        if pilih == 'y' or pilih == 'Y':
            continue
        elif pilih == 'N' or pilih == 'n':
            print('proses berakhir')
            break
        else:
            print("Maaf bisa tidak diproses")

    else:
        print("Eror")

    