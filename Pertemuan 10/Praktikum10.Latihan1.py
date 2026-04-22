#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================
#=============================================================================================
#Latihan 1 : BST
#=============================================================================================

class Node:
    def __init__(self,data):    # constructor untuk membuat node baru
        self.data = data        # menyimpan nilai pada node
        self.left = None        # pointer child kiri
        self.right = None       # pointer child kanan


def insert(root,data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left,data)
    elif data > root.data:
        root.right = insert(root.right,data)

    return root

#Mengisi data BST
root = None
data_list = [50,30,70,20,40,50,80]

for data in data_list:
    root = insert(root,data)

print("BST berhasil dibuat")

#Penjelasan :

#1. Program menggunakan class Node untuk membentuk Binary Search Tree (BST)
#   Setiap node memiliki data, child kiri (left), dan child kanan (right)
#2. Ditambahkan fungsi insert(root, data)
#   Fungsi ini digunakan untuk memasukkan data ke dalam BST
#3. Cara kerja fungsi insert:
#   - Jika root None → buat node baru
#   - Jika data < root.data → masuk ke kiri
#   - Jika data > root.data → masuk ke kanan
#   - Jika sama (duplikat) → tidak dimasukkan
#   - Proses dilakukan secara rekursif
#4. Data dimasukkan: [50, 30, 70, 20, 40, 50, 80]
#5. Urutan pembentukan tree:
#   - 50 jadi root
#   - 30 di kiri 50
#   - 70 di kanan 50
#   - 20 di kiri 30
#   - 40 di kanan 30
#   - 50 (duplikat) tidak dimasukkan
#   - 80 di kanan 70
#6. Struktur tree:
#         50
#        /  \
#      30    70
#     /  \     \
#   20   40     80
#7. Kesimpulan:
#   BST menyusun data dengan aturan kiri < root < kanan

#=============================================================================================
#Latihan 2 : Traversal Inorder
#=============================================================================================
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print("Hasil Inorder:")
inorder(root)

#Penjelasan :

#1. Ditambahkan fungsi inorder(root)
#   Fungsi ini digunakan untuk traversal dengan urutan:
#   Left → Root → Right
#2. Cara kerja fungsi inorder:
#   - Jika node tidak None:
#       a. Panggil inorder ke kiri
#       b. Cetak data node
#       c. Panggil inorder ke kanan
#3. Saat inorder(root) dijalankan:
#   Urutan traversal:
#   20 → 30 → 40 → 50 → 70 → 80
#4. Output:
#   20 30 40 50 70 80
#5. Kesimpulan:
#   Traversal inorder menghasilkan data terurut (ascending) pada BST

#=============================================================================================
#Latihan 3 : Search di BST
#=============================================================================================

def search(root,key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left,key)
    else:
        return search(root.right,key)

#uji pencarian
key = 100

if search(root,key):
    print("Data Ditemukan")
else:
    print("Data Tidak Ditemukan")

#Penjelasan :

#1. Ditambahkan fungsi search(root, key)
#   Fungsi ini digunakan untuk mencari data dalam BST
#2. Cara kerja fungsi search:
#   - Jika root None → return False
#   - Jika root.data == key → return True
#   - Jika key < root.data → cari ke kiri
#   - Jika key > root.data → cari ke kanan
#   - Proses dilakukan secara rekursif
#3. Contoh pencarian key = 100:
#   - 100 > 50 → ke kanan
#   - 100 > 70 → ke kanan
#   - 100 > 80 → ke kanan
#   - Tidak ditemukan → berhenti
#4. Output:
#   Data Tidak Ditemukan
#5. Kesimpulan:
#   Search pada BST lebih efisien karena langsung menuju arah yang sesuai