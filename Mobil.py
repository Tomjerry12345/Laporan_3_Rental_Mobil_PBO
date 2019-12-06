from Biodata import Biodata

class Avp(Biodata) :

   def __init__(self , nama , alamat , jamSewa , harga , mobil , warna):
       super().__init__(nama , alamat , jamSewa)
       self.harga = harga
       self.mobil = mobil
       self.warna = warna

   def totBayar(self):
       return super().jamSewa1(self.harga)

   def informasiMobil(self):
       super().informasiBiodata()
       print()
       print("Informasi Mobil")
       print("Merek : " , self.mobil)
       print("Warna : ", self.warna)
       print("Total Bayar : " , self.totBayar())

class Avansa(Avp) :
    pass
class Agya(Avp) :
    pass
