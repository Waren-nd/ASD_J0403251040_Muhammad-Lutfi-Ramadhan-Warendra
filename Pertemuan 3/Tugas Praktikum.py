# ==============================
# CIRCULAR LINKED LIST (SEARCH)
# ==============================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head


    def search(self, key):
        if self.head is None:
            return False

        temp = self.head

        while True:
            if temp.data == key:
                return True

            temp = temp.next
            if temp == self.head:
                break

        return False


cll = CircularLinkedList()

data = input("Masukkan elemen ke dalam Circular Linked List: ")

if data.strip() == "":
    print("(Tidak ada elemen)")
else:
    elemen = list(map(int, data.split(",")))

    for i in elemen:
        cll.append(i)

    cari = int(input("Masukkan elemen yang ingin dicari: "))

    if cll.search(cari):
        print(f"Elemen {cari} ditemukan dalam Circular Linked List.")
    else:
        print(f"Elemen {cari} tidak ditemukan dalam Circular Linked List.")


# ==============================
# SINGLE LINKED LIST (GABUNG)
# ==============================

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node


    def display(self):
        temp = self.head

        if temp is None:
            print("kosong")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("null")


    def gabung(self, list2):

        if self.head is None:
            self.head = list2.head
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = list2.head


ll1 = LinkedList()
ll2 = LinkedList()


data1 = input("\nMasukkan elemen untuk Linked List 1: ")

if data1.strip() != "":
    angka1 = list(map(int, data1.split(",")))

    for i in angka1:
        ll1.append(i)


data2 = input("Masukkan elemen untuk Linked List 2: ")

if data2.strip() != "":
    angka2 = list(map(int, data2.split(",")))

    for i in angka2:
        ll2.append(i)


print("\nLinked List 1: ", end="")
ll1.display()

print("Linked List 2: ", end="")
ll2.display()


ll1.gabung(ll2)

print("Linked List setelah digabungkan: ", end="")
ll1.display()