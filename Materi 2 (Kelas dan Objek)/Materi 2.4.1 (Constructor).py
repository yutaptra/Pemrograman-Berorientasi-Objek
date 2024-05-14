class Motor:
    def __init__(self, merek, tahun_pembuatan):
        self.merek = merek
        self.tahun_pembuatan = tahun_pembuatan

    def info(self):
        print(f"Merek: {self.merek}")
        print(f"Tahun Pembuatan: {self.tahun_pembuatan}")

motor1 = Motor("Honda", 2020)
motor1.info() # Output: merek: Honda, Tahun Pembuatan: 2020
