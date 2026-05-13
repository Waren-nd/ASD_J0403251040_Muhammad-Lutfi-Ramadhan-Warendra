#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#Praktikum 13 - Graph III: Spanning Tree
#=============================================================================================
# Latihan 5 : Buat Program MST dengan Kasus Baru
#=============================================================================================
# Algoritma : Kruskal
#=============================================================================================

# Daftar edge graph dalam format:
# (bobot, kota1, kota2)
#
# Bobot menunjukkan jarak atau biaya perjalanan antar kota
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]


# Mengurutkan edge berdasarkan bobot terkecil
# Algoritma Kruskal selalu memilih edge dengan bobot minimum terlebih dahulu
edges.sort()

# List untuk menyimpan hasil Minimum Spanning Tree (MST)
mst = []

# Variabel untuk menyimpan total bobot MST
total_bobot = 0

# Set untuk menyimpan kota yang sudah terhubung
connected = set()

# Perulangan untuk memeriksa setiap edge
for bobot, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    # Jika salah satu kota belum terhubung,
    # maka edge dapat dimasukkan ke MST
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, bobot))

        # Menambahkan bobot ke total bobot
        total_bobot += bobot

        # Menandai kota sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil Minimum Spanning Tree
print("Minimum Spanning Tree:")

# Menampilkan edge yang dipilih
for edge in mst:
    print(edge)


# Menampilkan total bobot MST
print("\nTotal bobot minimum =", total_bobot)


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Kasus apa yang dipilih?
#
#    Kasus yang dipilih adalah
#    "Jaringan Jalan Antar Kota".
#
#    Kota yang digunakan:
#    Bogor, Jakarta, Depok, dan Bandung.


# 2. Algoritma apa yang digunakan?
#
#    Program ini menggunakan algoritma Kruskal.
#
#    Algoritma Kruskal bekerja dengan cara:
#    - Mengurutkan edge berdasarkan bobot terkecil.
#    - Memilih edge satu per satu.
#    - Edge dipilih jika tidak membentuk cycle.
#
#    Tujuannya adalah mendapatkan
#    Minimum Spanning Tree (MST)
#    dengan total bobot minimum.


# 3. Edge mana saja yang dipilih dalam MST?
#
#    Setelah edge diurutkan,
#    edge yang dipilih adalah:
#
#    (Bogor, Depok) = 2
#    (Depok, Jakarta) = 3
#    (Depok, Bandung) = 4
#
#    Ketiga edge tersebut berhasil
#    menghubungkan semua kota
#    dengan total bobot paling kecil.


# 4. Berapa total bobot MST?
#
#    Total bobot dihitung dari:
#
#    2 + 3 + 4 = 9
#
#    Jadi total bobot Minimum Spanning Tree adalah 9.


# 5. Mengapa edge tertentu tidak dipilih?
#
#    Edge seperti:
#    (Bogor, Jakarta) = 5
#    (Jakarta, Bandung) = 6
#
#    tidak dipilih karena sudah ada jalur lain
#    dengan bobot lebih kecil yang dapat
#    menghubungkan semua kota.
#
#    Jika edge tersebut ditambahkan,
#    maka akan menambah total bobot
#    dan dapat membentuk cycle.
#
#    Oleh karena itu edge tersebut
#    tidak termasuk dalam MST.