from vehicle import Car, Bike

class ParkingLot:

    def __init__(self):
        self.vehicles = []

    def park_vehicle(self):
        vehicle_no = input("Enter Vehicle Number: ")
        owner = input("Enter Owner Name: ")

        print("\n1. Car")
        print("2. Bike")

        choice = input("Enter Choice: ")

        if choice == "1":
            vehicle = Car(vehicle_no, owner)
        else:
            vehicle = Bike(vehicle_no, owner)

        vehicle.calculate_fee()
        self.vehicles.append(vehicle)

        print("\nVehicle Parked Successfully!")

    def show_vehicles(self):

        if not self.vehicles:
            print("\nParking Lot is Empty")
            return

        for vehicle in self.vehicles:
            vehicle.display()

    def search_vehicle(self):

        number = input("Enter Vehicle Number: ")

        for vehicle in self.vehicles:
            if vehicle.vehicle_no == number:
                vehicle.display()
                return

        print("Vehicle Not Found")

    def remove_vehicle(self):

        number = input("Enter Vehicle Number: ")

        for vehicle in self.vehicles:
            if vehicle.vehicle_no == number:
                self.vehicles.remove(vehicle)
                print("Vehicle Removed Successfully")
                return

        print("Vehicle Not Found")

    def total_collection(self):

        total = 0

        for vehicle in self.vehicles:
            total += vehicle.get_fee()

        print("\nTotal Parking Collection : ₹", total)