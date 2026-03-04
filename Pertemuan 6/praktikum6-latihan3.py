#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

# ============================================================================================
# Latihan 3 . Tracing Insertion Sort
# ============================================================================================

"""
Buat program dengan menggunakan algoritma insertion sort
Tracing dengan data = [5, 2, 4, 6, 1, 3]
"""

def insertion_sort(data):
        
    #melihat data awal
    print("Data Awal: ",data)
    print("="*50)

    #Loop mulai dari data ke 2 (index array ke 1) / Array mulai dari 0 
    for i in range(1, len(data)):

        key = data[i] #simpan nilai yang disisipkan
        j = i-1 #index elemen terakhir dibagian kiri

        print("Iterasi ke-", i)
        print("Nilai Key = ", key)
        print("Bagian Kiri (terurut): ", data[:i])
        print("Bagian kanan (belum terutut): ", data[i:])

        #Geser
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j -=1
        #sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah disisipkan :", data)
        print("-"*50)

    return data
angka = [5, 2, 4, 6, 1, 3]
print("Hasil Sorting: ", insertion_sort(angka))

"""
Soal :
1. Tuliskan isi list setelah iterasi i = 1.
Jawaban : 
Isi list setelah terasi ke- 1 adalah [2, 5, 4, 6, 1, 3] 

2. Tuliskan isi list setelah iterasi i = 3.
Jawaban : 
Isi list setelah Iterasi ke- 3 adalah [2, 4, 5, 6, 1, 3]  


3. Berapa kali pergeseran terjadi pada iterasi i = 4? 
Jawaban : 
Pada Iterasi i = 4 Pergeseran yang terjadi: 3 kali (5,4 dan 2 bergeser ke kanan untuk memberi ruang bagi 1).

"""