class Motor:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna

    def __del__(self):
        print(f"{self.merek} {self.warna} dihapus")

motor1 = Motor("Honda", "Hitam")
del motor1
