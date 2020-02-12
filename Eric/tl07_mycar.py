from tl07_class_car import Car,Battery,ElectricCar

my_newcar=Car('audi','a4',2016)
print(my_newcar.get_descriptive_name())
my_newcar.update_odometer(30)
my_newcar.read_odometer()
my_newcar.update_odometer(10000)
my_newcar.read_odometer()
my_newcar.update_odometer(30)
my_newcar.read_odometer()
my_newcar.increment_odometer(100)
my_newcar.read_odometer()

my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.battery_size=85
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()