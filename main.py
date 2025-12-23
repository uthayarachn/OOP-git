class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
        self.is_moving = True

    def drive(self):
        print(f"{self.brand} {self.model} is driving")

    def apply_brake(self):
        print("Slowing down...")
        self.is_moving = False


class ElectricCar(Car):
    def __init__(self, model, brand, battery_size):
        super().__init__(model, brand)
        self.battery_size = battery_size

    def charge(self):
        print(f"The {self.battery_size} kWh battery is charging")


# สร้างออบเจกต์รถธรรมดา
my_car = Car("vios", "toyota")
my_car.drive()
print(my_car.is_moving)
my_car.apply_brake()
print(my_car.is_moving)

print("------")

# สร้างออบเจกต์รถไฟฟ้า
ev_car = ElectricCar("model 3", "tesla", 75)
ev_car.drive()
ev_car.apply_brake()
ev_car.charge()
print(ev_car.is_moving)

# สร้างออบเจกต์รถไฟฟ้า
ev_car = ElectricCar("model 3", "tesla", 75)
ev_car.drive()
ev_car.apply_brake()
ev_car.charge()
print(ev_car.is_moving)