import math
class Lingkaran():
    pi = 3.14
    jari_jari = 0
    luas = 0
    keliling = 0
    
    def __init__(self, jari_jari) :
        self.jari_jari = jari_jari
        
    def ukur_luas(self):
        self.luas = self.pi * self.jari_jari * self.jari_jari
        
    def ukur_keliling(self):
        self.keliling = 2 * self.pi * self.jari_jari
        
    def cetak(self):
        print("luas :", self.luas)
        print("keliling :", self.keliling)
        print("jari - jari", self.jari_jari)
