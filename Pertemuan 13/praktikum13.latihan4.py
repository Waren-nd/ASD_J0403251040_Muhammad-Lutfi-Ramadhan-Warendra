#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#Praktikum 13 - Graph III: Spanning Tree
#=============================================================================================
# Latihan 4 : Studi Kasus: Jaringan Kabel Antar Gedung
#=============================================================================================
# Algoritma : Kruskal
#=============================================================================================

# Daftar edge graph dalam format:
# (bobot, gedung1, gedung2)
#
# Bobot menunjukkan biaya pemasangan kabel
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]


# Mengurutkan edge berdasarkan bobot terkecil
# Algoritma Kruskal selalu memilih biaya paling kecil terlebih dahulu
edges.sort()


# List untuk menyimpan hasil Minimum Spanning Tree (MST)
mst = []


# Variabel untuk menyimpan total biaya minimum
total_biaya = 0


# Set untuk menyimpan gedung yang sudah terhubung
connected = set()


# Perulangan untuk memeriksa setiap edge
for biaya, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    # Jika salah satu gedung belum terhubung,
    # maka edge dapat dimasukkan ke MST
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, biaya))

        # Menambahkan biaya ke total biaya
        total_biaya += biaya

        # Menandai gedung sudah terhubung
        connected.add(u)
        connected.add(v)


# Menampilkan hasil MST
print("Jaringan Kabel Minimum:")

# Menampilkan edge yang dipilih
for edge in mst:
    print(edge)


# Menampilkan total biaya minimum
print("\nTotal biaya minimum =", total_biaya)


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Algoritma apa yang digunakan?
#
#    Program ini menggunakan algoritma Kruskal.
#
#    Algoritma Kruskal bekerja dengan cara:
#    - Mengurutkan seluruh edge berdasarkan bobot terkecil.
#    - Memilih edge satu per satu.
#    - Edge dipilih jika tidak membentuk cycle.
#
#    Tujuannya adalah mendapatkan Minimum Spanning Tree (MST)
#    dengan total biaya minimum.


# 2. Edge mana saja yang dipilih?
#
#    Setelah edge diurutkan berdasarkan biaya,
#    edge yang dipilih adalah:
#
#    (GedungC, GedungD) = 1
#    (GedungA, GedungC) = 2
#    (GedungB, GedungD) = 3
#
#    Edge tersebut dipilih karena memiliki biaya paling kecil
#    dan tetap dapat menghubungkan semua gedung.


# 3. Berapa total biaya minimum?
#
#    Total biaya dihitung dari seluruh edge MST:
#
#    1 + 2 + 3 = 6
#
#    Jadi total biaya minimum pemasangan kabel adalah 6.


# 4. Mengapa MST cocok digunakan pada kasus ini?
#
#    MST cocok digunakan karena tujuan kasus ini adalah
#    menghubungkan seluruh gedung dengan biaya seminimal mungkin.
#
#    Dengan MST:
#    - Semua gedung tetap saling terhubung.
#    - Tidak ada jalur kabel yang berlebihan.
#    - Tidak terbentuk cycle yang menyebabkan pemborosan biaya.
#
#    Oleh karena itu, MST membantu membuat jaringan kabel
#    yang efisien dan hemat biaya.