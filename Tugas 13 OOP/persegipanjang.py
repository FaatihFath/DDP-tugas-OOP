import math
class PersegiPanjang():
    panjang = 0 
    lebar = 0 
    luas = 0
    kelilng = 0
    def __init__(self, panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar
        
    def ukur_luas(self):
        self.luas = 2 * (self.panjang + self.lebar)
        
    def ukur_keliling(self):
        self.keliling = 2 * (self.panjang + self.lebar)
        
    def cetak(self):
        print("luas :", self.luas)
        print("keliling :", self.kelilng)
        print("panjang :", self.panjang)
        print("lebar :", self.lebar)
       