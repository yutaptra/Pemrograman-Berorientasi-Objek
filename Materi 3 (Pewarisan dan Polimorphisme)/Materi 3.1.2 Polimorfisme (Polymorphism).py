class Hewan:
    def bersuara(self):
        pass

class Ayam(Hewan):
    def bersuara(self):
        print("Kukuruyuk!")

class Kambing(Hewan):
    def bersuara(self):
        print("Mbek!")

hewan1 = Ayam()
hewan2 = Kambing()

for hewan in [hewan1, hewan2]:
    hewan.bersuara()
