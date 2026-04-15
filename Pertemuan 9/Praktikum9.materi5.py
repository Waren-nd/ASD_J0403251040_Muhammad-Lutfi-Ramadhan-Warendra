#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================
#=============================================================================================
#Materi 5 : Membuat Traversal Postorder
#=============================================================================================

#class node adalah unit dasar pada tree

class Node:
    def __init__(self, data):
        self.data = data    #Menyimpan nilai node
        self.left = None    #child kiri
        self.right = None   #child kanan

#Membuta Traversal Postorder : left ==> right ==> root
def postorder(node):
    if node is not None:
        postorder(node.left)      #left
        postorder(node.right)     #right
        print(node.data, end=" ") #root

#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C") 

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal postorder
print("Hasil Traversal postorder: ")
postorder(root)

#Penjelasan :

#1. Program masih menggunakan class Node yang sama
#   Setiap node memiliki data, child kiri (left), dan child kanan (right)

#2. Ditambahkan fungsi postorder(node)
#   Fungsi ini digunakan untuk traversal dengan urutan:
#   Left => Right => Root

#3. Cara kerja fungsi postorder:
#   - Jika node tidak None:
#       a. Panggil postorder ke child kiri
#       b. Panggil postorder ke child kanan
#       c. Cetak data node (root)

#4. Dibuat root node dengan nilai "A"

#5. Dibuat child level 1:
#   - B sebagai anak kiri A
#   - C sebagai anak kanan A

#6. Dibuat child level 2 (hanya di sisi B):
#   - D sebagai anak kiri B
#   - E sebagai anak kanan B

#7. Perbedaan dengan traversal sebelumnya:
#   - Preorder : Root → Left → Right
#   - Inorder  : Left → Root → Right
#   - Postorder: Left → Right → Root
#   → Pada postorder, root dicetak paling akhir

#8. Saat fungsi postorder(root) dijalankan:
#   Urutan traversal:
#   - D (kiri dari B)
#   - E (kanan dari B)
#   - B (root dari subtree kiri)
#   - C (kanan dari A)
#   - A (root utama)

#9. Output yang dihasilkan:
#   D E B C A

#10. Kesimpulan:
#   Traversal postorder mengunjungi semua child terlebih dahulu,
#   lalu root di akhir.