#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================
#=============================================================================================
#Materi 1 : Membuat Node Tree
#=============================================================================================

#class node adalah unit dasar pada tree

class Node:
    def __init__(self, data):
        self.data = data #Menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat sebuah node root
root = Node("A")

#menampilkan isi node 
print("Data pada root:", root.data)
print("Child kiri root:", root.left)
print("Child kanan root:", root.right)

#Penjelasan : 
#1. Program dimulai dengan mendefinisikan class Node
#   Class ini digunakan untuk membuat node pada tree
#   Setiap node memiliki 3 atribut:
#   - data  : menyimpan nilai
#   - left  : menunjuk ke child kiri
#   - right : menunjuk ke child kanan 

#2. Dibuat sebuah objek node sebagai root dengan nilai "A"
#   root = Node("A")
#   Pada tahap ini hanya ada satu node yaitu root dengan data "A" dan kedua child-nya left dan right masih bernilai None atau tidak ada anak
#   - root.data = "A"
#   - root.left = None
#   - root.right = None

#3. Program tidak membuat child (anak) untuk root 
#   sehingga left dan right tetap bernilai None atau tidak ada anak

#4. Program menampilkan isi dari root dan child-nya:
#   - root.data menampilkan "A"
#   - root.left menampilkan None (tidak ada anak kiri)
#   - root.right menampilkan None (tidak ada anak kanan)

#5. Kesimpulan:
#   Tree hanya terdiri dari satu node (root saja)
#   dan belum memiliki cabang (child)