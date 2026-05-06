#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#Praktikum 12 - Graph II: Shortest Path 
#=============================================================================================
# Materi 2 : Implementasi Bellman Ford  
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

def bellman_ford(graph, start): 
    # Inisialisasi jarak awal semua node dengan tak hingga (inf)
    distances = {node: float('inf') for node in graph} 
    # Jarak node awal ke dirinya sendiri = 0
    distances[start] = 0 

    # Relaksasi dilakukan sebanyak (jumlah node - 1) kali
    # Karena pada graf dengan N node, jalur terpanjang tanpa siklus hanya memiliki N-1 edge
    for _ in range(len(graph) - 1): 

        # Iterasi setiap node dalam graf
        for node in graph: 
 
            # Iterasi setiap tetangga dari node
            for neighbor, weight in graph[node].items(): 

                # Jika jarak melalui node saat ini lebih kecil dari jarak yang tersimpan
                if distances[node] + weight < distances[neighbor]: 
                    # Update jarak minimum ke tetangga
                    distances[neighbor] = distances[node] + weight 
    
    # Kembalikan hasil jarak minimum dari node awal ke semua node
    return distances 

# Panggil fungsi Bellman-Ford dengan node awal 'A'
hasil = bellman_ford(graph, 'A')
print(hasil)