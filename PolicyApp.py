from VehiclePortal import Car, Bike, Vehicle
from Employees import Employee


class Policy:
    @staticmethod
    def display_policy(vehicle: Vehicle, years):
        if years < 5:
            amount = vehicle.calculate_premium()
        else:
            amount = vehicle.calculate_premium() + 1000
        print(f'Total premium due for {vehicle} is {amount}')


print('------------User-----------')
"""Following code is a part of User module"""


class User:
    @staticmethod
    def show_premium(vehicle: Vehicle):
        years = int(input('Enter how old is the vehicle '))
        Policy.display_policy(vehicle, years)


my_car = Car('Honda', 'City', 1500000)
my_bike = Bike('Bajaj', 'xyz', 100000)
my_self = Employee(3445, 'aaa', 70000)

User.show_premium(my_car)
User.show_premium(my_bike)
# show_premium(my_self) duck-typing

print('------------Admin-----------')
"""Following code is for admin module"""
vehicles = [my_car, my_bike]
"""report to see policy applied in current year"""
for v in vehicles:
    Policy.display_policy(v, years=1)
