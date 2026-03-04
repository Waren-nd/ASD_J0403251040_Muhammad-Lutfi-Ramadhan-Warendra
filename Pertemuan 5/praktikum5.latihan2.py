#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

# ============================================================================================
# Latihan 2: Tracing Rekursi
# ============================================================================================

def countdown(n):
    # Base case
    if n == 0:
        print("Selesai")
        return

    # Proses sebelum rekursi
    print("Masuk:", n)

    # Recursive call
    countdown(n - 1)

    # Proses setelah rekursi
    print("Keluar:", n)


countdown(3)
#Output "Keluar" muncul terbalik karena:
#rekursi menggunakan sistem stack (LIFO), sehingga fungsi 
#yang terakhir dipanggil akan selesai dan mencetak hasil lebih dulu 
#saat proses kembali (unwinding).
