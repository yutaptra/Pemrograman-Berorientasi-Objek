class Motor:
    def __init__(self, merek, tahun_pembuatan):
        self.merek = merek
        self.tahun_pembuatan = tahun_pembuatan
        
motor1 = Motor("Honda", 2020)
print(motor1.merek) # Output: Honda
