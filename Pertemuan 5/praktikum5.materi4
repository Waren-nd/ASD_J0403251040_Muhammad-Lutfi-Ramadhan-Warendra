#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

# ==========================================================
# Backtracking 1: Kombinasi Biner (n)
# ==========================================================

def biner(n, hasil=""):
    # Base case:
    # Jika panjang string sudah sama dengan n,
    # maka cetak hasil dan hentikan rekursi
    if len(hasil) == n:
        print(hasil)
        return

    # Recursive case (Choose + Explore):
    # Tambah '0' lalu lanjutkan rekursi
    biner(n, hasil + "0")

    # Tambah '1' lalu lanjutkan rekursi
    biner(n, hasil + "1")
    

# Memanggil fungsi untuk membuat semua kombinasi biner panjang 3
biner(3)