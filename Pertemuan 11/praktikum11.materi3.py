#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================
#====~=========================================================================================
# Materi 3 : Implementasi DFS
#=============================================================================================

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

def dfs(graph,node,visited):
#Fungsi untuk melakukan penelusuran graph menggunakan DFS
#graph : dictionary yang menyimpan graph
#node : menyimpan node yang sedang dikunjungi
#visited : menyimpan node yang sudah dikunjungi

    #tandai node saat ini sebagai sudah dikunjungi
    visited.add(node)

    #tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    #periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:

        #jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            #lakukan DFS secara rekursif pada tetangga tersebut
            dfs(graph, neighbor, visited)

#set visited
visited = set()

#menjalankan DFS dari node A
dfs(graph, 'A', visited)