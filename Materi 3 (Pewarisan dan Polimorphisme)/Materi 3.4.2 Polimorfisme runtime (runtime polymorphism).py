class Hewan:
    def __init__(self, jenis, tahun):
        self.jenis = jenis
        self.tahun = tahun
    
    def info(self):
        print(f"Hewan: {self.jenis} ({self.tahun})")

class Kucing(Hewan):
    def __init__(self, jenis, tahun, warna):
        super().__init__(jenis, tahun)
        self.warna = warna
        
    def info(self):
        print(f"Kucing: {self.jenis} ({self.tahun}) - Warna: {self.warna}")

class Anjing(Hewan):
    def __init__(self, jenis, tahun, jenis_anjing):
        super().__init__(jenis, tahun)
        self.jenis_anjing = jenis_anjing
        
    def info(self):
        print(f"Anjing: {self.jenis} ({self.tahun}) - Jenis Anjing: {self.jenis_anjing}")

Hewan1 = Hewan("Hewan", 2022)
kucing1 = Kucing("Persia", 2019, "Putih")
anjing1 = Anjing("Golden Retriever", 2017, "Domestik")

Hewan1.info()  # output: Hewan: Hewan (2022)
kucing1.info()   # output: Kucing: Persia (2019) - Warna: Putih
anjing1.info()   # output: Anjing: Golden Retriever (2017) - Jenis Anjing: Domestik
