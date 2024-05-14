#adalah konsep di mana kita hanya menampilkan informasi penting dari suatu objek dan menyembunyikan informasi yang tidak penting.
from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

class BelahKetupat(Bentuk):
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
    def luas(self):
        return 0.5 * self.diagonal1 * self.diagonal2

class Segitiga(Bentuk):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def luas(self):
        return 0.5 * self.alas * self.tinggi

belah_ketupat1 = BelahKetupat(20, 10)
segitiga1 = Segitiga(4, 3)

print(belah_ketupat1.luas())  # output: 100.0
print(segitiga1.luas())       # output: 6.0

