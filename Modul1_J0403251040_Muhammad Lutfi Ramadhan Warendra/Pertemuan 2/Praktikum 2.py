<<<<<<<< HEAD:Pertemuan 2/Praktikum 2.py
#===================================================================
#Pratikum 2 : Konsep ADT dan FIle Handling (STUDI KASUS)
#Latihan 1 : Membuat fungsi load data
#===================================================================

nama_file ="data_mahasiswa.txt"

#membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file):
    data_dict = {} #inisialisasai data dictionary

    with open (nama_file,"r", encoding="latin-1") as file:
        for baris in file:
            baris = baris.strip() #menghilangkan karakter baris baru
            nim, nama, nilai = baris.split(",") #pecah menjadi data satuan
        
        #Simpan data Mahasiswa ke dictioary dengan (key,value)
            data_dict[nim] = {                  #key
                "nama" : nama,                  #values
                "nilai": int(nilai)             #values
            }      

    return data_dict

#memanggil fungsi baca_data_mahasiswa
#buka_data = baca_data_mahasiswa(nama_file)
#print ("jumlah data terbaca", len(buka_data))

#===================================================================
#Pratikum 2 : Konsep ADT dan FIle Handling (STUDI KASUS)
#Latihan 2 : Membuat fungsi menampilkan data
#===================================================================

def tampikan_data(data_dict):
    #membuat Header Tabel
    print("\n==== Daftar Mahasiswa ====")
    print(f"{'NIM':<10}|{'Nama':<12}|{'Nilai':>5}")
    print("-" * 32)
    
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama: <12} | {nilai:>5}")

    """
    untuk tampilan yang rapi, atur f-string formatin
    {'NIM':<10} artinya:
        tampilan nim <= rata kiri dengan lebar 10 karakter
    {'Nama': <12} artinya:
        tampilkan nama rata kiri, dengan lebar kolom 12 karakter
    {'Nilai': >5} artinya:
    tampilkan nilai => rata kanan, dengan lebar 5 karakter
    """
#tampikan_data(buka_data)
#print(buka_data)

#===================================================================
#Pratikum 2 : Konsep ADT dan FIle Handling (STUDI KASUS)
#Latihan 3 : Membuat fungsi mencari data
#===================================================================
def cari_data(data_dict):
    #mencari data mahasiswa berdasarkan NIM
    nim_cari = input("Masukkan NIM yang ingin dicari: ").strip()
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n==== Data Mahasiswa Ditemukan ====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama     : {nama}")
        print(f"Nilai     : {nilai}")
        
    else:
        print("\nData tidak ditemukan")

#cari_data(buka_data)

#===================================================================
#Pratikum 2 : Konsep ADT dan FIle Handling (STUDI KASUS)
#Latihan 4 : Membuat fungsi update nilai
#===================================================================

def update_nilai(data_dict):
    #cari nim mahasiswa yang akan diupdate nilainya
    nim = input("Masukkan NIM Mahasiswa yang akan diupdate niilainya: ")

    if nim not in data_dict:
        print("NIM tidak ditemukan, Update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): "))
    except ValueError:
        print("Nilai harus berupa angka, Update dibatalkan")
        return
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara rentang 0-100, Update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru
    
    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#update_nilai(buka_data)
#print(buka_data)

#===================================================================
#Pratikum 2 : Konsep ADT dan FIle Handling (STUDI KASUS)
#Latihan 5 : Membuat fungsi menyimpan data
#===================================================================

def simpan_data(nama_file,data_dict):
    with open(nama_file,"w", encoding="latin-1") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#simpan_data(nama_file,buka_data)
#print("Data berhasil disimpan")

#===================================================================
#Pratikum 2 : Konsep ADT dan FIle Handling (STUDI KASUS)
#Latihan 6 : Membuat Menu Program
#===================================================================

def main():
    #Menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

    while True:
        print("\n=== Menu Data Mahasiswa===")
        print("1. Tampilkan semua data") #fs no.2
        print("2. Cari data berdasarkan NIM") #fs.no 3
        print("3. Update nilai mahasiswa") #fs no.4
        print("4. Simpan data ke file") # fs no.5
        print("0. Keluar")

        pilihan = input("Pilihan menu: ").strip()
    
        if pilihan == "1":
            tampikan_data(buka_data)

        elif pilihan == "2":
            cari_data(buka_data)
    
        elif pilihan == "3":
            update_nilai(buka_data)
    
        elif pilihan == "4":
            simpan_data(nama_file,buka_data)

        elif pilihan == "0":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
