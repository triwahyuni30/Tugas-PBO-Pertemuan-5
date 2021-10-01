class BurungMerpati :
    def terbang(self) : 
        print("Burung Merpati bisa terbang") 
    def renang(self) : 
        print("Burung Merpati tidak bisa berenang")
        
class Penguin : 
    def terbang(self) : 
        print("Penguin tidak bisa terbang") 
    def renang(self) :   
        print("Penguin bisa berenang")



def tes_terbang(hewan) :
    hewan.terbang()

bumer = BurungMerpati()
pe = Penguin()

tes_terbang(bumer)
tes_terbang(pe)