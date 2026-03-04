#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

# ============================================================================================
# Latihan 4 . Memahami Kode Program (Merge Sort)
# ============================================================================================

def merge_sort(data):
    
    #base case
    if len(data) <= 1:
        return data

    #Divide ; Membagi data menjadi 2 bagian
    mid = len(data) //2
    left = data[:mid] #slicing bagian kiri
    right = data[mid:] #slicing bagian kanan

    #recursive call 
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merged(left_sorted, right_sorted)

def merge(left,right):
    result = []
    i= 0
    j= 0

    #Membandingkan elemen kiri dan kanan, 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1 
        else: 
            result.append(right[j])
            j+=1
    
    #menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result 
"""
Soal:
1. Apa yang dimaksud dengan base case?
Jawaban :Base case adalah kondisi penghentian rekursi yaitu saat panjang data kurang dari atau sama dengan satu karena data tersebut sudah terurut sehingga tidak perlu dibagi lagi.
2. Mengapa fungsi memanggil dirinya sendiri?
Jawaban : Fungsi memanggil dirinya sendiri karena merge sort menggunakan konsep rekursi untuk membagi data menjadi bagian yang lebih kecil hingga mencapai base case sebelum digabungkan kembali.
3. Apa tujuan fungsi merge()?
Jawaban : Tujuan fungsi merge() adalah untuk menggabungkan dua list yang sudah terurut menjadi satu list baru yang tetap terurut.
"""