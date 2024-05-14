# adalah konsep dalam pemrograman berorientasi objek yang memungkinkan penggunaan kelas 
# sebagai model atau blue print yang merepresentasikan objek dari dunia nyata atau 
# konsep yang kompleks dalam bentuk yang lebih sederhana.
from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass
    
class Ayam(Hewan):
    def suara(self):
        print("Kiw Kiw")
        
class Burung(Hewan):
    def suara(self):
        print("Cukurukuk")
        
sapi = Ayam()
sapi.suara()  # output: Kiw Kiw

kambing = Burung()
kambing.suara()  # output: Cukurukuk
