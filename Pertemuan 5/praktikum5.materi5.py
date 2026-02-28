#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

# ============================================================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ============================================================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Pruning:
    # Jika jumlah angka '1' sudah melebihi batas,
    # hentikan rekursi (tidak lanjut eksplorasi)
    if jumlah_1 > batas:
        return

    # Base case:
    # Jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return

    # Recursive case (Choose + Explore)

    # Pilih '0' → jumlah_1 tidak bertambah
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # Pilih '1' → jumlah_1 bertambah 1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)


# Memanggil fungsi
biner_batas(4, 2)