========
#===================================================================
#Pratikum 2 : Konsep ADT dan FIle Handling (STUDI KASUS)
#Latihan 1 : Membuat fungsi load data
#===================================================================

nama_file ="data_mahasiswa.txt"

#membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file):
    data_dict = {} #inisialisasai data dictionary
    try:
        with open(nama_file, "r", encoding="latin-1") as file:
            for baris in file:
                baris = baris.strip() #menghilangkan karakter baris baru
                if not baris:
                    continue
                try:
                    nim, nama, nilai = baris.split(",") #pecah menjadi data satuan
                    data_dict[nim] = {
                        "nama": nama,
                        "nilai": int(nilai)
                    }
                except ValueError:
                    # lewati baris yang tidak sesuai format
                    continue
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan. Membuat file kosong baru.")
        with open(nama_file, "w", encoding="latin-1"):
            pass

    return data_dict

#memanggil fungsi baca_data_mahasiswa
#buka_data = baca_data_mahasiswa(nama_file)
#print ("jumlah data terbaca", len(buka_data))

#===================================================================
#Pratikum 2 : Konsep ADT dan FIle Handling (STUDI KASUS)
#Latihan 2 : Membuat fungsi menampilkan data
#===================================================================

def tampilkan_data(data_dict):
    #membuat Header Tabel
    print("\n==== Daftar Mahasiswa ====")
    print(f"{'NIM':<10}|{'Nama':<12}|{'Nilai':>5}")
    print("-" * 32)
    
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}")

    """
    untuk tampilan yang rapi, atur f-string formatin
    {'NIM':<10} artinya:
        tampilan nim <= rata kiri dengan lebar 10 karakter
    {'Nama': <12} artinya:
        tampilkan nama rata kiri, dengan lebar kolom 12 karakter
    {'Nilai': >5} artinya:
    tampilkan nilai => rata kanan, dengan lebar 5 karakter
    """
#tampikan_data(buka_data)
#print(buka_data)

#===================================================================
#Pratikum 2 : Konsep ADT dan FIle Handling (STUDI KASUS)
#Latihan 3 : Membuat fungsi mencari data
#===================================================================
def cari_data(data_dict):
    #mencari data mahasiswa berdasarkan NIM
    nim_cari = input("Masukkan NIM yang ingin dicari: ").strip()
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n==== Data Mahasiswa Ditemukan ====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama     : {nama}")
        print(f"Nilai     : {nilai}")
        
    else:
        print("\nData tidak ditemukan")

#cari_data(buka_data)

#===================================================================
#Pratikum 2 : Konsep ADT dan FIle Handling (STUDI KASUS)
#Latihan 4 : Membuat fungsi update nilai
#===================================================================

def update_nilai(data_dict):
    #cari nim mahasiswa yang akan diupdate nilainya
    nim = input("Masukkan NIM Mahasiswa yang akan diupdate nilainya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan, Update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): "))
    except ValueError:
        print("Nilai harus berupa angka, Update dibatalkan")
        return
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara rentang 0-100, Update dibatalkan")
        return

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru
    
    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#update_nilai(buka_data)
#print(buka_data)

#===================================================================
#Pratikum 2 : Konsep ADT dan FIle Handling (STUDI KASUS)
#Latihan 5 : Membuat fungsi menyimpan data
#===================================================================

def simpan_data(nama_file,data_dict):
    with open(nama_file,"w", encoding="latin-1") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#simpan_data(nama_file,buka_data)
#print("Data berhasil disimpan")

#===================================================================
#Pratikum 2 : Konsep ADT dan FIle Handling (STUDI KASUS)
#Latihan 6 : Membuat Menu Program
#===================================================================

def main():
    #Menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

    while True:
        print("\n=== Menu Data Mahasiswa===")
        print("1. Tampilkan semua data") #fs no.2
        print("2. Cari data berdasarkan NIM") #fs.no 3
        print("3. Update nilai mahasiswa") #fs no.4
        print("4. Simpan data ke file") # fs no.5
        print("0. Keluar")

        pilihan = input("Pilihan menu: ").strip()
    
        if pilihan == "1":
            tampilkan_data(buka_data)

        elif pilihan == "2":
            cari_data(buka_data)
    
        elif pilihan == "3":
            update_nilai(buka_data)
    
        elif pilihan == "4":
            simpan_data(nama_file,buka_data)

        elif pilihan == "0":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
>>>>>>>> 5e04aa4400d1526057c3fa156c16015a0a52c320:Modul1_J0403251040_Muhammad Lutfi Ramadhan Warendra/Pertemuan 2/Praktikum 2.py
    main()