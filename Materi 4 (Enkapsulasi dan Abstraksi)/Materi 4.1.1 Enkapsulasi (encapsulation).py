class Anjing:
    def __init__(self, jenis, tahun):
        self._jenis = jenis
        self._tahun = tahun
        
    def __info(self):
        print(f"Anjing: {self._jenis} ({self._tahun})")
        
anjing1 = Anjing("Chihuahua", 2020)
anjing1._Anjing__info()  # Output: Anjing: Chihuahua (2020)

print(anjing1._jenis)  # Output: Chihuahua
