#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#Praktikum 12 - Graph II: Shortest Path 
#====~========================================================================================
# Materi 1 : Implementasi Dijkstra 
#=============================================================================================

import heapq 
# Representasi graf dalam bentuk dictionary
# Setiap node memiliki dictionary tetangga dengan bobot (jarak)
graph = { 
    'A': {'B': 4, 'C': 2},  # Node A terhubung ke B dengan bobot 4, ke C dengan bobot 2
    'B': {'D': 5},          # Node B terhubung ke D dengan bobot 5
    'C': {'D': 1},          # Node C terhubung ke D dengan bobot 1
    'D': {}                 # Node D tidak memiliki tetangga
}

def dijkstra(graph, start): 
    # Menyimpan jarak minimum 
    distances = {node: float('inf') for node in graph} 
 
    # Jarak node awal = 0 
    distances[start] = 0 
 
    # Priority queue 
    pq = [(0, start)] 
 
    while pq: 
        current_distance, current_node = heapq.heappop(pq) 
 
        # Periksa semua tetangga 
        for neighbor, weight in graph[current_node].items(): 
 
            distance = current_distance + weight 
 
            # Jika ditemukan jarak lebih kecil 
            if distance < distances[neighbor]: 
            # Update jarak minimum
                distances[neighbor] = distance 
            # Masukkan tetangga ke priority queue untuk diproses
                heapq.heappush(pq, (distance, neighbor)) 
    # Kembalikan dictionary berisi jarak minimum dari node awal ke semua node
    return distances 

# Panggil fungsi Dijkstra dengan node awal 'A'
hasil = dijkstra(graph, 'A') 
print(hasil)

