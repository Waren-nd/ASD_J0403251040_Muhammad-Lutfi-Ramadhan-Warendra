#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================
#=============================================================================================
#Latihan 6 : Rotasi Kanan pada BST Tidak Seimbang 
#=============================================================================================

# Class Node
class Node:
    def __init__(self, data):
        self.data = data     # nilai pada node
        self.left = None     # child kiri
        self.right = None    # child kanan


# Preorder Traversal
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)



# Menampilkan Struktur Tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("   " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")



# Fungsi Rotasi Kanan

def rotate_right(y):
    if y is None or y.left is None:
        return y  # tidak bisa rotasi

    x = y.left       # child kiri
    T2 = x.right     # subtree kanan dari x

    # Rotasi
    x.right = y
    y.left = T2

    return x  # root baru


# ----------------------------- 
# Program utama 
# ----------------------------- 
if __name__ == "__main__":
    # Membuat tree tidak seimbang:
    # 30 -> 20 -> 10
    root = Node(30)
    root.left = Node(20)
    root.left.left = Node(10)

    print("Preorder sebelum rotasi kanan:")
    preorder(root)

    print("\n\nStruktur sebelum rotasi kanan:")
    tampil_struktur(root)

    # Rotasi kanan di root
    root = rotate_right(root)

    print("\nPreorder sesudah rotasi kanan:")
    preorder(root)

    print("\n\nStruktur sesudah rotasi kanan:")
    tampil_struktur(root)

#Penjelasan :

#1. Program menggunakan class Node untuk membuat Binary Search Tree (BST)
#   Setiap node memiliki data, child kiri (left), dan child kanan (right)
#2. Dibuat tree secara manual yang tidak seimbang:
#   Data: 30 → 20 → 10 (condong ke kiri)
#3. Struktur awal tree:
#       30
#      /
#    20
#   /
# 10
#4. Ditambahkan fungsi preorder(root)
#   Traversal dengan urutan:
#   Root → Left → Right
#5. Hasil preorder sebelum rotasi:
#   30 20 10
#6. Ditambahkan fungsi tampil_struktur(root)
#   Untuk menampilkan bentuk tree secara bertingkat
#7. Ditambahkan fungsi rotate_right(y)
#   Fungsi ini digunakan untuk melakukan rotasi kanan
#8. Cara kerja rotasi kanan:
#   - y = root lama
#   - x = child kiri dari y
#   - T2 = child kanan dari x (disimpan sementara)
#   - x.right = y (y menjadi anak kanan x)
#   - y.left = T2 (subtree lama dipindahkan)
#   - x menjadi root baru
#9. Proses rotasi:
#   - Node 20 naik menjadi root
#   - Node 30 menjadi anak kanan
#   - Node 10 tetap di kiri
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
#   - Rotasi kanan digunakan untuk mengatasi tree yang miring ke kiri
#   - Membantu menyeimbangkan struktur tree
#   - Root baru diambil dari child kiri