#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================
#=============================================================================================
#Materi 3 : Membuat Traversal Preorder
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

#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C") 

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal preorder
print("Hasil Traversal Preorder: ")
preorder(root)

#Penjelasan :

#1. Program masih menggunakan class Node yang sama
#   Setiap node memiliki data, child kiri (left), dan child kanan (right)

#2. Ditambahkan fungsi preorder(node)
#   Fungsi ini digunakan untuk traversal (menelusuri) tree dengan urutan:
#   Root => Left => Right

#3. Cara kerja fungsi preorder:
#   - Jika node tidak None:
#       a. Cetak data node (root)
#       b. Panggil preorder ke child kiri
#       c. Panggil preorder ke child kanan

#4. Dibuat root node dengan nilai "A"

#5. Dibuat child level 1:
#   - B sebagai anak kiri A
#   - C sebagai anak kanan A

#6. Dibuat child level 2 (hanya di sisi B):
#   - D sebagai anak kiri B
#   - E sebagai anak kanan B

#7. Perbedaan dengan kode sebelumnya:
#   - Sekarang menggunakan traversal (preorder), bukan print satu-satu
#   - Tidak semua node ditampilkan manual, tapi otomatis lewat fungsi
#   - Tree belum lengkap (tidak ada child untuk C → F dan G belum dibuat)

#8. Saat fungsi preorder(root) dijalankan:
#   Urutan traversal:
#   - A (root)
#   - B (kiri A)
#   - D (kiri B)
#   - E (kanan B)
#   - C (kanan A)

#9. Output yang dihasilkan:
#   A B D E C

#10. Kesimpulan:
#   Program ini memperkenalkan konsep traversal preorder
#   untuk menelusuri isi tree secara otomatis dan simple tanpa harus print manual setiap node