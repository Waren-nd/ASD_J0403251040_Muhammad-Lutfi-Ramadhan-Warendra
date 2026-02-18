#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

#=============================================================================================
#Implementasi Dasar : Node pada Linked List
#=============================================================================================

#Membuat kelas node (merupakan unit dasar dari Linked List)
class Node:
    def __init__(self,data): #konstruktor untuk inisialisasi node
        self.data = data #Menyimpan nilai/data
        self.next = None #pointer ke node berikutnya (awal=none)
# 1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menentukan node pertama (head)
head = nodeA

# 4) Traversal : Menelusuri dari head sampai akhir (None)
current = head
while current is not None:
    print(current.data) #Menampilkan data pada node saat ini
    current = current.next #Pindah ke node berikutnya

#=============================================================================================
#Implementasi Dasar : Linked List + Insert Awal
#=============================================================================================

class LinkedList:
    def __init__(self):
        self.head = None #awalnya kosong

    def insert_awal(self, data):
      #1) buat node baru
      nodeBaru = Node(data) #panggil class node

      #2) node baru menunjuk ke head lama
      nodeBaru.next = self.head

      #3) head pindah ke node baru
      self.head = nodeBaru
    def hapus_awal(self):
        data_terhapus = self.head.data
        #menggeser head ke node berikutnya
        self.head = self.head.next
        print("Node yang dihapus adalah:", data_terhapus)

    def tampilkan(self):  #Implementasi Traversal
          current = self.head
          while current is not None:
              print(current.data)
              current = current.next

print("=====List Baru=====")
ll = LinkedList() #instatiasi objek ke class linked list
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()