#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================
#=============================================================================================
#Latihan 5 : Rotasi Kiri pada BST Tidak Seimbang 
#=============================================================================================

# Class Node 
class Node: 
    def __init__(self, data): 
        self.data = data  # nilai pada node
        self.left = None  # child kiri
        self.right = None # child kanan
 
 
# Fungsi preorder untuk melihat isi tree 
def preorder(root): 
    if root is not None: 
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right) 
 
 
# Fungsi untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L") 
        tampil_struktur(root.right, level + 1, "R") 
 
 
# Fungsi rotasi kiri 
def rotate_left(x): 
    # x adalah root lama 
    y = x.right       # y adalah child kanan x 
    T2 = y.left       # subtree kiri milik y disimpan sementara 
 
    # Proses rotasi 
    y.left = x        # x menjadi child kiri dari y 
    x.right = T2      # child kanan x diganti dengan T2 
 
    # y menjadi root baru 
    return y 
 
# ----------------------------- 
# Program utama 
# ----------------------------- 
if __name__ == "__main__":
    root = None
# Membuat tree yang tidak seimbang: 
# 10 -> 20 -> 30 
    root = Node(10) 
    root.right = Node(20) 
    root.right.right = Node(30) 
    print("Preorder sebelum rotasi kiri:") 
    preorder(root) 
    print("\n\nStruktur sebelum rotasi kiri:") 
    tampil_struktur(root) 
    # Melakukan rotasi kiri pada root 
    root = rotate_left(root) 
    print("\nPreorder sesudah rotasi kiri:") 
    preorder(root) 
    print("\n\nStruktur sesudah rotasi kiri:") 
    tampil_struktur(root) 

#Penjelasan :

#1. Program menggunakan class Node untuk membuat Binary Search Tree (BST)
#   Setiap node memiliki data, child kiri (left), dan child kanan (right)
#2. Dibuat tree secara manual yang tidak seimbang:
#   Data: 10 → 20 → 30 (condong ke kanan)
#3. Struktur awal tree:
#   10
#     \
#      20
#        \
#         30
#4. Ditambahkan fungsi preorder(root)
#   Traversal dengan urutan:
#   Root → Left → Right
#5. Hasil preorder sebelum rotasi:
#   10 20 30
#6. Ditambahkan fungsi tampil_struktur(root)
#   Untuk menampilkan bentuk tree secara bertingkat
#7. Ditambahkan fungsi rotate_left(x)
#   Fungsi ini digunakan untuk melakukan rotasi kiri
#8. Cara kerja rotasi kiri:
#   - x = root lama
#   - y = child kanan dari x
#   - T2 = child kiri dari y (disimpan sementara)
#   - y.left = x (x menjadi anak kiri y)
#   - x.right = T2 (subtree lama dipindahkan)
#   - y menjadi root baru
#9. Proses rotasi:
#   - Node 20 naik menjadi root
#   - Node 10 menjadi anak kiri
#   - Node 30 tetap di kanan
#10. Struktur setelah rotasi:
#       20
#      /  \
#    10   30
#11. Hasil preorder sesudah rotasi:
#   20 10 30
#12. Output struktur:
#   Root: 20
#      L: 10
#      R: 30
#13. Kesimpulan:
#   - Rotasi kiri digunakan untuk mengatasi tree yang miring ke kanan
#   - Membantu menyeimbangkan struktur tree
#   - Root baru diambil dari child kanan