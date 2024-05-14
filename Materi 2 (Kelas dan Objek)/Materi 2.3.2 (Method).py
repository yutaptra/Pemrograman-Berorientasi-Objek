class Motor:
    def __init__(self, merek, tahun_pembuatan):
        self.merek = merek
        self.tahun_pembuatan = tahun_pembuatan

    def description(self):
        print("Ini adalah motor", self.merek, "tahun", self.tahun_pembuatan)

motor1 = Motor("Honda", 2020)
motor1.description() # Output: Ini adalah motor Honda tahun 2020.
