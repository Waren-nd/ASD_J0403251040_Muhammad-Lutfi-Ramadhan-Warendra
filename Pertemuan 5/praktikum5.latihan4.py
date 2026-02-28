#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

# ============================================================================================
# Latihan 4: Kombinasi Huruf
# ============================================================================================

def kombinasi(n, hasil=""):
    # Base case:
    # Jika panjang string 'hasil' sudah sama dengan n,
    # maka kombinasi sudah lengkap → cetak hasil
    if len(hasil) == n:
        print(hasil)
        return

    # Recursive case:
    # Tambahkan huruf "A" ke hasil, lalu lanjutkan rekursi
    kombinasi(n, hasil + "A")

    # Tambahkan huruf "B" ke hasil, lalu lanjutkan rekursi
    kombinasi(n, hasil + "B")


# Memanggil fungsi untuk membuat kombinasi panjang 2
kombinasi(2)