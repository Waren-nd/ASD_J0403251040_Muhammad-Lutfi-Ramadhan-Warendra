#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================
#=============================================================================================
#Materi 2 : Membuat Binary node tree sederhana
#=============================================================================================

#class node adalah unit dasar pada tree

class Node:
    def __init__(self, data):
        self.data = data    #Menyimpan nilai node
        self.left = None    #child kiri
        self.right = None   #child kanan

#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C") 

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

root.right.left = Node("F")
root.right.right = Node("G")


#menampilkan isi node 
print("Data pada root:", root.data)
print("Child kiri root:", root.left.data)
print("Child kanan root:", root.right.data)
print("Child kiri dari B:", root.left.left.data)
print("Child kanan dari B:", root.left.right.data)
print("Child kiri dari C:", root.right.left.data)
print("Child kanan dari C:", root.right.right.data)

#Penjelasan :

#1. Program masih menggunakan class Node yang sama seperti sebelumnya
#   Setiap node memiliki data, child kiri (left), dan child kanan (right)

#2. Dibuat root node dengan nilai "A"
#   root.data = "A"
#   root.left = None
#   root.right = None

#3. Perbedaan dari kode sebelumnya:
#   Sekarang root sudah memiliki child (anak)
#   - root.left = Node("B")  => anak kiri dari A
#   - root.right = Node("C") => anak kanan dari A

#4. Selanjutnya dibuat child level 2 untuk node B
#   - root.left.left = Node("D")  => anak kiri dari B
#   - root.left.right = Node("E") => anak kanan dari B

#5. Ditambahkan juga child level 2 untuk node C
#   - root.right.left = Node("F")  => anak kiri dari C
#   - root.right.right = Node("G") => anak kanan dari C

#6. Perbedaan utama dengan kode sebelumnya:
#   sekarang tree sudah memiliki struktur yang lebih lengkap dengan 3 level (A, B-C, D-E-F-G):
#   Sebelumnya tree hanya memiliki 1 node (A saja)
#   idak ada lagi nilai None pada child yang sudah diisi

#7. Program menampilkan semua isi node:
#   - root (A)
#   - child kiri & kanan dari root (B dan C)
#   - child dari B (D dan E)
#   - child dari C (F dan G)

#8. Kesimpulan:
#   Struktur tree sekarang berbentuk binary tree lengkap:

#           A
#         /   \
#        B     C
#       / \   / \
#      D   E F   G