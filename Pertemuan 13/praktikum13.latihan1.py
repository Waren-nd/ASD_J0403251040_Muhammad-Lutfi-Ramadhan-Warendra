#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#Praktikum 13 - Graph III: Spanning Tree
#=============================================================================================
# Latihan 1 :  Memahami Konsep Spanning Tree
#=============================================================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan edge graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# Jawaban Analisis:
# 1. Perbedaan graph awal dan spanning tree:
#    - Graph awal  memiliki seluruh edge sehingga memungkinkan adanya banyak jalur dan cycle.
#    - Sedangkan spanning tree adalah bagian dari graph yang hanya menggunakan edge penting untuk menghubungkan semua vertex tanpa membentuk cycle.
#
#    Pada graph awal terdapat 5 edge:
#    (A,B), (A,C), (A,D), (C,D), dan (B,D)
#
#    Sedangkan spanning tree hanya memiliki 3 edge:
#    (A,C), (C,D), dan (D,B)
#
#    Walaupun jumlah edge berkurang, semua vertex tetap terhubung.


# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#
#    - Cycle adalah jalur melingkar yang kembali ke titik awal, Jika spanning tree memiliki cycle, maka ada edge yang sebenarnya tidak diperlukan karena masih ada jalur lain.
#    - Tujuan spanning tree adalah membentuk hubungan paling sederhana dan efisien antar vertex.
#
#    Oleh karena itu, cycle harus dihilangkan agar graph tidak memiliki hubungan yang redundan atau berulang.


# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#
#    Dalam teori graph, spanning tree dengan n vertex selalu memiliki tepat n-1 edge.
#
#    Alasannya:
#    - Jika edge kurang dari n-1, maka ada vertex yang tidak terhubung.
#    - Jika edge lebih dari n-1, maka akan terbentuk cycle.
#
#    Pada graph ini terdapat 4 vertex:
#    A, B, C, dan D
#
#    Maka jumlah edge spanning tree:
#    4 - 1 = 3 edge
#
#    Karena graph awal memiliki 5 edge, spanning tree menggunakan
#    edge lebih sedikit agar tetap terhubung tanpa cycle.