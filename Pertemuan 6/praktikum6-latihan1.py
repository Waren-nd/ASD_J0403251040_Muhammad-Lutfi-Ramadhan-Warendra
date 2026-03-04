#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

# ============================================================================================
# Latihan 1 . Memahami Kode Program (Insertion Sort)
# ============================================================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i] 
        j = i-1 

        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j -=1

        data[j+1] = key

    return data
"""
Soal:
1. Mengapa perulangan dimulai dari indeks 1?
Jawaban : Karena elemen pertama (index 0) dianggap sudah terurut dengan sendirinya.

2. Apa fungsi variabel key?
Jawaban : Menyimpan nilai sementara, Supaya nilainya tidak hilang saat elemen lain digeser

3. Mengapa digunakan while, bukan for?
Jawaban : Digunakan while karena jumlah pergeseran elemen tidak pasti dan harus berhenti berdasarkan kondisi tertentu.

4. Operasi apa yang terjadi di dalam while?
Jawaban : Di dalam while terjadi proses pergeseran elemen yang lebih besar dari key ke satu posisi ke kanan agar key bisa ditempatkan dengan benar.
"""