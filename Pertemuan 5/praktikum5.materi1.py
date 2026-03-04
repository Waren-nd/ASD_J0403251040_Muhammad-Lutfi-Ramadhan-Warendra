#=============================================================================================
#Nama    : Muhammad Lutfi Ramadhan Warendra
#NIM     : J0403251040
#Kelas   : TPL B2
#=============================================================================================

#=============================================================================================
#Materi Rekursif : Faktorial
# recursive case => 3! = 3 x 2 x 1 
# base case 0 berhenti
#=============================================================================================

def faktorial(n):
    #base case
    #Jika n == 0, maka hasil faktorial adalah 1
    # (karena 0! = 1)
    if n == 0:
        return 1
    #recursive case
    return n*faktorial(n-1)  #n-1*n-2*n-3 ......... n-?

print("======Program Faktorial======")
print("Hasil Faktorial : ", faktorial(3))

