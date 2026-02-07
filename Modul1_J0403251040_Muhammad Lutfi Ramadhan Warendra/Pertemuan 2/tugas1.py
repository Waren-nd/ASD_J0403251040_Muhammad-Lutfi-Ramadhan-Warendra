# ========================================================== 
# TUGAS HANDS-ON MODUL 1 
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt) 
# 
# Nama  : Muhammad Lutfi Ramadhan Warendra 
# NIM   : J0403251040
# Kelas : B2
# ========================================================== 
# ------------------------------- 
# Konstanta nama file 
# ------------------------------- 
NAMA_FILE = "stok_barang.txt" 
# ------------------------------- 
# Fungsi: Membaca data dari file 
# ------------------------------- 
def baca_stok(nama_file): 
    stok_dict = {} #inisialisasai data dictionary
#membuat fungsi membaca file stok_barang
    with open ("stok_barang.txt","r", encoding="latin-1") as file:
        for baris in file:
            baris = baris.strip() #menghilangkan karakter baris baru
            if baris == "":
                continue
            kode, nama, stok = baris.split(",") #pecah menjadi data satuan
            #Simpan data stok barang ke dictioary dengan (key,value)
            stok_dict[kode] = {
                    "nama": nama,
                    "stok": int(stok)
            }
# TODO: Buka file dan baca seluruh baris 
# Hint: with open(nama_file, "r", encoding="utf-8") as f: 
# TODO: Untuk setiap baris: 
# - gunakan strip() untuk menghilangkan \n 
# - split(",") untuk memisahkan kolom 
# - simpan ke dictionary
        
    return stok_dict 
# ------------------------------- 
# Fungsi: Menyimpan data ke file 
# ------------------------------- 
def simpan_stok(nama_file, stok_dict): # Fungsi ini menyimpan seluruh data stok ke file teks.
# TODO: Tulis ulang seluruh isi file berdasarkan stok_dict 
# Hint: with open(nama_file, "w", encoding="utf-8") as f: 
    with open ("stok_barang.txt","w", encoding="latin-1") as file:
        for kode, data in stok_dict.items():
            file.write(f"{kode},{data['nama']},{data['stok']}\n")

# ------------------------------- 
# Fungsi: Menampilkan semua data 
# ------------------------------- 
def tampilkan_semua(stok_dict):
    #menampilkan semua barang yang ada di stok.
    if not stok_dict:
        print("Stok barang kosong.")
        return

    print("\nKode   | Nama Barang | Stok")
    print("-" * 55)
    for kode, data in stok_dict.items():
        print(f"{kode:<15} | {data['nama']:<25} | {data['stok']:>10}")
    # Menampilkan setiap data barang
# TODO: Jika kosong, tampilkan pesan stok kosong 
# TODO: Tampilkan dengan format rapi: kode | nama | stok


# ------------------------------- 
# Fungsi: Cari barang berdasarkan kode 
# ------------------------------- 
def cari_barang(stok_dict): 
    #Mencari barang berdasarkan kode barangnya
    kode = input("Masukkan kode barang: ").strip() 

    if kode in stok_dict:
        data = stok_dict[kode]
        print("Data barang ditemukan:")
        print(f"Kode : {kode}")
        print(f"Nama : {data['nama']}")
        print(f"Stok : {data['stok']}")
    else:
        print("Barang tidak ditemukan")
# TODO: Cek apakah kode ada di dictionary 
# Jika ada: tampilkan detail barang 
# Jika tidak ada: tampilkan 'Barang tidak ditemukan'

# ------------------------------- 
# Fungsi: Tambah barang baru 
# ------------------------------- 
def tambah_barang(stok_dict): 
    kode = input("Masukkan kode barang baru: ").strip()
    if kode in stok_dict:
        print("Kode sudah digunakan")
        return
    
    nama = input("Masukkan nama barang: ").strip() 
    stok_awal = int(input("Masukkan stok awal"))

    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }
print("Barang berhasil ditambahkan")

# TODO: Validasi kode tidak boleh duplikat 
# Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return 
# TODO: Input stok awal (integer) 
# Hint: stok_awal = int(input(...)) 
# TODO: Simpan ke dictionary 

# ------------------------------- 
# Fungsi: Update stok barang 
# ------------------------------- 
def update_stok(stok_dict): #Mengubah stok barang +/-
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip() 

    if kode not in stok_dict:
        print("Barang tidak ditemukan")
        return

    # TODO: Cek apakah kode ada di dictionary 
    # Jika tidak ada: tampilkan pesan dan return 
    
    print("Pilih jenis update:") 
    print("1. Tambah stok") 
    print("2. Kurangi stok") 
    
    pilihan = input("Masukkan pilihan (1/2): ").strip() 
    jumlah = int(input("Masukkan jumlah: "))
    # TODO: Input jumlah perubahan stok 
    # Hint: jumlah = int(input("Masukkan jumlah: ")) 

    if pilihan =="1":   #Menambah stok
        stok_dict[kode]["stok"] += jumlah
        print("Stok berhasil ditambahkan")
    elif pilihan == "2": # Mengurangi stok
        if stok_dict[kode]["stok"] - jumlah < 0:
            print("Error: Stok tidak boleh negatif.")
        else:
            stok_dict[kode]["stok"] -= jumlah
            print("Stok berhasil dikurangi.")
    else:
        print("Pilihan tidak valid.")

    
    # TODO: 
    # - Jika pilihan 1: stok = stok + jumlah 
    # - Jika pilihan 2: stok = stok - jumlah 
    # - Jika hasil < 0: batalkan dan tampilkan error

# ------------------------------- 
# Program Utama 
# ------------------------------- 
def main(): 
    # Membaca data dari file saat program mulai 
    stok_barang = baca_stok(NAMA_FILE) 
 
    while True: 
        print("\n=== MENU STOK KANTIN ===") 
        print("1. Tampilkan semua barang") 
        print("2. Cari barang berdasarkan kode") 
        print("3. Tambah barang baru") 
        print("4. Update stok barang") 
        print("5. Simpan ke file") 
        print("0. Keluar") 
 
        pilihan = input("Pilih menu: ").strip() 
 
        if pilihan == "1": 
            tampilkan_semua(stok_barang) 
 
        elif pilihan == "2": 
            cari_barang(stok_barang) 
 
        elif pilihan == "3": 
            tambah_barang(stok_barang) 
 
        elif pilihan == "4": 
            update_stok(stok_barang) 
 
        elif pilihan == "5": 
            simpan_stok(NAMA_FILE, stok_barang) 
            print("Data berhasil disimpan.") 
 
        elif pilihan == "0": 
            print("Program selesai.") 
            break 
        else: 
            print("Pilihan tidak valid. Silakan coba lagi.") 
# Menjalankan program utama 
if __name__ == "__main__": 
    main()