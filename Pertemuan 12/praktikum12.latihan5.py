#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#Praktikum 12 - Graph II: Shortest Path 
#=============================================================================================
# Latihan 5 : Studi Kasus dengan Program Shortest Path  
#=============================================================================================

import heapq

# Representasi graph berbobot menggunakan dictionary
# Bobot menunjukkan jarak (misalnya waktu tempuh atau biaya)
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}


# Fungsi Dijkstra untuk mencari jarak terpendek
def dijkstra(graph, start):
    # Inisialisasi semua jarak dengan tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke dirinya sendiri = 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, lewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Jika ditemukan jarak lebih kecil, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Menentukan node awal (Bogor) dan menjalankan algoritma
start_node = 'Bogor'
hasil = dijkstra(graph, start_node)

# Output jarak terpendek dari node awal ke semua node
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")

# ==========================================================
# Jawaban Analisis:
# 1. Node awal yang digunakan adalah Bogor.
# 2. Node yang memiliki jarak paling kecil dari Bogor adalah Depok (2).
# 3. Node yang memiliki jarak paling besar dari Bogor adalah Bandung (8).
# 4. Algoritma Dijkstra bekerja dengan cara:
#    - Menginisialisasi semua jarak dengan tak hingga, kecuali node awal = 0.
#    - Menggunakan priority queue untuk memilih node dengan jarak terkecil.
#    - Melakukan relaksasi edge: memperbarui jarak ke tetangga jika ditemukan
#      jalur lebih pendek.
#    - Proses berulang sampai semua node sudah diproses.
#    Pada kasus ini, Dijkstra menemukan jalur optimal Bogor -> Depok -> Jakarta
#    dan Bogor -> Depok -> Bandung sehingga menghasilkan jarak sesuai output.
# ==========================================================
