class Mahasiswa: #pendefinisian sebuah kelas Mahasiswa dengan method __init__.
    def __init__(self, nama, nim, jurusan): #fungsi untuk menginisialisasi nama, nim, dan jurusan mahasiswa
        self.nama = nama #penginisialisasian nama
        self.nim = nim   #penginisialisasian nim/npm
        self.jurusan = jurusan   #penginisialisasian jurusan
    
    def tampilkan_info(self):       #fungsi untuk menampilkan data mahasiswa yang sudah diinisialisasi sebelumnya
        print("Nama:", self.nama)   #printout untuk nama
        print("NIM:", self.nim)     #printout untuk NPM
        print("Jurusan:", self.jurusan.NamaJurusan)     #printout untuk jurusan


class Jurusan:      #pendefinisian kelas Jurusan dengan metode __init__ untuk menginisialisasi nama jurusan dan daftar mahasiswa
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []
    
    def tambah_mahasiswa(self, mahasiswa):    #fungsi tambah mahasiswa untuk menampilkan mahasiswa yang sudah didefinisikan dengan metode append
        self.DaftarMahasiswa.append(mahasiswa)
    
    def tampilkan_daftar_mahasiswa(self):   #fungsi tampilkan daftar mahasiswa 
        if len(self.DaftarMahasiswa) == 0:  #merupakan fungsi if atau logika untuk melihat apakah mahasiswa terdaftar dalam data 
            print("Tidak ada mahasiswa terdaftar dalam jurusan", self.NamaJurusan)  #jika mahasiswa tidak ada (tidak ditemukan dalam data), maka akan mengeluarkan output seperti kode di samping
        else:
            print("Daftar mahasiswa di jurusan", self.NamaJurusan + ":")    #jika mahasiswa ditemukan, maka akan mengeluarkan output seperti kode di samping
            for mahasiswa in self.DaftarMahasiswa:  #sebagai format jika mahasiswa ditemukan dalam data, maka akan dipanggil seperti kode dibawah
                print("Nama:", mahasiswa.nama, 
                      "\nNPM :", mahasiswa.nim)     #pemanggilan dengan format "Nama :" dan "NPM :"


class Universitas:      #pendefinisian kelas universitas yang akan memuat nama universitas dan fungsi-fungsi seperti init, tambah jurusan, dan tampilkan jurusan
    def __init__(self, nama_universitas):       #mendefiniskan nama universitas
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []
    
    def tambah_jurusan(self, jurusan):      #fungsi untuk menambahkan jurusan 
        self.DaftarJurusan.append(jurusan)  #pemanggilan jurusan yang sudah dideklarasikan
    
    def tampilkan_daftar_jurusan(self):     #fungsi untuk menampilkan jurusan 
        if len(self.DaftarJurusan) == 0:    #merupakan fungsi if atau logika untuk melihat apakah jurusan terdaftar dalam data 
            print("Tidak ada jurusan terdaftar di", self.NamaUniversitas)   #jika jurusan tidak ditemukan, maka akan mengeluarkan output seperti kode di samping
        else:
            print("Daftar jurusan di", self.NamaUniversitas + ":")  #jika jurusan ditemukan, maka akan menamplikan daftar jurusan di universitas yang dideklarasikan 
            for jurusan in self.DaftarJurusan:
                print(jurusan.NamaJurusan)  #menampilkan nama jurusan yang ada di universitas yang  dideklarasikan
    
# Objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# Objek Jurusan dengan nama "Teknik Informatika" dan ditambahkan ke dalam Universitas XYZ
new_jurusan = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(new_jurusan)

# Objek Mahasiswa dengan nama dan npm yang  dimasukkan ke dalam Jurusan Teknik Informatika di Universitas XYZ
new_mahasiswa = Mahasiswa("Rana Qonitah Helida", "G1A022017", new_jurusan)
new_jurusan.tambah_mahasiswa(new_mahasiswa)

# Menampilkan daftar jurusan yang ada di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()

# Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
new_jurusan.tampilkan_daftar_mahasiswa()

