class Biodata(object) :
    def __init__(self , nama , alamat , jamSewa):
        self.nama = nama
        self.alamat = alamat
        self.jamSewa = jamSewa
    def jamSewa1(self , harga):
        hasil = self.jamSewa * harga
        return hasil

    def informasiBiodata(self):
        print()
        print("Informasi Biodata")
        print("nama : " , self.nama)
        print("alamat : " , self.alamat)
        print("jam sewa : " , self.jamSewa)