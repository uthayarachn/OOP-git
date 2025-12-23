class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def drive(self):
        print(f"{self.brand} {self.model} is driving")


class ElectricCar(Car):
    def __init__(self, model, brand, battery_size):
        super().__init__(model, brand)
        self.battery_size = battery_size

    def charge(self):
        print(f"The {self.battery_size} kWh battery is charging")


# สร้างออบเจกต์รถธรรมดา
my_car = Car("vios", "toyota")
my_car.drive()

# สร้างออบเจกต์รถไฟฟ้า
ev_car = ElectricCar("model 3", "tesla", 75)
ev_car.drive()
ev_car.charge()