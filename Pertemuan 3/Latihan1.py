#==============================================
#Pertemuan 3 
#==============================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSingleLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None    # Menambahkan atribut tail
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: #jika linked list masih kosong
            self.head = new_node
            self.tail = new_node  # Inisialisasi tail saat menambahkan node pertama
            self.tail.next = self.head  # Membuat circular link
        else:
            self.tail.next = new_node  # Gunakan tail untuk menambahkan node di akhir
            self.tail = new_node       # Perbarui tail ke node baru
            self.tail.next = self.head  # Circular link kembali ke head
    def display(self):
        if not self.head:
            print("List is empty")
            return
        print("Circular Linked List Traversal:")
        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next

        while temp != self.head:  # Loop hingga kembali ke head
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")
    
L= CircularSingleLinkedList()
L.insert_at_end(3)
L.insert_at_end(5)
L.insert_at_end(13)
L.insert_at_end(2)
L.display()

#LATIHAN 1
L.delete_node(5)
L.display()