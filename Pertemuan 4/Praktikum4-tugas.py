#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

#=============================================================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
#=============================================================================================
# ------------------------------
# Class Node
# Merepresentasikan satu data pelanggan dalam antrian
# ------------------------------
class Node:
    def __init__(self, no, nama, servis):
        self.no = no          # Nomor antrian
        self.nama = nama      # Nama pelanggan
        self.servis = servis  # Jenis servis
        self.next = None      # Pointer ke node berikutnya


# ------------------------------
# Class QueueBengkel
# Mengelola antrian pelanggann 
# ------------------------------
class QueueBengkel:
    def __init__(self):
        self.front = None  # Pointer ke depan (pelanggan pertama)
        self.rear = None   # Pointer ke belakang (pelanggan terakhir)

    # ------------------------------
    # Method enqueue
    # Menambahkan pelanggan ke belakang antrian
    # ------------------------------
    def enqueue(self, no, nama, servis):
        # Membuat node baru
        new_node = Node(no, nama, servis)

        # Jika antrian kosong
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            # Hubungkan node terakhir ke node baru
            self.rear.next = new_node
            # Pindahkan pointer rear ke node baru
            self.rear = new_node

        print("Pelanggan berhasil ditambahkan ke antrian.")

    # ------------------------------
    # Method dequeue
    # Melayani pelanggan terdepan
    # ------------------------------
    def dequeue(self):
        # Jika antrian kosong
        if self.front is None:
            print("Antrian kosong! Tidak ada pelanggan untuk dilayani.")
            return

        # Simpan node terdepan
        dilayani = self.front

        # Pindahkan front ke node berikutnya
        self.front = self.front.next

        # Jika setelah dequeue antrian menjadi kosong
        if self.front is None:
            self.rear = None

        print("\nMelayani Pelanggan:")
        print("No Antrian :", dilayani.no)
        print("Nama       :", dilayani.nama)
        print("Servis     :", dilayani.servis)
        print("Pelanggan telah dilayani dan keluar dari antrian.")

    # ------------------------------
    # Method tampilkan
    # Menampilkan seluruh pelanggan dalam antrian
    # ------------------------------
    def tampilkan(self):
        # Jika antrian kosong
        if self.front is None:
            print("Antrian kosong.")
            return

        print("\nDaftar Antrian Pelanggan:")
        print("-" * 40)

        current = self.front  # Mulai dari depan
        while current is not None:
            print("No Antrian :", current.no)
            print("Nama       :", current.nama)
            print("Servis     :", current.servis)
            print("-" * 40)
            current = current.next  # Pindah ke node berikutnya


# ------------------------------
# Fungsi utama program
# ------------------------------
def main():
    q = QueueBengkel()  # Membuat objek antrian

    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama      : ")
            servis = input("Servis    : ")
            q.enqueue(no, nama, servis)

        elif pilih == "2":
            q.dequeue()

        elif pilih == "3":
            q.tampilkan()

        elif pilih == "4":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid!")


# Menjalankan program
if __name__ == "__main__":
    main()