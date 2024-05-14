class Motor:
    # class attribute
    brand = "Honda"

    def __init__(self, model, tahun):
        self.model = model
        self.tahun = tahun

    # class method
    @classmethod
    def change_brand(cls, new_brand):
        cls.brand = new_brand

# create objects
motor1 = Motor("Vario", 2022)
motor2 = Motor("CBR", 2021)

# access class attribute
print(motor1.brand)  # output: Honda
print(motor2.brand)  # output: Honda

# access and change class attribute
print(Motor.brand)  # output: Honda
Motor.change_brand("Yamaha")
print(Motor.brand)  # output: Yamaha
print(motor1.brand)  # output: Yamaha
print(motor2.brand)  # output: Yamaha

class Motor:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna

motor1 = Motor('Subaru', 'Pink')
motor2 = Motor('Ferrari', 'Ungu')

print(motor1.merek) # Output: Subaru
print(motor2.warna) # Output: Hitam
