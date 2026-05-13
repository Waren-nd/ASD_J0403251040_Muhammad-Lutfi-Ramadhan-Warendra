#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#Praktikum 13 - Graph III: Spanning Tree
#=============================================================================================
# Latihan 2 : Implementasi Sederhana Algoritma Kruskal 
#=============================================================================================

# Daftar edge graph dalam format:
# (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]


# Mengurutkan edge berdasarkan bobot terkecil
# Algoritma Kruskal selalu memilih edge dengan bobot minimum terlebih dahulu
edges.sort()


# Menyimpan hasil Minimum Spanning Tree (MST)
mst = []


# Variabel untuk menyimpan total bobot MST
total_weight = 0


# Set digunakan untuk menyimpan node yang sudah terhubung
connected = set()


# Perulangan untuk mengecek setiap edge
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    # Jika salah satu node belum terhubung,
    # maka edge dapat dimasukkan ke MST
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan bobot edge ke total bobot
        total_weight += weight

        # Menandai node sudah terhubung
        connected.add(u)
        connected.add(v)


# Menampilkan hasil Minimum Spanning Tree
print("Minimum Spanning Tree:")

# Perulangan untuk menampilkan setiap edge MST
for edge in mst:
    print(edge)


# Menampilkan total bobot MST
print("Total bobot =", total_weight)


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Edge mana yang dipilih pertama kali?
#
#    Edge pertama yang dipilih adalah: 
#    (C, D) dengan bobot 1
#
#    Karena setelah diurutkan, edge tersebut memiliki
#    bobot paling kecil dibanding edge lainnya.


# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#
#    Algoritma Kruskal bertujuan mencari Minimum Spanning Tree (MST),
#    yaitu spanning tree dengan total bobot minimum.
#
#    Oleh karena itu, edge dengan bobot terkecil dipilih terlebih dahulu
#    agar total biaya atau total bobot graph menjadi sekecil mungkin.
#
#    Proses ini dilakukan terus menerus selama edge tersebut
#    tidak membentuk cycle.


# 3. Berapa total bobot MST yang dihasilkan?
#
#    Edge yang dipilih:
#    (C, D) = 1
#    (A, C) = 2
#    (B, D) = 3
#
#    Total bobot:
#    1 + 2 + 3 = 6
#
#    Jadi total bobot MST yang dihasilkan adalah 6.


# 4. Mengapa edge tertentu tidak dipilih?
#
#    Edge seperti:
#    (A, B) = 4
#    (A, D) = 5
#
#    tidak dipilih karena semua node sudah terhubung
#    sebelum edge tersebut diperiksa.
#
#    Jika edge tersebut tetap ditambahkan,
#    maka akan terbentuk cycle atau jalur berulang.
#
#    Hal itu bertentangan dengan konsep spanning tree
#    yang harus terhubung tanpa cycle.