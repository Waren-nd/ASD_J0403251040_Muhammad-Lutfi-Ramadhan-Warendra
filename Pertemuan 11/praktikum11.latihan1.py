#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================
#=============================================================================================
# Latihan 1 : Studi Kasus BFS (Jalur Terdekat Lokasi)
#=============================================================================================


# struktur data untuk membuat antrian, kita gunakan dari library collections bawaan python
from collections import deque 


# representasi graph
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    # Fungsi untuk melakukan penelusuran graph dengan BFS
    # graph : Dictionary yang menyimpan struktur graph
    # start : node awal penelusuran

    # Queue digunakan untuk menyimpan node yang akan diproses / dibaca
    queue = deque()

    # Variabel untuk menyimpan node yang sudah diproses / dikunjungi
    visited = set()

    # Masukkan node awal ke queue
    queue.append(start)

    # Tandai node awal sebagai sudah dikunjungi
    visited.add(start)

    while queue:
        # Mengambil node paling depan dari queue
        node = queue.popleft()

        # Menampilkan node yang sedang dikunjungi
        print(node, end=" ")

        # Periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            # Jika tetangga belum dikunjungi
            if neighbor not in visited:
                # Tandai tetangga sebagai sudah dikunjungi
                visited.add(neighbor)

                # Masukkan tetangga ke queue untuk diproses selanjutnya
                queue.append(neighbor)

# Menjalankan BFS dari node Rumah
print("BFS dari Rumah:")
bfs(graph, 'Rumah')

'''''
Jawaban Analisis :
1. Node mana yang dikunjungi pertama?

Node yang pertama dikunjungi adalah A,
karena BFS selalu dimulai dari node awal (start node).

2. Mengapa BFS cocok untuk mencari jalur terdekat?
BFS cocok untuk mencari jalur terdekat karena menelusuri graph berdasarkan level 
(jarak terdekat dulu). Node yang paling dekat dari titik awal akan dikunjungi lebih dulu, 
sehingga jalur yang ditemukan merupakan jalur dengan jumlah langkah paling sedikit.

3. Apa perbedaan urutan BFS jika struktur graph diubah? 
Urutan BFS dapat berubah jika:

- struktur graph berubah (edge berbeda)
- urutan tetangga diubah

Karena BFS mengikuti urutan node yang masuk ke dalam queue,
maka hasil traversal bisa berbeda meskipun node-nya sama.
'''''