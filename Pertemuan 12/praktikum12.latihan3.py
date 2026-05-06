#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#Praktikum 12 - Graph II: Shortest Path 
#=============================================================================================
# Latihan 3 : Implementasi Bellman Ford 
#=============================================================================================

# Weighted graph dengan bobot negatif 
graph = { 
    'A': {'B': 5, 'C': 4}, 
    'B': {}, 
    'C': {'B': -2} 
} 
 
def bellman_ford(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Bellman-Ford. 
    """ 
 
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
 
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
 
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1 
    for _ in range(len(graph) - 1): 
        # Periksa semua edge 
        for node in graph: 
            for neighbor, weight in graph[node].items(): 
                # Jika jarak ke node saat ini sudah diketahui, 
                # dan ditemukan jarak yang lebih kecil ke neighbor, 
                # maka lakukan update jarak 
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 
 
    return distances 
 
hasil = bellman_ford(graph, 'A') 
 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance) 

# ==========================================================
# Jawaban Analisis:
# 1. Bobot langsung dari A ke B adalah 5.
# 2. Total bobot jalur A -> C -> B = 4 + (-2) = 2.
# 3. Jalur A -> C -> B menghasilkan jarak lebih kecil menuju B (2 < 5).
# 4. Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena
#    algoritma ini melakukan relaksasi berulang kali sehingga tetap bisa
#    menemukan jarak terpendek meskipun ada edge berbobot negatif.
# 5. Proses relaksasi edge adalah langkah membandingkan jarak saat ini ke
#    suatu node dengan jarak alternatif melalui edge lain, lalu memperbarui
#    jarak jika ditemukan nilai yang lebih kecil.
# 6. Perbedaan utama Bellman-Ford dan Dijkstra:
#    - Dijkstra hanya bekerja dengan bobot positif, sedangkan Bellman-Ford
#      bisa menangani bobot negatif dan mendeteksi siklus negatif.
#    - Dijkstra menggunakan priority queue untuk efisiensi, sedangkan
#      Bellman-Ford lebih sederhana namun lebih lambat (O(V*E)).
# ==========================================================
