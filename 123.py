class Vehicle:
    vehicle_type = "none"

class Car(Vehicle):
    price = 1000000

    def horse_powers(self):
        return 200

class Nissan(Car):
    def __init__(self):
        self.vehicle_type = "SUV"
        self.price = 50000

    def horse_powers(self):
        return 250

nissan_car = Nissan()
print(nissan_car.vehicle_type)
print(nissan_car.price)
