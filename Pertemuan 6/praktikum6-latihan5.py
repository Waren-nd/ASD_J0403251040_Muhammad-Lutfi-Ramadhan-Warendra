#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

# ============================================================================================
# Latihan 5 . Melengkapi Fungsi Merge
# ============================================================================================

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
1. Lengkapi kondisi agar menjadi ascending.
Jawaban :
 if left[i] < right[j]: //done
2. Jelaskan fungsi result.extend()
Jawaban : 
result.extend() berfungsi untuk menambahkan sisa elemen yang belum dibandingkan dari salah satu list ke dalam result setelah proses perbandingan utama selesai.
"""