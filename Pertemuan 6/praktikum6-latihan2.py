#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

# ============================================================================================
# Latihan 2 . Melengkapi Potongan Kode
# ============================================================================================

def insertion_sort(data):
     for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data [j] > key: # Ubah data[j] < key untuk menjadi descending
            data[j + 1] = data[j]
            j -= 1

        data[j+1] = key

        return data

"""
Soal:
1. Lengkapi kondisi agar menjadi sorting ascending.
Jawaban : 
while j >= 0 and data [j] > key //done

data[j+1] = key

2. Ubah agar menjadi descending. 
Jawaban :
while j >= 0 and data[j] < key:  # diubah untuk descending //done

Karena untuk sorting descending, elemen yang lebih kecil dari key harus digeser 
ke kanan agar nilai yang lebih besar berada di depan, sehingga kondisi diubah 
menjadi data[j] < key

"""