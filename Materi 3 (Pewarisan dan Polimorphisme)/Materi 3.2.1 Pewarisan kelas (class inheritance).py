class Makhluk:
    def __init__(self, jenis, umur):
        self.jenis = jenis
        self.umur = umur
    
    def info(self):
        print(f"Makhluk: {self.jenis} ({self.umur})")
        
class Hewan(Makhluk):
    def __init__(self, jenis, umur, warna_bulu):
        super().__init__(jenis, umur)
        self.warna_bulu = warna_bulu
        
    def info(self):
        super().info()
        print(f"Warna Bulu: {self.warna_bulu}")

hewan1 = Hewan("Kucing", 5, "Hitam")
hewan1.info()
