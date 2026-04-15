#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================
#=============================================================================================
#Materi 6 : Struktur Organisasi Perusahaan
#=============================================================================================

#class node adalah unit dasar pada tree

class Node:
    def __init__(self, data):
        self.data = data    #Menyimpan nilai node
        self.left = None    #child kiri
        self.right = None   #child kanan

#Fungsi preorder : Root ==> left ==> right
def preorder(node):
    if node is not None:
        print(node.data, end=" ") #root
        preorder(node.left)      #left
        preorder(node.right)     #right

#membuat tree struktur organisasi
root = Node("Direktur")

#child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child level 2
root.left.left = Node("Staff1")
root.left.right = Node("Staff2")

root.right.right = Node("Staff3")

#Menjalankan Traversal Preorder
print("Struktur Organisasi (preorder):")
preorder(root)

#Penjelasan :

#1. Program mendefinisikan class Node
#   Setiap node menyimpan:
#   - data (nama jabatan)
#   - child kiri (left)
#   - child kanan (right)

#2. Dibuat fungsi preorder(node)
#   Traversal preorder memiliki urutan:
#   Root => Left => Right
#   Artinya:
#   - Cetak node sekarang
#   - Telusuri subtree kiri
#   - Telusuri subtree kanan

#3. Dibuat root dengan nilai "Direktur"
#   Ini adalah posisi tertinggi dalam struktur organisasi

#4. Dibuat child level 1:
#   - Manajer A sebagai anak kiri Direktur
#   - Manajer B sebagai anak kanan Direktur

#5. Dibuat child level 2:
#   - Staff1 dan Staff2 adalah anak dari Manajer A
#   - Staff3 adalah anak kanan dari Manajer B
#   (anak kiri Manajer B tidak ada → None)

#6. Perbedaan dengan contoh tree sebelumnya:
#   - Data sekarang berupa struktur organisasi (teks), bukan huruf A, B, C
#   - Tree tidak lengkap (Manajer B hanya punya 1 child)
#   - Tetap menggunakan konsep binary tree

#7. Saat preorder(root) dijalankan:
#   Urutan traversal:
#   - Direktur (root)
#   - Manajer A (kiri)
#   - Staff1 (kiri dari A)
#   - Staff2 (kanan dari A)
#   - Manajer B (kanan)
#   - Staff3 (kanan dari B)

#8. Output yang dihasilkan:
#   Direktur Manajer A Staff1 Staff2 Manajer B Staff3

#9. Kesimpulan:
#   Preorder traversal cocok untuk menampilkan struktur dari atas ke bawah
#   (dari pimpinan ke bawahan secara berurutan)
#
#         Direktur
#        /      \
#  Manajer A   Manajer B
#    /   \           \
# Staff1 Staff2     Staff3