#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#Praktikum 13 - Graph III: Spanning Tree
#=============================================================================================
# Latihan 3 : Implementasi Algoritma Prim 
#=============================================================================================

# Digunakan untuk mengambil edge dengan bobot terkecil secara otomatis
import heapq


# Representasi graph menggunakan dictionary
# Format:
# 'Node': {'Tetangga': bobot}
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}


# Fungsi algoritma Prim
def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Priority queue untuk menyimpan edge berdasarkan bobot terkecil
    edges = []

    # Memasukkan seluruh edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil Minimum Spanning Tree
    mst = []

    # Menyimpan total bobot MST
    total_weight = 0

    # Perulangan selama masih ada edge
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi
        if v not in visited:

            # Menandai node sudah dikunjungi
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan bobot ke total bobot
            total_weight += weight

            # Memeriksa seluruh tetangga dari node baru
            for neighbor, w in graph[v].items():

                # Jika tetangga belum dikunjungi
                if neighbor not in visited:

                    # Menambahkan edge ke priority queue
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan hasil MST dan total bobot
    return mst, total_weight


# Menjalankan algoritma Prim mulai dari node A
mst, total = prim(graph, 'A')


# Menampilkan hasil Minimum Spanning Tree
print("Minimum Spanning Tree:")

# Menampilkan setiap edge pada MST
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total)


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Node awal apa yang digunakan?
#
#    Node awal yang digunakan adalah node A.
#
#    Hal ini terlihat pada pemanggilan fungsi:
#    prim(graph, 'A')
#
#    Algoritma Prim akan mulai membangun MST
#    dari node tersebut.


# 2. Edge mana yang dipilih pertama kali?
#
#    Dari node A terdapat beberapa edge:
#    A-B = 4
#    A-C = 2
#    A-D = 5
#
#    Edge dengan bobot terkecil adalah:
#    (A, C) = 2
#
#    Oleh karena itu edge pertama yang dipilih adalah
#    A ke C.


# 3. Bagaimana Prim menentukan edge berikutnya?
#
#    Setelah memilih satu edge,
#    algoritma Prim akan memeriksa seluruh edge
#    yang terhubung dengan node yang sudah dikunjungi.
#
#    Kemudian Prim memilih edge dengan bobot terkecil
#    yang menuju node yang belum dikunjungi.
#
#    Proses ini dilakukan terus menerus sampai
#    semua node terhubung.
#
#    Pada graph ini urutan edge yang dipilih:
#    (A, C) = 2
#    (C, D) = 1
#    (D, B) = 3


# 4. Berapa total bobot MST yang dihasilkan?
#
#    Total bobot dihitung dari seluruh edge MST:
#
#    2 + 1 + 3 = 6
#
#    Jadi total bobot Minimum Spanning Tree adalah 6.


# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#
#    Algoritma Prim:
#    - Memulai dari satu node awal.
#    - Mengembangkan tree sedikit demi sedikit.
#    - Selalu memilih edge terkecil dari node
#      yang sudah terhubung.
#
#    Algoritma Kruskal:
#    - Tidak dimulai dari node tertentu.
#    - Langsung mengurutkan seluruh edge berdasarkan bobot.
#    - Memilih edge terkecil satu per satu
#      selama tidak membentuk cycle.
#
#    Jadi, Prim berfokus pada pengembangan node,
#    sedangkan Kruskal berfokus pada pemilihan edge global.