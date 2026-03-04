#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

#=============================================================================================
#Materi Rekursif : Call Stack
# Tracing bilangan (masuk-keluar) 
#input 3
#3-2-1 | 1-2-3
#=============================================================================================

def hitung(n):
    
    # Base case:
    # Jika n == 0, hentikan rekursi
    if n == 0:
        print("selesai")
        return
    
    # Proses sebelum rekursi (fase masuk)
    print("Masuk:", n)

    # Recursive case:
    # Memanggil fungsi dengan n-1
    hitung(n-1)

    # Proses setelah rekursi (fase keluar)
    print("Keluar", n)


print("====== Program Tracing ======")
hitung(3)