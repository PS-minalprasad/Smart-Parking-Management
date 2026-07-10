class Vehicle:
    def __init__(self, vehicle_no, owner_name):
        self.vehicle_no = vehicle_no
        self.owner_name = owner_name
        self.__parking_fee = 0  # Encapsulation

    def set_fee(self, fee):
        self.__parking_fee = fee

    def get_fee(self):
        return self.__parking_fee

    def calculate_fee(self):
        pass

    def display(self):
        print("\nVehicle Number :", self.vehicle_no)
        print("Owner Name     :", self.owner_name)
        print("Parking Fee    : ₹", self.__parking_fee)


class Car(Vehicle):
    def calculate_fee(self):
        self.set_fee(100)


class Bike(Vehicle):
    def calculate_fee(self):
        self.set_fee(50)