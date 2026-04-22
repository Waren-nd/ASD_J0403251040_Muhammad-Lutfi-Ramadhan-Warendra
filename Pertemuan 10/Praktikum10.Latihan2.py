#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================
#=============================================================================================
#Latihan 4 : Membuat BST yang Tidak Seimbang
#=============================================================================================

# Class Node untuk menyimpan data BST 
class Node: 
    def __init__(self, data): 
        self.data = data      # nilai pada node 
        self.left = None      # child kiri 
        self.right = None     # child kanan 
 
 
# Fungsi insert untuk BST 
def insert(root, data): 
    # Jika root kosong, buat node baru 
    if root is None: 
        return Node(data) 
 
    # Jika data lebih kecil, masuk ke subtree kiri 
    if data < root.data: 
        root.left = insert(root.left, data) 
 
    # Jika data lebih besar, masuk ke subtree kanan 
    elif data > root.data: 
        root.right = insert(root.right, data) 
 
    return root 
 
 
# Fungsi Traversal Preorder untuk melihat bentuk tree 
def preorder(root): 
    if root is not None: 
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right) 
 
 
# Fungsi sederhana untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L") 
        tampil_struktur(root.right, level + 1, "R")

# ----------------------------- 
# Program utama 
# ----------------------------- 
if __name__ == "__main__":
    root = None 
# Data dimasukkan berurutan naik 
    data_list = [10, 20, 30] 

    for data in data_list: 
        root = insert(root, data) 

    print("Preorder BST:") 
    preorder(root) 
    print("\n\nStruktur BST:") 
    tampil_struktur(root)  

#Penjelasan :

#1. Program menggunakan class Node untuk membuat Binary Search Tree (BST)
#   Setiap node memiliki data, child kiri (left), dan child kanan (right)
#2. Ditambahkan fungsi insert(root, data)
#   Fungsi ini digunakan untuk memasukkan data ke dalam BST
#3. Cara kerja fungsi insert:
#   - Jika root None → buat node baru
#   - Jika data < root.data → masuk ke kiri
#   - Jika data > root.data → masuk ke kanan
#   - Proses dilakukan secara rekursif sampai menemukan posisi kosong
#4. Data dimasukkan: [10, 20, 30]
#   Data dimasukkan secara berurutan naik
#5. Proses pembentukan tree:
#   - 10 menjadi root
#   - 20 lebih besar dari 10 → masuk ke kanan
#   - 30 lebih besar dari 10 → ke kanan
#     lalu lebih besar dari 20 → ke kanan lagi
#6. Struktur tree yang terbentuk:
#   10
#     \
#      20
#        \
#         30
#7. Tree menjadi tidak seimbang (unbalanced)
#   Karena semua node condong ke kanan (seperti linked list)
#8. Ditambahkan fungsi preorder(root)
#   Traversal dengan urutan:
#   Root → Left → Right
#9. Hasil preorder:
#   10 20 30
#10. Ditambahkan fungsi tampil_struktur(root)
#    Fungsi ini menampilkan bentuk tree secara bertingkat
#11. Output struktur:
#   Root: 10
#      R: 20
#         R: 30
#12. Kesimpulan:
#   - Jika data dimasukkan berurutan (naik/turun), BST bisa menjadi tidak seimbang
#   - Tree yang tidak seimbang membuat pencarian menjadi kurang efisien
#   - Bentuknya menyerupai seperti linked list