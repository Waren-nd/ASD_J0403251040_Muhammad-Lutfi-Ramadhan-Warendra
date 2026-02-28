#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

#=============================================================================================
#Implementasi Dasar : Queue Berbasis Linked List
#=============================================================================================

#Membuat kelas node (merupakan unit dasar dari Linked List)
class Node:
    def __init__(self,data): #konstruktor untuk inisialisasi node
        self.data = data #Menyimpan nilai/data
        self.next = None #pointer ke node berikutnya (awal=none)

#Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None  #Node paling belakang

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data): 
        #Menambah data di belakang (rear)
        nodeBaru = Node(data)

        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        self.rear.next = nodeBaru
        self.rear = nodeBaru 
    def dequeue(self):
        #Menghapus data dari depan (front)
        data_terhapus = self.front.data #peek dalam queue

        #1)Lihat(peek) data yang paling depan
        data_terhapus = self.front.data 

        #2) geser front ke node berikutnya
        self.front = self.front.next

        
        #3) Jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus jadi none
        if self.front is None:
            self.rear = None

        return data_terhapus

    def tampilkan(self):
        #Menampilkan isi queue dari front ke rear
        current = self.front
        print("Front ", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Rear")

#Instantiasi objek class QueueLL
q = QueueLL() 

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()