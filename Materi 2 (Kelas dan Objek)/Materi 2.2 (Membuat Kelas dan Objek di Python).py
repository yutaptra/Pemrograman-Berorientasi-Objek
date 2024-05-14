class Kendaraan:
    # Atribut
    merek = ""
    warna = ""
    tahun_pembuatan = ""
    nomor_polisi = ""

    # Metode
    def nyalakan_mesin(self):
        print("Mesin dinyalakan.")

    def matikan_mesin(self):
        print("Mesin dimatikan.")

    def jalan_maju(self):
        print("Kendaraan bergerak ke depan.")

    def jalan_mundur(self):
        print("Kendaraan mundur.")

# Membuat objek
mobil1 = Kendaraan()
mobil1.merek = "Toyota"
mobil1.warna = "Hitam"
mobil1.tahun_pembuatan = "2020"
mobil1.nomor_polisi = "B 1234 AB"

# Memanggil metode objek
mobil1.nyalakan_mesin()
mobil1.jalan_maju()
mobil1.matikan_mesin()

# Membuat objek lainnya
motor1 = Kendaraan()
motor1.merek = "Honda"
motor1.warna = "Merah"
motor1.tahun_pembuatan = "2019"
motor1.nomor_polisi = "B 5678 CD"

# Memanggil metode objek lainnya
motor1.nyalakan_mesin()
motor1.jalan_mundur()
motor1.matikan_mesin()
