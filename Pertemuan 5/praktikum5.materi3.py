#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

#=============================================================================================
#Materi Rekursif : Menjumlahkan Elemen List
#=============================================================================================

def jumlah_list(data, index=0):
    # Base case:
    # Jika index sudah sama dengan panjang list,
    # berarti semua elemen sudah dijumlahkan
    if index == len(data):
        return 0

    # Recursive case:
    # Mengambil nilai pada index saat ini
    # lalu menambahkan dengan hasil pemanggilan
    # fungsi untuk index berikutnya
    return data[index] + jumlah_list(data, index + 1)


print("====== Program Jumlah Data List ======")

# Memanggil fungsi dengan list sebagai parameter
# Fungsi akan menjumlahkan seluruh isi list secara rekursif
print(jumlah_list([2, 4, 6, 8]))