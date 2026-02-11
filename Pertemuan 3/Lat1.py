#==============================================
#Pertemuan 3 
#==============================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularSingleLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def delete_node(self, key):
        if not self.head:
            print("List is empty")
            return
        
        curr = self.head
        prev = self.tail
        
        # Jika head yang akan dihapus
        if curr.data == key:
            # Jika hanya ada satu node
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            return
        
        # Mencari node yang akan dihapus
        curr = curr.next
        prev = self.head
        
        while curr != self.head:
            if curr.data == key:
                prev.next = curr.next
                
                # Jika yang dihapus adalah tail
                if curr == self.tail:
                    self.tail = prev
                
                return
            prev = curr
            curr = curr.next
        
        print("Data tidak ditemukan")
    def search(self, key):
        if not self.head:
            return False
        
        curr = self.head
        
        while True:
            if curr.data == key:
                return True
            curr = curr.next
            if curr == self.head:
                break
        
        return False
    def display(self):
        if not self.head:
            print("List is empty")
            return
        
        print("Circular Linked List Traversal:")
        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next

        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("(null)")
    
    def merge(self, list2):
        if not self.head:
            self.head = list2.head
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = list2.head

    
L = CircularSingleLinkedList()
L.insert_at_end(3)
L.insert_at_end(5)
L.insert_at_end(13)
L.insert_at_end(2)
L.display()

# LATIHAN 1
L.delete_node(5)
L.display()

#LATIHAN 2
CSL1 = CircularSingleLinkedList()
CSL1.insert_at_end(3)
CSL1.insert_at_end(7)
CSL1.insert_at_end(12)
CSL1.insert_at_end(19)
CSL1.insert_at_end(25)
CSL1.display()

#x = int(input("Masukkan elemen yang ingin dicari: "))
#match CSL1.search(x):
#    case True:
#        print("Elemen ditemukan.")
#   case False:
#        print("Elemen tidak ditemukan.")

#LATIHAN 4
LL1 = CircularSingleLinkedList()
data1 = [1, 3, 5, 7]
for data in data1:
    LL1.insert_at_end(data)

# Linked List 2
LL2 = CircularSingleLinkedList()
data2 = [2, 4, 6, 8]
for data in data2:
    LL2.insert_at_end(data)

print("Linked List 1:")
LL1.display()

print("Linked List 2:")
LL2.display()

# Gabungkan
LL1.merge(LL2)

print("Linked List setelah digabungkan:")
LL1.display()
