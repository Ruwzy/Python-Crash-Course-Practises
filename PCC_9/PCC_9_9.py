class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has" + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):       
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " -kwh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately" + str(range)
        message += "miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


test_car = ElectricCar("Jeep", "Wrangler Rubicon", 2018)
test_car.battery.describe_battery()

print("\nUpgrad the battery, and check it again: ")
test_car.battery.upgrade_battery()
test_car.battery.describe_battery()

print("\nTry upgrading the 2nd time: ")
test_car.battery.upgrade_battery()
test_car.battery.describe_battery()
