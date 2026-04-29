#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================
#=============================================================================================
# Materi 2 : Implementasi BSF 
#=============================================================================================

#struktur data untuk membuat antrian, kita gunakan dari library collections bawaan python
from collections import deque 


#representasi graph 
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(graph, start):
    #Fungsi untuk melakukan penelusuran graph dengan BFS
    # graph : Dictionary yang menyimpan struktur dari graph
    #start : node awal penelusuran

    #Queue digunakan untuk menyimpan node yang akan diproses / dibaca
    queue = deque()

    #Variabel yang digunakan untuk menyimpan node yang sudah diprose / dikunjungi
    visited = set()

    #Masukkan node awal ke queue
    queue.append(start)

    #tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start)

    while queue:
        #mengambil node paling depan dari queue
        node = queue.popleft() 

        #tampilkan node yang sedang dikunjungi
        print(node, end=" ") 

        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #jika tetangga belum dikunjungi
            if neighbor not in visited:
                #tandai tetangga sebagai sudah dikunjungi
                visited.add(neighbor)
                #masukkan tetangga ke queue untuk diproses selanjutnya
                queue.append(neighbor)
            
#menjalankan BFS dari node A
bfs(graph, 'A')