# Public: variabel dan method yang dapat diakses dari luar class. Nama variabel dan method diawali dengan huruf kecil.
class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        
    def info(self):
        print(f"Hewan: {self.nama} ({self.umur} tahun)")
    
print("Public")     
hewan1 = Hewan("Anjing", 3)
print(hewan1.nama)  # output: Anjing
hewan1.info()       # output: Hewan: Anjing (3 tahun)

# Private: variabel dan method yang tidak dapat diakses dari luar class. Nama variabel dan method diawali dengan underscore (_).
class Hewan:
    def __init__(self, nama, umur):
        self._nama = nama
        self._umur = umur
        
    def info(self):
        print(f"Hewan: {self._nama} ({self._umur} tahun)")
        
print("Private")  
hewan1 = Hewan("Ayam", 5)
print(hewan1._nama)  # output: Ayam
hewan1.info()        # output: Hewan: Ayam (5 tahun)

# Protected: variabel dan method yang hanya dapat diakses dari dalam class dan subclass. Nama variabel dan method diawali dengan double underscore (__)
class Hewan:
    def __init__(self, nama, umur):
        self.__nama = nama
        self.__umur = umur
        
    def info(self):
        print(f"Hewan: {self.__nama} ({self.__umur} tahun)")
        
class Anjing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.__jenis_bulu = jenis_bulu
        
    def info(self):
        super().info()
        print(f"Jenis Bulu: {self.__jenis_bulu}")
        
print("Protected")  
anjing1 = Anjing("Chihuahua", 2, "Fluffy")
print(anjing1.__nama)  # error: 'Anjing' object has no attribute '__nama'
anjing1.info()  # output: Hewan: Chihuahua (2 tahun)\nJenis Bulu: Fluffy