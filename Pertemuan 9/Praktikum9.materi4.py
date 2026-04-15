#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================
#=============================================================================================
#Materi 4 : Membuat Traversal Inorder
#=============================================================================================

#class node adalah unit dasar pada tree

class Node:
    def __init__(self, data):
        self.data = data    #Menyimpan nilai node
        self.left = None    #child kiri
        self.right = None   #child kanan

#Fungsi Inorder : left ==> root ==> right
def inorder(node):
    if node is not None:
        inorder(node.left)          #left
        print(node.data, end=" ")   #root
        inorder(node.right)         #right

#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C") 

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal inorder
print("Hasil Traversal inorder: ")
inorder(root)

#Penjelasan :

#1. Program masih menggunakan class Node yang sama
#   Setiap node memiliki data, child kiri (left), dan child kanan (right)

#2. Ditambahkan fungsi inorder(node)
#   Fungsi ini digunakan untuk traversal dengan urutan:
#   Left => Root => Right

#3. Cara kerja fungsi inorder:
#   - Jika node tidak None:
#       a. Panggil inorder ke child kiri
#       b. Cetak data node (root)
#       c. Panggil inorder ke child kanan

#4. Dibuat root node dengan nilai "A"

#5. Dibuat child level 1:
#   - B sebagai anak kiri A
#   - C sebagai anak kanan A

#6. Dibuat child level 2 (hanya di sisi B):
#   - D sebagai anak kiri B
#   - E sebagai anak kanan B

#7. Perbedaan dengan preorder:
#   - Preorder: Root → Left → Right
#   - Inorder : Left → Root → Right
#   - Jadi pada inorder, root dicetak di tengah

#8. Saat fungsi inorder(root) dijalankan:
#   Urutan traversal:
#   - D (kiri dari B)
#   - B (root dari subtree kiri)
#   - E (kanan dari B)
#   - A (root utama)
#   - C (kanan dari A)

#9. Output yang dihasilkan:
#   D B E A C

#10. Kesimpulan:
#   Traversal inorder mengunjungi node kiri terlebih dahulu,
#   lalu root, kemudian node kanan
