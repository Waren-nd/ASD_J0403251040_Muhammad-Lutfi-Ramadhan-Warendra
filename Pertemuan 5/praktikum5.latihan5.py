#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

# ============================================================================================
# Latihan 5: Studi Kasus: Generator PIN
# ============================================================================================

def buat_pin(panjang, hasil=""):
    # Base case:
    # Jika panjang string 'hasil' sudah sama dengan panjang yang diinginkan,
    # maka PIN sudah lengkap → cetak hasil
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # Recursive case:
    # Ulangi untuk setiap kemungkinan angka
    for angka in ["0", "1", "2"]:
        # Tambahkan angka ke 'hasil' lalu lanjutkan rekursi
        buat_pin(panjang, hasil + angka)


# Memanggil fungsi untuk membuat PIN sepanjang 3 digit
buat_pin(3)