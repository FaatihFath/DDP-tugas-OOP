import math
class SegitigaSiku2():
    alas = 0
    tinggi = 0
    luas = 0
    keliling = 0
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        
    def ukur_luas(self):
        self.luas = 0.5 * self.alas * self.tinggi
    
    def ukur_keliling(self):
        bagian_miring = self.alas**2 + self.tinggi**2
        bagian_miring = math.sqrt(bagian_miring)
        self.keliling = self.alas + self.tinggi + bagian_miring    
        
    def cetak(self):
        print("luas:", self.luas)
        print("keliling :", self.keliling)
        print("alas :", self.alas)
        print("tinggi :", self.tinggi)   