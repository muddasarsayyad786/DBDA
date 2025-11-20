from Day4.VehiclePortal import Taxi, Bus
from RentalService import Rental


class RentalApp:
    @staticmethod
    def display_rent(rental_vehicle: Rental):
        print('----Welcome to My Rental App-----')
        hrs = int(input('Enter the hours for which you want to rent : '))
        amount = rental_vehicle.calculate_rent(hrs)
        print(f'Total rent for {rental_vehicle} : Rs. {amount}')


print('----The USER -----')
taxi = Taxi('Tata', 'abc', 120000, 12345)
RentalApp.display_rent(taxi)

bus = Bus('ttt', 'ppp', 240000, 1289)
RentalApp.display_rent(bus)