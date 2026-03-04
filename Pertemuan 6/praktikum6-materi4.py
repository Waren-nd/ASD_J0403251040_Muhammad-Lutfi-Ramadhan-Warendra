#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

# ============================================================================================
# Merge Sort dengan tracing
# ============================================================================================

def merge_sort(data,depth=0):
    indent = " " * depth # Indentasi berdasarkan level rekursif
    print(f"{indent}merge_sort({data})")
    
    #base case
    if len(data) <= 1:
        return data

    #Divide ; Membagi data menjadi 2 bagian
    mid = len(data) //2
    left = data[:mid] #slicing bagian kiri
    right = data[mid:] #slicing bagian kanan

    print(f"{indent}divide -> left = {left} | right = {right}")

    #recursive call 
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    merged = merge(left_sorted(left))
    print(f"{indent}merge -> {left_sorted} + {right_sorted} = {merged}")

    return merged

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

angka = [13,7,28,5,19,4]
print("Hasil Sorting: ", merge_sort(angka))

