class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

car = ElectricCar("Tesla", "Model S", 2022, 75)
print(f"Car: {car.make} {car.model} {car.year} with battery size {car.battery_size} kWh")






















# The ElectricCar class inherits from Car and adds an additional attribute, battery_size.