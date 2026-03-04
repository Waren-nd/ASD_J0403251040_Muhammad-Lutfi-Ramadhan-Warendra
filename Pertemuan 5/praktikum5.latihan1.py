#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

#=============================================================================================
# Latihan 1: Rekursi Pangkat
#=============================================================================================

def pangkat(a, n):
    # Base case:
    # Jika pangkat 0, hasilnya selalu 1
    if n == 0:
        return 1

    # Recursive case:
    # a^n = a × a^(n-1)
    # Bagian ini memanggil fungsi itu sendiri dengan nilai n yang dikurangi 1, sesuai rumus:
    return a * pangkat(a, n - 1)

#Saat print(pangkat(2, 4)) dijalankan, fungsi akan menghitung 2^4 menggunakan rekursi.
print(pangkat(2, 4))  # Output: 16
