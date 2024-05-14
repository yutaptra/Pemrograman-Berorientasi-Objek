class Makhluk:
    def __init__(self, jenis, umur):
        self.jenis = jenis
        self.umur = umur
    
    def info(self):
        print(f"Makhluk: {self.jenis} ({self.umur} tahun)")

class Hewan(Makhluk):
    def __init__(self, jenis, umur, warna):
        super().__init__(jenis, umur)
        self.warna = warna
        
    def info(self):
        print(f"Hewan: {self.jenis} ({self.umur} tahun) - Warna Bulu: {self.warna}")

hewan1 = Hewan("Kucing", 3, "Putih")
hewan1.info()
