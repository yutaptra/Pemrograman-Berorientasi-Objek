class Anjing:
    def __init__(self, nama, umur):
        self._nama = nama
        self._umur = umur
        
    def get_nama(self):
        return self._nama
    
    def set_nama(self, nama):
        self._nama = nama
        
    def get_umur(self):
        return self._umur
    
    def set_umur(self, umur):
        self._umur = umur
        
anjing1 = Anjing("Woof", 3)
print(anjing1.get_nama())  # output: Woof
anjing1.set_nama("Puppy")
print(anjing1.get_nama())  # output: Puppy
print(anjing1.get_umur())  # output: 3
anjing1.set_umur(4)
print(anjing1.get_umur())  # output: 4
