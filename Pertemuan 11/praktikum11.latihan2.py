#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================
#=============================================================================================
# Latihan 2 : Studi Kasus DFS (Eksplorasi Jalur) 
#=============================================================================================

# representasi graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    # Fungsi untuk melakukan penelusuran graph dengan DFS
    # graph : Dictionary yang menyimpan struktur graph
    # node  : node yang sedang dikunjungi
    # visited : menyimpan node yang sudah dikunjungi

    # Tandai node sebagai sudah dikunjungi
    visited.add(node)

    # Menampilkan node yang sedang dikunjungi
    print(node, end=" ")

    # Periksa semua tetangga dari node
    for neighbor in graph[node]:
        # Jika tetangga belum dikunjungi
        if neighbor not in visited:
            # Lanjutkan penelusuran ke node tersebut (rekursif)
            dfs(graph, neighbor, visited)

# Variabel untuk menyimpan node yang sudah dikunjungi
visited = set()

# Menjalankan DFS dari node A
print("DFS dari A:")
dfs(graph, 'A', visited)

'''''
Jawaban Analisis :
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
DFS menggunakan pendekatan rekursif (atau stack) sehingga akan terus
menelusuri satu jalur sampai ke node paling dalam sebelum kembali (backtracking).
Oleh karena itu, DFS selalu masuk ke node terdalam terlebih dahulu.

2. Apa yang terjadi jika urutan neighbor diubah?
ika urutan neighbor diubah, maka urutan hasil DFS juga akan berubah.
Hal ini karena DFS mengikuti urutan neighbor yang ada dalam graph.
Contohnya jika ['B','C'] diubah menjadi ['C','B'], maka jalur DFS akan berbeda.

3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
DFS: A B D E C F  (menelusuri sampai dalam dulu)
BFS: A B C D E F  (menelusuri per level)
Perbedaan:
- DFS masuk ke dalam (depth) terlebih dahulu
- BFS menyebar ke samping (level) terlebih dahulu
'''''