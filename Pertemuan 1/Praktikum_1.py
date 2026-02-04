#===================================================
#Pratikum 1 : Konsep ADT dan FIle Handling
#Latihan Dasar 1A : Membaca Seluruh isi file
#===================================================

#membuka file dengan mode read ("r")
with open ("data_mahasiswa.txt","r", encoding="latin-1") as file:
    isi_file = file.read() #membaca keseluruhan isi file dalam satu string
print(isi_file)

#membuka file per baris
print("===Hasil Read===")
print("tipe data", type(isi_file))
print("Jumlah Karakter", len(isi_file))
print("jumlah baris", isi_file.count("\n")+1)

#membuka file per baris
print("---Membaca File per Baris---")
jumlah_baris = 0
with open("data_mahasiswa.txt","r", encoding="latin-1") as file:
    for baris in file:
        jumlah_baris +=1
        baris = baris.strip() #menghilangkan baris baru \n
        print("Baris ke-", jumlah_baris)
        print ("Isinya : ",baris)

#===================================================
#Pratikum 1 : Konsep ADT dan FIle Handling
#Latihan Dasar 2 : Parsing baris menjadi kolom data
#===================================================

with open ("data_mahasiswa.txt","r", encoding="latin-1") as file:
     for baris in file:
        baris = baris.strip()
        jumlah_baris = jumlah_baris + 1
        if baris =="":
            continue
        nim, nama, nilai = baris.split(",") # parsing data berdasarkan karakter
        print("NIM: ", nim, "| Nama: ", nama, "| Nilai: ", nilai)


#===================================================
#Pratikum 1 : Konsep ADT dan FIle Handling
#Latihan Dasar 3 : Membaca file dan menyimpan ke List
#===================================================
data_list = [] #List untuk menampung data mahasiswa
with open ("data_mahasiswa.txt","r", encoding="latin-1") as file:
    for baris in file: 
        baris = baris.strip()
        #Simpan sebagai List " [nim,nama,nilai]"
        data_list.append([nim,nama,int(nilai)])

print("=== Data Mahasiswa dalama List===")
print(data_list)
print("jumlah Record", len(data_list))

print("===Menampilkan Data Record Tertentu===")
print("Contoh Record pertama: ",data_list[0])

#===================================================
#Pratikum 1 : Konsep ADT dan FIle Handling
#Latihan Dasar 4 : Membaca file dan menyimpan ke Dictionary
#===================================================

data_dict = {} #buat variabel untuk dictionary
with open ("data_mahasiswa.txt","r", encoding="latin-1") as file:
    for baris in file:
        print(baris)
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        #Simpan data Mahasiswa ke dictioary dengan key NIM
        data_dict[nim] = {                  #key
            "nama" : nama,                  #values
            "nilai": int(nilai)             #values
        }
print("===Data Mahasiswa dalam Dictionary===")
print(data_dict)