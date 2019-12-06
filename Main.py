from Mobil import *

mobil_awal = ["apv   " , "avansa" , "agya  "]
kode = [1 , 2 , 3 ]
harga = [200000 , 300000 , 400000]
warna = ["hitam" , "Merah" , "Hijau"]
print("------------Rental Mobil------------------")
ulang = mobil_awal.__len__()
print("Kode       Jenis Mobil    Harga Sewa / Hari")
for i in range(ulang) :
    print(kode[i] , "           " , mobil_awal[i] , "          " , harga[i])

pil = int(input("Silahkan Pilih : "))
nama = input("Input nama : ")
alamat = input("Input alamat :")
jamSewa = int(input("Input jam sewa : "))

if pil == kode[0] :
 mobil= Avp(nama , alamat , jamSewa , harga[0] , mobil_awal[0] , warna[0])
 mobil.informasiMobil()

elif pil == kode[1] :
 mobil= Avansa(nama , alamat , jamSewa , harga[1] , mobil_awal[1] , warna[1])
 mobil.informasiMobil()

elif pil == kode[2] :
 mobil= Avansa(nama , alamat , jamSewa , harga[2] , mobil_awal[2] , warna[2])
 mobil.informasiMobil()